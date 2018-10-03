# basic image processing
import numpy as np
import matplotlib.pyplot as plt
import imageio
from moviepy.editor import VideoClip

# more features from scipy and skimage
# see http://www.scipy-lectures.org/advanced/image_processing/index.html#basic-image
from scipy import ndimage
from skimage import color, filters
from skimage.transform import rescale, resize, rotate, downscale_local_mean

# hashlib, just for demonstration
import hashlib

# lists
iml = []
lbl = []

# read img
imFile = "../data/punk.png"
#im = misc.imread(imFile)
im = imageio.imread(imFile)
lb = "Original"
iml.append(im)
lbl.append(lb)
print("shape: ",im.shape,", dtype: ",im.dtype)
#  save copy for video
imr = im.copy()

# grayscale
imgray = color.rgb2gray(im)
# result is float range 0..1
# convert to 0..255 int
imgray = np.dot(imgray,256).astype(np.uint8)
lb = "Gray"
iml.append(imgray)
lbl.append(lb)

imageio.imwrite('punk_g.png', imgray)
#imageio.imwrite('punk2_g.png', (256.0*imgray).astype(np.uint8))
print("shape: ",imgray.shape,", dtype: ",imgray.dtype)

################################
### encryption intermezzo ######
# convert the gray image into a 1D array
im1d = np.reshape(imgray,(1,imgray.shape[0]*imgray.shape[1]))
# get a hashing function
hg = hashlib.sha512()
# set the image as (must be bytes, we have this already)
hg.update(im1d)
# print the hex value
print("Hash of gray image: ", hg.hexdigest())
################################

# antialias not yet in skimage 0.13.1 ....
imm = rescale(imgray, 1.0 / 4.0, mode="reflect") # , anti_aliasing=False)
lb = "Resscale / 4"
iml.append(imm)
lbl.append(lb)
print("shape: ",imm.shape,", dtype: ",imm.dtype)

imm = resize(imgray, (imgray.shape[0] / 4, imgray.shape[1] / 4), mode="reflect") #, anti_aliasing=True)
lb = "Resize to size"
iml.append(imm)
lbl.append(lb)
print("shape: ",imm.shape,", dtype: ",imm.dtype)
print(lb)

imm = downscale_local_mean(imgray, (4, 3))
lb = "Downscale 4/3"
iml.append(imm)
lbl.append(lb)
print("shape: ",imm.shape,", dtype: ",imm.dtype)
print(lb)

imm = rotate(imgray, 90, resize=True, mode="reflect")
lb = "Rotate"
iml.append(imm)
lbl.append(lb)
print("shape: ",imm.shape,", dtype: ",imm.dtype)
print(lb)

imm = imgray > filters.threshold_li(imgray)
lb = "Threshold"
iml.append(imm)
lbl.append(lb)
print(lb)

imm = imgray.copy()
lb = "Contour"
iml.append(imm)
lbl.append(lb)
# we have to add the contour plot in this case later!
#ax[1,0].contour(imgray, [20,240])
print(lb)

imm = ndimage.gaussian_filter(imgray, sigma=5)
lb = "Gauss"
iml.append(imm)
lbl.append(lb)
print(lb)

#sobel. needs float value or unsigned byte. strange ...
sx = ndimage.sobel(imgray.astype(np.float32), axis=0, mode='constant')
sy = ndimage.sobel(imgray.astype(np.float32), axis=1, mode='constant')
imm = np.hypot(sx, sy)
lb = "Edges"
iml.append(imm)
lbl.append(lb)
print(lb)

#opening
imm = ndimage.binary_opening(imgray, structure=np.ones((3,3))).astype(np.int)
lb = "Opening"
iml.append(imm)
lbl.append(lb)
print(lb)

# distnace transform
imm = -ndimage.distance_transform_edt(imgray)
lb = "Distance"
iml.append(imm)
lbl.append(lb)
print(lb)

# show images

# images have different dimensions, don't use shared axes here
#f, ax = plt.subplots(nrows=2, ncols=3, sharex=True,sharey=True)
f, ax = plt.subplots(nrows=3, ncols=4)
i = 0
for a in ax:
    for aa in a:
        aa.axis("off")
        if i == 0:
            aa.imshow(iml[i])
        else:
            if i >= len(iml):
                continue
            #aa.imshow(iml[i], cmap=plt.cm.gray, clim=(0,1)) #(np.min(imgray),np.max(imgray)))
            aa.imshow(iml[i], cmap=plt.cm.gray, clim=(np.min(iml[i]),np.max(iml[i])))
            if "contour" in lbl[i].lower():
                aa.contour(iml[i], [100])

        aa.set_title(lbl[i])
        i += 1



plt.show()

# rotate function
def rot(t):
    global imr
    #imr = np.roll(imr,1,1)
    #return imr
    return np.roll(imr,int(t*20),1)


print("create video")

# setup the animation
fps = 20
animation = VideoClip(rot, duration=im.shape[0]/fps)
# write the video file
animation.write_videofile("punk.webm",fps=fps,audio=False)

