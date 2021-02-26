import cv2 

image1 = cv2.imread('Photos/star.jpg')
image2 = cv2.imread('Photos/circle.jpg') 

# cv2.bitwise_not is applied over the image input with applied parameters 
dest_not1 = cv2.bitwise_not(image1, mask = None) 
dest_not2 = cv2.bitwise_not(image2, mask = None) 


cv2.imshow('Image 1', image1)
cv2.imshow('Image 2', image2)
cv2.imshow('Bitwise NOT on image 1', dest_not1) 
cv2.imshow('Bitwise NOT on image 2', dest_not2) 

cv2.waitKey(0) 
cv2.destroyAllWindows()
