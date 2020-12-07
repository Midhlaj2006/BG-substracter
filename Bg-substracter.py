import numpy as np 
import cv2 
  
# creating object 
f1 = cv2.bgsegm.createBackgroundSubtractorMOG()
f2 = cv2.createBackgroundSubtractorMOG2()
f3 = cv2.bgsegm.createBackgroundSubtractorGMG()
  
# capture frames from a camera  
cap = cv2.VideoCapture(0)
# asking which frame you wants
inp =int(input("choose the number of the frame you want (one at at time/all of them):\n0-all\n1-MOG\n2-MOG2\n3-GMG\n"))
while True: 
    # read frames 
    ret, img = cap.read() 
      
    # apply mask for background subtraction 
    mask1 = f1.apply(img)
    mask2 = f2.apply(img)
    mask3 = f3.apply(img)
    #defining frames
    def MOG():
        cv2.imshow('MOG', mask1)
    def MOG2():
        cv2.imshow('MOG2', mask2)
    def GMG():
        cv2.imshow('GMG', mask3)
    #choosing the frame
    if inp==0:
        MOG()
        MOG2()
        GMG()
    elif inp==1:
        MOG()
    elif inp==2:
        MOG2()
    elif inp==3:
        GMG()
    else:
        print(f'Sorry {inp} is not found \nonly showing you your camera feed')
    #show original video
    cv2.imshow('Original', img)
    #running the clips
    key = cv2.waitKey(30) & 0xff 
    if key == 27: 
        break
  
cap.release()
cv2.destroyAllWindows()
