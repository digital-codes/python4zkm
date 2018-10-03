import numpy as np
from moviepy.editor import VideoClip

# video image format 
w = 640
h = 480
#create a numpy array for the image data
p = np.ndarray(shape=(h,w,3),dtype="uint8")

# function as 
# frame data generator. Parameter t is time in s
# at 20 fps increment is 0.05
def img(t):
    cv = 256 # colors
    col = (t * 20) % cv # set the color per frame
    # set all pixels
    for r in range(h):
        for c in range(w):
            if ((r < h/2) and (c < w/2)) or ((r >= h/2) and (c >= w/2)):
               p[r,c] = (0,col,0)
            else:
               p[r,c] = (col,0,col)
    return p

# setup the animation
animation = VideoClip(img, duration=5)
# write the video file
animation.write_videofile("simpleVideo.webm",fps=20,audio=False)

