import numpy as np
from matplotlib import pyplot as plt
import imageio
import time

# line drawing
def dl(x,y,l=0,d=-1,col=128):
    for ll in range(l):
        I[x,y] = col
        if d == 0:
            x += 1
        elif d == 1:
            y += 1
        elif d == 2:
            x -= 1
        elif d == 3:
            y -= 1
        else:
            print("invaid direction")
    return x,y
    
# recursive line drawing
def rdl(x,y,l=0,d=-1,col=128):
    I[x,y] = col
    if d == 0:
        x += 1
    elif d == 1:
        y += 1
    elif d == 2:
        x -= 1
    elif d == 3:
        y -= 1
    else:
        print("invaid direction")

    if l > 1:
        # recursive call
        return rdl(x,y,l-1,d,col)
    return x,y

# image dimensions
N = 200
# empty image. will be black in grayscale color map
I = np.empty((N,N), dtype = np.uint8)

# fill with a medium color
I.fill(128)

# do some pixel (line) drawing
x = N//2
y = x
I[x    ,y    ] = 255
I[x + 1,y + 1] = 255
I[x + 2,y + 2] = 255
I[x + 3,y + 3] = 255
I[x + 4,y + 4] = 255
I[x + 5,y + 5] = 255


# drawing with iterative function
x = N//2 - 50
y = x
l = 20
for i in range(10):
    x,y = dl(x,y,l,i%4,0)
    l += 5

# drawing with recursive function
x = N//2 + 30
y = x
l = 20
for i in range(10):
    x,y = rdl(x,y,l,i%4,255)
    l += 5
    
    


# setting the climit is important!
plt.imshow(I, cmap="gray",clim=(0,255)) # magma)
plt.axis('off')
 
##while None == plt.waitforbuttonpress(.1):
##    plt.draw()

plt.show()

imageio.imwrite("imggray.jpg",I)

# rotate
for i in range(10):
    I = np.roll(I,5,1)
    plt.imshow(I, cmap="gray",clim=(0,255)) # magma)
    plt.draw()
    plt.waitforbuttonpress(.1)
    time.sleep(.5)
    

print("Done")
plt.close()




