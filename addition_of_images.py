import cv2 

image1 = cv2.imread('Photos/star.jpg') 
image2 = cv2.imread('Photos/circle.jpg') 

weightedSum = cv2.addWeighted(image1, 0.5, image2, 0.4, 0) 

cv2.imshow('Image 1', image1) 
cv2.imshow('Image 2', image2) 
cv2.imshow('Weighted Image', weightedSum) 


cv2.waitKey(0)
cv2.destroyAllWindows() 
