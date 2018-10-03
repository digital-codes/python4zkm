import numpy as np
##import matplotlib.pyplot as plt
##from mpl_toolkits.mplot3d import Axes3D 
##import matplotlib.animation as animation
import io
import time

from moviepy.editor import VideoClip, VideoFileClip, AudioFileClip, CompositeVideoClip, TextClip
from vispy import app, scene, visuals
from vispy.gloo.util import _screenshot
from vispy import color

from scipy import misc


# textfile
tf = "zkmaudio.txt"
tenc = "utf-8"
#tenc = "iso-8859-15"

#with open(tf,"r",encoding="iso-8859-15") as infile:
with open(tf,"r",encoding=tenc) as infile:
     #tdf = io.StringIO(infile.read())
     td = infile.read()
infile.close()

tdf = io.StringIO(td.replace(".","\n").replace(",","\n"))

#make list of lines
tls = tdf.readlines() # replace(".","\n").split("\n")

# make binary array and detect max length
llen = 0
lines = []
for l in tls:
    lb = bytearray(l.upper().rstrip(),tenc)
    llen = max(llen, len(lb))
    lines.append(lb)

# extend lines to same size
bl = bytearray(" ",tenc) * llen 
for i in range(len(lines)):
    if len(lines[i]) < llen:
        lines[i] += bl[len(lines[i]):]

lcnt = len(lines)

#########


#########
# initialize 
# make sure to have the indexes right ...
xx = np.linspace(0,llen,llen)  # llen is max line length
yy = np.linspace(0,lcnt,lcnt) # lcnt is number of lines
x, y = np.meshgrid(yy, xx) # x is cols, y is rows
# fill z with increasing number of lines
zarray = np.full((lcnt, lcnt, llen),32)
for z in range(lcnt):
    for i in range(z):
        zarray[z][i] = lines[i] 

#########
canvas = scene.SceneCanvas(keys='interactive',bgcolor=(0,.3,.3,1))
view = canvas.central_widget.add_view()
cam1 = scene.PanZoomCamera(aspect=1) #SomeCamera()
view.camera = cam1
view.camera = 'turntable'

#### the time variable function: select the Z plane
Z = lambda t: zarray[int(t % lcnt)] # /127

surface = scene.visuals.SurfacePlot(x= np.linspace(0,lcnt-1,lcnt),
                        y=np.linspace(0,llen-1,llen), z= Z(0),
                        shading="smooth", color=(0.5, 0.5, 1, 1))

surface.transform = scene.transforms.MatrixTransform()
surface.transform.scale([1/20, 1/20, 1/200])
surface.transform.translate([-1.5, -2., 0.])
surface.transform.rotate(-45,(0,0,1))
surface.transform.rotate(-10,(1,0,0))


view.add(surface)
p = surface.parent
canvas.show()

#### display 
fms = lcnt # one plane
for i in range (fms):
    surface.set_data(z = Z(int(i%lcnt))) # Update the mathematical surface
    surface.color = (1.-i/fms,1,i/fms,1)
    canvas.bgcolor=(0,.3-i/(fms*10),.3,1)
    canvas.on_draw(None) # Update the image on Vispy's canvas
    app.process_events()
    time.sleep(.05)

# terminate with info text
txt1 = 'Generating video file ...'
#t1 = visuals.TextVisual(txt1, color='white', \
t1 = scene.visuals.Text(txt1, color='red', \
    pos=[canvas.size[0] // 4, canvas.size[1] // 3], anchor_x='left', anchor_y='bottom')
t1.font_size = 30

# the procedure to get the z odering right is quite strange ...
# need to set set parent of t1 to that of the scene
# the set a higher order to t1 (scene has order 0)
# however, we cannot add t1, but add as subvisual ...
t1.order = 1
t1.parent = surface.parent
view.add_subvisual(t1)

app.process_events()
time.sleep(2)
t1.parent = None # we have to clear the parent to remove the text
view.remove_subvisual(t1) # and remove the subvisual
app.process_events()
## write video

fnum = 0

def make_frame(t):
    global fnum
    # paramter t is time in seconds. so for 20 fps every second
    # has 20 calls. this is not the frame number
    # so multiply by some factor to get a faster movie
    surface.set_data(z = Z(fnum)) # Update the mathematical surface
    fnum += .25
    # optionally change color ...
    surface.color = (np.clip(1.-fnum/20,0,1),1,np.clip(fnum/20,0,1),1)
    canvas.bgcolor=(0,np.clip(.3-(fnum/20),0,1),.3,1)
    # optionally call event loop. this will make the video
    ## follow the user interactions .... 
    app.process_events()
    # draw and capture
    canvas.on_draw(None) # Update the image on Vispy's canvas
    return _screenshot((0,0,canvas.size[0],canvas.size[1]))[:,:,:3]


#animation = VideoClip(make_frame, duration=5).resize(width=350)
#animation = VideoClip(make_frame, duration=5).resize(width=800,height=600)

animation = VideoClip(make_frame, duration=10)

#animation.write_gif('otto.gif', fps=2, opt='OptimizePlus')
animation.write_videofile("surfVideo.webm",preset="medium",fps=20,audio=False)

######### close canvas only here ...
app.process_events()
canvas.close()
app.process_events()
app.quit()

#try to create sound version ...
audioclip = AudioFileClip("zkmaudio.wav")
videoclip = VideoFileClip("surfVideo.webm")
l = videoclip.duration
print("video length:",l)
audio = audioclip.set_duration(l) # same length as video
videoclip.set_audio(audio)
#textclip = TextClip("ZKM Open Codes", fontsize=20, color='white').set_pos("center","center")
# get font list with:
#TextClip.list("font")
# we could also add the text directly, see above
textclip = TextClip("ZKM Open Codes", font="FreeSans",fontsize=40, color='white',method='label')
t = textclip.set_duration(l)
# compose everything. make sure to set audio here!
finalclip = CompositeVideoClip([videoclip.set_audio(audio),t.set_pos("center","center")])
finalclip.write_videofile("surfVideo_sound.webm",preset="medium",fps=20)

