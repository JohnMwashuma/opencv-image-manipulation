import cv2   
import os 

  
# read the image 
img = cv2.imread('Photos/cat.jpg')  
  
# New filename 
filename = 'new_name.jpg'
  
# Using cv2.imwrite() method to save the image 
cv2.imwrite(filename, img) 
 
