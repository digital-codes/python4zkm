import numpy as np
from matplotlib import pyplot as plt
import imageio
import time

# this is a function which draws a line, useing a foor loop
# line drawing
def dl(x,y,l=0,d=-1,col=128):
    """ Drawing a line with a for loop"""
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
    
# this is a function which draws a line in a recursive way
# recursive line drawing
def rdl(x,y,l=0,d=-1,col=128):
    """ Drawing a line with recursive calls to this very function"""
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

######################################
# We have defined the functions, now we create an empty
# image and fill it with some intermediate color

# image dimensions
N = 200
# empty image. will be black in grayscale color map
I = np.empty((N,N), dtype = np.uint8)

# fill with a medium color
I.fill(128)

# we set some pixels to 255, which gives a white pixel
# blalck pixels have the value 0
# do some pixel (line) drawing
x = N//2
y = x
I[x    ,y    ] = 255
I[x + 1,y + 1] = 255
I[x + 2,y + 2] = 255
I[x + 3,y + 3] = 255
I[x + 4,y + 4] = 255
I[x + 5,y + 5] = 255


# we use the first function to draw a pattern
# drawing with iterative function
x = N//2 - 50
y = x
l = 20
for i in range(10):
    x,y = dl(x,y,l,i%4,0)
    l += 5

# then we use the second function to draw a pattern
# drawing with recursive function
x = N//2 + 30
y = x
l = 20
for i in range(10):
    x,y = rdl(x,y,l,i%4,255)
    l += 5
    
    
# when we show the image, we have to set a color map
# also, setting the climit is important!
plt.imshow(I, cmap="gray",clim=(0,255)) # magma)
plt.axis('off')
plt.title("Simple Graphics") 

plt.show()

# we write the image to disk
imageio.imwrite("imggray.jpg",I)

# we create a shift animation of the image
plt.title("Animated Graphics") 
for i in range(10):
    I = np.roll(I,5,1)
    plt.imshow(I, cmap="gray",clim=(0,255)) # magma)
    plt.draw()
    plt.waitforbuttonpress(.1)
    time.sleep(.3)
    

print("Done")
plt.close()




