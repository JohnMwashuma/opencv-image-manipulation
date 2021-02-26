import cv2 as cv

# Reading image
img = cv.imread('Photos/cat.jpg')

#reading the image in grayscale
img2 = cv.imread('Photos/cat.jpg', 0)

cv.imshow('Cat', img)
cv.imshow('Grayscale Cat', img2)

# Keyboard binding function, waits for an infinite amount of time for the keyboad to be pressed
cv.waitKey(0)

# removing/deleting created GUI window from screen and memory
cv2.destroyAllWindows()
