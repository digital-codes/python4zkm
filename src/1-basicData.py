# this time, we use more external modules
import matplotlib.pyplot as plt
import numpy as np
import wave
import sys
import pygame
import time
import random
from mpl_toolkits.mplot3d import Axes3D


# playing and plotting data from a wave file

# pgame stuff related to playing sound
pygame.mixer.pre_init(24000, size=-16, channels=1)
pygame.mixer.init(buffer=2) # very small buffer here to reduce latency
pygame.init()


useWav = False
fileBase = "../data/otto"  # zkmaudio
wavFile = fileBase + ".wav"
txtFile = fileBase + ".txt"


# plotly output looks nice for the wav file

if useWav:
    spf = wave.open(wavFile,'r')
    #Check we have a mono file
    if spf.getnchannels() == 2:
        print ('Just mono files')
        sys.exit(0)
    #Extract Raw Audio from Wav File
    signal = spf.readframes(2000 )#-1)
    signal = np.fromstring(signal, 'Int16')[800:]
    print("Using ",wavFile)
else:
    # try to read a text file
    try:
        with open(txtFile) as f:
            signal = f.read()
            signal.replace("\n"," ")
            print("Using ",txtFile)
    except:
        #alternatively, we can plot from a string entered manually like so:
        signal = "dqpinfqfmmdqwpdqwpdqwodmopmodpwndeniqwqwnfojqnwd"
        print("Using ", signal)

    txtSignal = signal # make a copy of the text
    signal = np.fromstring(signal.upper(), "uint8")
    sigMin = min(signal)
    signal -= min(signal)
    signal = np.clip(signal,0,100)
    #signal -= int(np.mean(signal))


# make x and z from signal
# limit number of points, important for wav file
min3d = 0
max3d = len(signal)
if len(signal) > 1000:
    for i in range(len(signal)):
                   if abs(signal[i]) > 1000:
                       min3d = i
                       break
    max3d = min(len(signal), min3d + 200 )
    print("min ",min3d,", max ",max3d)

#x3d = [i for i in range(min3d,max3d)]
#y3d = [signal[i] % 10 for i in range(min3d,max3d)]
#z3d = [signal[i] % 100 for i in range(min3d,max3d)]
x3d = [random.randint(0,max3d-min3d) for i in range(0,max3d-min3d)]
y3d = [random.randint(0,max3d-min3d) for i in range(0,max3d-min3d)]
z3d = [signal[i] for i in range(min3d,max3d)]
#label3d = [chr(signal[i]+sigMin)  for i in range(min3d,max3d)]
label3d = ["%d" % (signal[i])  for i in range(min3d,max3d)]
pntSize = 9 # 00

plt.ioff()
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(x3d,y3d,z3d, s= pntSize)

for i in range(len(x3d)):
    ax.text(x3d[i],y3d[i],z3d[i], label3d[i], size=20)

plt.axis("off")
plt.title('A pile of numbers ...')
plt.get_current_fig_manager().full_screen_toggle()
elevation = 10
angle = 30
while None == plt.waitforbuttonpress(.1):
    ax.view_init(elev = elevation, azim=angle)
    plt.draw()
    #plt.pause(.001)
    angle += 3
    elevation += 10

# uncomment the show call if you want to manually rotate the
# plot after the animation
plt.show()

# 2d signal
plt.figure()
plt.title('Sequential numbers: A Wave display/timeseries...')
plt.plot(signal)
plt.get_current_fig_manager().full_screen_toggle()
plt.show()

# we can also create a 2d plot in the following way
# reshape the vector into a symetric 2d array
ncols = np.trunc(np.sqrt(len(signal))) # get lower bound of square root
signal = signal[:int(ncols*ncols)]  # take correct number of samples
signal2d = np.reshape(signal, (-1, int(ncols))) # reshape
plt.imshow(signal2d) # create image
plt.title('2D arranged numbers: An Image ...')
plt.get_current_fig_manager().full_screen_toggle()
plt.show()

# recalculate 3d PARMS
max3d = len(signal)
x3d = [random.randint(0,max3d-min3d) for i in range(0,max3d-min3d)]
y3d = [random.randint(0,max3d-min3d) for i in range(0,max3d-min3d)]
z3d = [signal[i] for i in range(min3d,max3d)]

# surface plot with plt
from mpl_toolkits.mplot3d import Axes3D

x = np.arange(0,ncols)
y = np.arange(0,ncols)
x,y = np.meshgrid(x,y)
hf = plt.figure()
ha = hf.add_subplot(111, projection='3d')

#ha.plot_surface(len(signal), len(signal), signal2d, color='b')
ha.plot_surface(x,y, signal2d, color='b')

plt.title('3D-stlye arranged numbers: A Surface Plot ...')
plt.get_current_fig_manager().full_screen_toggle()
plt.show()


##### text display if not wav
if not useWav:
    label3d = ["%c" % (signal[i]+sigMin)  for i in range(min3d,max3d)]
    pntSize = 0
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.scatter(x3d,y3d,z3d, s= pntSize)

    for i in range(len(x3d)):
        ax.text(x3d[i],y3d[i],z3d[i], label3d[i], size=20)

    plt.axis("off")
    plt.title('A pile of numbers with encoding: characters ...')
    plt.get_current_fig_manager().full_screen_toggle()
    elevation = 10
    angle = 30
    while None == plt.waitforbuttonpress(.1):
        ax.view_init(elev = elevation, azim=angle)
        plt.draw()
        #plt.pause(.001)
        angle += 3
        elevation += 10
    plt.close()


# for audio output, apply some mods
# make list longer
longSignal = signal
for i in range(100):
    longSignal = np.append(longSignal,signal)
# create array
#longSignal = np.fromstring(longSignal, "int16")
# plot the new signal ....

#plt.plot(longSignal[:100])
plt.figure()
plt.get_current_fig_manager().full_screen_toggle()
plt.plot(longSignal[:100].astype(np.uint8))
plt.title('Turning numbers into sound: High pitch ...')
plt.show()
# play
sd = pygame.mixer.Sound(longSignal)
sd.play()
# wait until the sound is finished
while pygame.mixer.get_busy():
    pass
# wait another half second
time.sleep(.5)
# make a lower tone by repeating each element individually
sl = len(longSignal)
longSignal = np.repeat(longSignal, 4)
# plot the new signal ....
plt.figure()
plt.get_current_fig_manager().full_screen_toggle()
plt.plot(longSignal[:100].astype(np.uint8))
plt.title('Turning numbers into sound: Low pitch ...')
plt.show()
# play
sd = pygame.mixer.Sound(longSignal[:sl])
sd.play()

#important to wait until sound finished
while pygame.mixer.get_busy():
    pass

# and then to stop mixes, as it infers with espeak
pygame.mixer.stop()

##########################################
# initialize speech output
#for windows speech, we need win32 stuff
import platform
if "windows" in platform.system().lower():
    import win32api
    import win32com.client
import pyttsx3;

# prepare speech
engine = pyttsx3.init();
voices = engine.getProperty('voices')
for v in voices:
    #print("voice:",v.name)
    if "german" in v.name.lower(): #"german":
        engine.setProperty('voice', v.id)
        engine.setProperty("rate",150)
        break

#####################################
# Load a video and show it with moviepy
# Import everything needed to edit video clips
from moviepy.editor import *

clip = VideoFileClip("../data/ottos-mops.webm")
fps = clip.fps
dur = clip.duration
sz = clip.size
nframes = fps*dur

fig = plt.subplot(1,3,1) #figure()
plt.get_current_fig_manager().full_screen_toggle()
fig.axis("off")
plt.title('Ottos Mops hops ...')

if not useWav:
    tfig = plt.subplot(1,3,2)
    tfig.axis("off")
    tfig.annotate(txtSignal,\
        xy=(1, 1), xytext=(.4,.8), xycoords="data", \
        textcoords="axes fraction",ha="left", va="top", size=14)

    import wordcloud
    wc = wordcloud.WordCloud().generate_from_text(txtSignal)
    wfig = plt.subplot(1,3,3)
    wfig.axis("off")
    wfig.imshow(wc)


plt.ion()
#plt.show()


#############
# prepare text for speech output
text = txtSignal.replace("\n",".").replace("..",".")
lines = text.split(".")

for i in range(int(nframes)):
    frame = np.array(clip.get_frame(i))
    fig.imshow(frame)
    plt.draw()
    plt.pause(.05)
    if i < len(lines):
        engine.say(lines[i])
        engine.runAndWait()
    plt.pause(.1)
