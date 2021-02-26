import cv2 as cv

# Reading image
img = cv.imread('Photos/cat.jpg')

cv.imshow('Cat', img)

# Keyboard binding function, waits for an infinite amount of time for the keyboad to be pressed
cv.waitKey(0)

# removing/deleting created GUI window from screen and memory
cv2.destroyAllWindows()
