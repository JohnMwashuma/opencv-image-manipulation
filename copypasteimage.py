import cv2

img = cv2.imread('assets/messi.png', -1)

# Copy part of the image
tag = img[100:300, 200:250] 
img[50:250, 150:200] = tag

#Notes: Put the same number of dimensions

cv2.imshow('Image', tag)
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()