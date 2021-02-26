import cv2 

image1 = cv2.imread('Photos/star.jpg')
image2 = cv2.imread('Photos/circle.jpg')

# cv2.bitwise_or is applied over the image inputs with applied parameters 
dest_or = cv2.bitwise_or(image2, image1, mask = None) 

cv2.imshow('Image 1', image1)
cv2.imshow('Image 2', image2)
cv2.imshow('Bitwise OR', dest_or) 

cv2.waitKey(0) 
cv2.destroyAllWindows()  
