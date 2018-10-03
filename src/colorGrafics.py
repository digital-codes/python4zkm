import numpy as np
from matplotlib import pyplot as plt
import imageio

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

print("Done")
plt.close()




