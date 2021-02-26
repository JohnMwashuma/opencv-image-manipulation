import cv2 
	
# path to input images are specified and 
# images are loaded with imread command 
image1 = cv2.imread('Photos/star.jpg')
image2 = cv2.imread('Photos/circle.jpg')

# cv2.bitwise_and is applied over the image inputs with applied parameters 
dest_and = cv2.bitwise_and(image2, image1, mask = None) 

cv2.imshow('Image 1', image1)
cv2.imshow('Image 2', image2)
cv2.imshow('Bitwise And', dest_and) 


cv2.waitKey(0) 
cv2.destroyAllWindows() 