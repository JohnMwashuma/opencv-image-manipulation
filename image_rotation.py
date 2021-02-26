import cv2

#put image in the same directory as python file or use a path

#1. LOADING/READING AN IMAGE
img = cv2.imread ('assets/ku.jpg',0) #you can load jpeg, png
path = r"D:\Msc\Sem 2\CCI 509 - Image and Vision Systems\pics\flower.jpg"
img2 = cv2.imread(path, -1) 

#3. ROTATING AN IMAGE
img3 = cv2.rotate (img,cv2.ROTATE_90_CLOCKWISE) #ROTATE_180, ROTATE_90_COUNTERCLOCKWISE, ROTATE_90_CLOCKWISE

cv2.imshow('Kenyatta University', img)
cv2.imshow ('Red Flowers',img2)
cv2.imshow('Rotated_KU', img3)

cv2.waitKey (0)
cv2.destroyAllWindows ()