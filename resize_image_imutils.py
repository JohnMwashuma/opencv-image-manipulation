import imutils
import cv2

img = cv2.imread('Photos/cat.jpg',0)

#resized = cv2.resize(img, (200, 200))
#cv2.imshow("Fixed Resizing", resized)
#cv2.waitKey(0)
resized = imutils.resize(img, width=300)
cv2.imshow("Imutils Resize", resized)
cv2.waitKey(0)
