from cv2 import VideoCapture, imshow, namedWindow, imwrite, destroyWindow, waitKey
# or import *
# initialize the camera
ncams = 0
for i in range(3):
    try:
        cam = VideoCapture(i)
        if not cam.isOpened():
            print("Not open")
            break
    except:
        print("Except")
        break
    ncams += 1
    cam.release()

print("Cameras: ",ncams)
cn = 0 #ncams - 1
camfile = ("camGrab.png")
print("Using cam ",cn)
print("Press any key to take snapshot to ",camfile)

if ncams > 0:
    cam = VideoCapture(cn)   # 0,1 -> index of camera
    namedWindow("cam-test") #,CV_WINDOW_AUTOSIZE)
    while True:
        s, img = cam.read()
        if s:    # frame captured without any errors
#            namedWindow("cam-test") #,CV_WINDOW_AUTOSIZE)
            imshow("cam-test",img)
            
        # waitkey(0) stops until key presseed!
        k = waitKey(30)
        if k > 0 and k < 255:
            break

    destroyWindow("cam-test")
    imwrite(camfile,img) #save image
    cam.release()


    
