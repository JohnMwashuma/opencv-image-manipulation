  
import numpy as np
import cv2

cap = cv2.VideoCapture(0) #No of webcam. 0 access 1 camera; 1 access 2 cameras

while True:
    ret, frame = cap.read() #Captures the image and stores in an array. Camera won't be used if another App is using it. ret returns false if there's an issue
    cv2.imshow('CLIFF', frame)

    if cv2.waitKey(1) == ord('c'): #Listens for Keyboard "c" for 1 miliseconds
        break

cap.release()
cv2.destroyAllWindows()