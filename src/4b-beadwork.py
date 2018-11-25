import numpy as np
from matplotlib import pyplot as plt
import matplotlib.animation as animation
import imageio
import sys
from moviepy.editor import VideoClip

#colors
colors = ((255,255,255),(0,0,0),(255,0,0),(0,255,0))
# bead patterns
bead5 = np.array(((0,0,1,0,0),(0,1,1,1,0),(1,1,1,1,1),(0,1,1,1,0),(0,0,1,0,0)))
bead7 = np.array(((0,0,1,1,1,0,0),(0,1,1,1,1,1,0),(1,1,1,1,1,1,1),(1,1,1,1,1,1,1),(1,1,1,1,1,1,1),(0,1,1,1,1,1,0),(0,0,1,1,1,0,0)))
bead9 = np.array(((0,0,1,1,1,1,1,0,0),(0,1,1,1,1,1,1,1,0),(1,1,1,1,1,1,1,1,1),(1,1,1,1,1,1,1,1,1),(1,1,1,1,1,1,1,1,1),(1,1,1,1,1,1,1,1,1),(1,1,1,1,1,1,1,1,1),(0,1,1,1,1,1,1,1,0),(0,0,1,1,1,1,1,0,0)))
# select one of the patterns
bead = bead7

# a typical pattern is like:
# 0r,2g 1s,3w 0r,2g ...
# 1w,3s 0g,2r 1w,3s ...
# pairs start on same column

def mkBead(y,x,col):
    """ create color pattern"""
    p = np.empty((np.shape(bead)[0],np.shape(bead)[1],3),dtype=np.uint8)
    p.fill(128)
    for i in range(np.shape(bead)[0]):
        for j in range(np.shape(bead)[1]):
            if bead[i,j] == 1:
                p[i,j] = np.array(colors[col])
    # set color
    I[y:y+np.shape(bead)[0],x:x+np.shape(bead)[1]] = p

# row, col, size, index, left/right, color)
def mkThread(y,x, s, i, d, c):
    """position row,col, length, index, direction, colors (0,1) """
    b = np.shape(bead)[1]
    #d = 1
    #print("dir ",d)
    for j in range(s):
        if d == 1:
            # top left to bottom right diagonal
            # cl starts with 0
            cl = c[0] if j < i else c[1]
        else:
            # top right to bottom left diagonal
            # cl 1 start with s
            cl = c[0] if j >= s- i else c[1]

        mkBead(y,x+j*b,cl)

        
# image dimensions, depends on beads and triangle width
W = 10 # triangle width in beds
T = 8  # triangles in row, 
R = 4  # Triangle rows. multiple of 4, normally
M = np.shape(bead)[0]*W*R # rows
N = np.shape(bead)[1]*W*T # cols

s = N // T

# empty image. needs additional dimentsion for RGB color
I = np.empty((M,N,3), dtype = np.uint8)

# background fill individual colors
I.fill(255)

J = []


for r in range(W*R):
    for t in range(T):
        # row, col, size, index, left/right, color)
        # direction must change every tile and row
        # dir 0 for even/even and odd/odd
        d = 0 if (0 == (r // W) % 2) and (0 == t % 2) else \
            0 if (1 == (r // W) % 2) and (1 == t % 2) else 1
        # colors are circucar, so order is reversed in odd row
        c = (0,1) if (t % 2) == 0 and (0 == (r // W) % 2) else \
            (2,3) if (t % 2) == 1 and (0 == (r // W) % 2) else \
            (3,2) if (t % 2) == 0 and (1 == (r // W) % 2) else (1,0)
        mkThread(r*np.shape(bead)[1],t*s,W, r % W, d,c)
        J.append(I.copy())

imageio.imwrite("bead_lin.jpg",I)

############## display #########
f = plt.figure()
p1 = f.add_subplot(211)
p1.set_title("Result")
p1.axis('off')
p1.imshow(I)

p2 = f.add_subplot(212)
p2.set_title("Process")
p2.axis('off')
 
################################
# plot animation function
def plotReplay(f):
    if f >= len(J):
        im.set_array(J[len(J) - 1])
    else:
        im.set_array(J[f])
    return im,  # the trailing comma is important !!!

im = p2.imshow(np.ones(np.shape(I)), animated=True)

# give some extra frames for the movie trailer
ani = animation.FuncAnimation(f, plotReplay, interval=20, frames=len(J) + 20, blit=True)


ani.save("bead_ani_lin.mp4")

plt.show()

plt.close()

# uncomment exit if you want the real video
sys.exit()

###### generate movie ##########
# animation function
def replay(t):
    f = int(t * 20)
    if f >= len(J):
        return J[len(J) - 1]
    else:
        return J[f]

print("Frames: ",len(J))

# setup the animation
fps = 20
animation = VideoClip(replay, duration=len(J)/fps + 1)
# write the video file
animation.write_videofile("bead_lin.webm",fps=fps,audio=False)
