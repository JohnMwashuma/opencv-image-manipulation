import cv2

img = cv2.imread('Photos/cat.jpg',1)
blurred = cv2.GaussianBlur(img, (11, 11), 0)
cv2.imshow("Blurred", blurred)
cv2.waitKey(0)
