import numpy as np 
import cv2 
  
# creating object 
f1 = cv2.bgsegm.createBackgroundSubtractorMOG()
f2 = cv2.createBackgroundSubtractorMOG2()
f3 = cv2.bgsegm.createBackgroundSubtractorGMG()
  
# capture frames from a camera  
cap = cv2.VideoCapture(0)
while(1): 
    # read frames 
    ret, img = cap.read() 
      
    # apply mask for background subtraction 
    mask1 = f1.apply(img)
    mask2 = f2.apply(img)
    mask3 = f3.apply(img)
    #showing original clips
    cv2.imshow('Original', img)
    #defining frames
    def MOG():
        cv2.imshow('MOG', mask1)
    def MOG2():
        cv2.imshow('MOG2', mask2)
    def GMG():
        cv2.imshow('GMG', mask3)
    #change this to others
    MOG()
       
    #running the clips
    key = cv2.waitKey(30) & 0xff 
    if key == 27: 
        break
  
cap.release()
cv2.destroyAllWindows()
