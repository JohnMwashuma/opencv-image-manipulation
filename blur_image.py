import cv2 as cv

img = cv.imread('Photos/park.jpg')

cv.imshow('Original', img)

blur = cv.GaussianBlur(src=img, ksize=(7,7), sigmaX=cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

cv.waitKey(0)
