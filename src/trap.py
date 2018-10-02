import cv2
import numpy

# using clean image or not
cleanImg = False #True

# source for the image is here:
# https://open-codes.zkm.de/sites/default/files/styles/catalog_full/public/artwork/342-autonomous-trap-001.jpg?itok=j-TjIGfc

if cleanImg:
    file = "../data/t3.jpg"
else:
    file = "../data/t1.jpg"
    
img0 = (cv2.imread(file,1)) # color mode
img1 = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY) # gray
if not cleanImg:
    img_filt = cv2.medianBlur(img1, 7) # median 3 with t3
    img_filt0 = img_filt.copy()
else:
    img_filt = img1.copy()

img_th = cv2.adaptiveThreshold(img_filt,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,4)
img_th0 = img_th.copy()
    
img_con, contours, hierarchy = cv2.findContours(img_th, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
#print("Contours:",len(contours))
#for i in range(len(contours)):
#    print("contour ",i,": ", len(contours[i])," segments")
img_con0 = img_con.copy()


img_con1 = cv2.cvtColor(img_con, cv2.COLOR_GRAY2RGB) # convert to rgb

if not cleanImg:
    # all contours
    img3 = cv2.drawContours(img_con1, contours, -1, (0,255,0), 1)
else:
    #specific contours
    img3 = cv2.drawContours(img_con1, contours, 33, (255,0,0), 2) # segment
    img3 = cv2.drawContours(img_con1, contours, 19, (0,0,255), 2) # segment

    img3 = cv2.drawContours(img_con1, contours, 71, (255,0,255), 2) # closed circle inner edge
    img3 = cv2.drawContours(img_con1, contours, 75, (255,255,0), 2) # closed circle outer edge



cv2.namedWindow("Img0", cv2.WINDOW_AUTOSIZE)
cv2.imshow("Img0", img0)
if not cleanImg:
    cv2.namedWindow("Img1", cv2.WINDOW_AUTOSIZE)
    cv2.imshow("Img1", img_filt0)
    cv2.namedWindow("Img2", cv2.WINDOW_AUTOSIZE)
    cv2.imshow("Img2", img_th0)
cv2.namedWindow("Img3", cv2.WINDOW_AUTOSIZE)
cv2.imshow("Img3", img_con0)
cv2.namedWindow("Img4", cv2.WINDOW_AUTOSIZE)
cv2.imshow("Img4", img3)

#linux needs cv loop
while True:

    ch = 0xFF & cv2.waitKey(1)
    if ch == 27:
        break
cv2.destroyAllWindows()

#im = cv2.imread('f.png')
#imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
#ret, thresh = cv2.threshold(imgray, 127, 255, 0)
#im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#To draw all the contours in an image:
#cv2.drawContours(im2, contours, -1, (0,255,0), 3)
#To draw an individual contour, say 4th contour:
#cv2.drawContours(im2, contours, 3, (0,255,0), 3)
#But most of the time, below method will be useful:
#cnt = contours[4]
#cv2.drawContours(im2, [cnt], 0, (0,255,0), 3)
