import cv2 
	
image1 = cv2.imread('Photos/star.jpg')
image2 = cv2.imread('Photos/circle.jpg') 

sub = cv2.subtract(image1, image2) 

cv2.imshow('Image 1', image1) 
cv2.imshow('Image 2', image2) 
cv2.imshow('Subtracted Image', sub) 

cv2.waitKey(0)
cv2.destroyAllWindows() 
