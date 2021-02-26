import cv2   
import os 
  

image_path = r'C:\Users\Rajnish\Desktop\GeeksforGeeks\geeks.png'

directory = r'C:\Users\Rajnish\Desktop\GeeksforGeeks'
  
# read the image 
img = cv2.imread(image_path)  
  
# New filename 
filename = 'new_name.jpg'
  
# Using cv2.imwrite() method to save the image 
cv2.imwrite(filename, img) 
 
