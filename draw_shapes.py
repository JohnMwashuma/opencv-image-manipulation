import cv2 as cv
import numpy as np

# Height, Width and number of colour channels
blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)

# # 1. Paint the image a certain color
blank[:] = 0,255,0
cv.imshow('Green', blank)

blank[200:300, 300:400] = 0,0,255 # colour specific range of pixels
cv.imshow('Red', blank)

# 2. Draw a Rectangle
cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=cv.FILLED)
cv.rectangle(
    blank,
    (0, 0),
    (blank.shape[1]//2, blank.shape[0]//2),
    (0, 255, 0),
    thickness=-1
)
cv.imshow('Rectangle', blank)

# # 3. Draw a circle
cv.circle(blank, (250,250), 40, (0,0,255), thickness=3)
cv.imshow('Circle', blank)

# # 3. Draw a line
cv.line(blank, (0, 0), (250, 250), (255, 255, 255), thickness=3)
cv.imshow('Line', blank)

# # 5. Write text
cv.putText(blank, 'Hello', (225, 225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), thickness=2)
cv.imshow('Text', blank)

cv.waitKey(0)
