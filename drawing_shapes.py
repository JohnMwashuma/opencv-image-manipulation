import cv2 

img = cv.imread('Photos/background.jpg')

#drawing a line
line_start_point = (0, 0) 
line_end_point = (250, 250) 
line_color = (0, 255, 0) 
line_thickness = 9
# Using cv2.line() method to draw the line using the initilized parameters
line = cv2.line(image, line_start_point, line_end_point, line_color, line_thickness) 

#drawing an arrow
arrow_start_point = (0, 0) 
arrow_end_point = (250, 250) 
arrow_color = (0, 255, 0) 
arrow_thickness = 9
# Using cv2.arrowedLine() method to draw the arrow using the initilized parameters
arrow = cv2.arrowedLine(image, arrow_start_point, arrow_end_point,arrow_color, arrow_thickness)

#drawing a circle
circle_center_coordinates = (120, 50)
circle_radius = 20
circle_color = (0, 255, 0)
circle_thickness = 2 
# Using cv2.circle() method to draw a circle with blue line borders of thickness of 2 px
circle = cv2.circle(image, circle_center_coordinates, circle_radius, circle_color, circle_thickness)

#drawing a rectangle
rectangle_start_point = (5, 5) 
rectangle_end_point = (220, 220)  
rectangle_color = (0, 255, 0) 
rectangle_thickness = 2
rectangle = cv2.rectangle(image, rectangle_start_point, rectangle_end_point, rectangle_color, rectangle_thickness) 

cv2.imshow('rectangle', rectangle)
cv2.imshow('circle', circle)
cv2.imshow('line', line) 
cv2.imshow('arrow', arrow) 

cv.waitKey(0)
cv2.destroyAllWindows()
