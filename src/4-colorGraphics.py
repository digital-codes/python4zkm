import numpy as np
from matplotlib import pyplot as plt
import imageio
from skimage import color

# line drawing
def dl(x,y,len=0,dir=-1,col=128):
    for ll in range(len):
        I[x,y,0] = col[0]
        I[x,y,1] = col[1]
        I[x,y,2] = col[2]
        if dir == 0:
            x += 1
        elif dir == 1:
            y += 1
        elif dir == 2:
            x -= 1
        elif dir == 3:
            y -= 1
        else:
            print("invaid direction")
    return x,y
    
# recursive line drawing
def rdl(x,y,len=0,dir=-1,col=128):
    I[x,y,0] = col[0]
    I[x,y,1] = col[1]
    I[x,y,2] = col[2]
    if dir == 0:
        x += 1
    elif dir == 1:
        y += 1
    elif dir == 2:
        x -= 1
    elif dir == 3:
        y -= 1
    else:
        print("invaid direction")
    if len > 1:
        # recursive call
        return rdl(x,y,len,dir)
    return x,y

# image dimensions
N = 200
# empty image. needs additional dimentsion for RGB color
I = np.empty((N,N,3), dtype = np.uint8)

# background fill individual colors
I[:,:,0].fill(128)    # red
I[:,:,1].fill(128)    # green
I[:,:,2].fill(128)  # blue




# do some line drawing
x = N//2
y = x
I[x    ,y    ,2] = 255
I[x + 1,y + 1,2] = 255
I[x + 2,y + 2,2] = 255
I[x + 3,y + 3,2] = 255
I[x + 4,y + 4,2] = 255
I[x + 5,y + 5,2] = 255


# drawing with iterative function
x = N//2 - 50
y = x
l = 20
for i in range(10):
    x,y = dl(x,y,l,i%4,(255,0,0))
    l += 5

# drawing with recursive function
x = N//2 + 30
y = x
l = 20
for i in range(10):
    x,y = dl(x,y,l,i%4,(0,255,0))
    l += 5
    

# setting the climit is important!
plt.imshow(I,clim=(0,255))
plt.axis('off')
 
##while None == plt.waitforbuttonpress(.1):
##    plt.draw()

plt.show()

imageio.imwrite("imgrgb.jpg",I)

print("Colors can be defined differently\n\
RGB is based upon display physics, but it's hard to guess\n\
color from values. HSV is better in this repsect\n")

# use HSV colors, see https://en.wikipedia.org/wiki/HSL_and_HSV

# image dimensions
N = 256
# empty image. needs additional dimentsion for color
I = np.empty((N,N,3), dtype = np.uint8)

# generate HSV image
v = 200 # default V
for r in range(N):
    for c in range(N):
        I[r,c] = (r,c,v) 

# convert to RGB
I2 = color.hsv2rgb(I)        

# make a scaled RGB image with color resolution RGB:565
J = np.empty((N,N,3), dtype = np.uint8)
for g in range(2**6):
    for b in range(2**5):
        for r in range(2**5):
            i = g*2**10 + b*2**5 + r # pixel index
            J[i//256,i%256] = (r*2**3,g*2**2,b*2**3) # rescale colors

# create a figure
f = plt.figure()
p1 = f.add_subplot(121)
# setting the climit is important!
p1.imshow(J,clim=(0,255))
p1.axis('off')
p1.set_title("RGB Colors")

p2 = f.add_subplot(122)
# setting the climit is important!
p2.imshow(I2,clim=(0,255))
p2.axis('off')
p2.set_title("HSV Colors")
 
plt.show()



print("Done")
plt.close()




