import numpy as np
from matplotlib import pyplot as plt
from skimage import color

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




