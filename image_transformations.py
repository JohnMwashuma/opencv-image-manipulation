import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpg')

cv.imshow('Original Image', img)


def translate(img, x, y):
    """
    Shifts an image a long the x and y axis.

    :param img: Image to translate.
    :param x: Number of pixels to shift along the x-axis.
    :param y: Number of pixels to shift along the y-axis.

    returns: The translated image.
    """
    transMat = np.float32([[1,0,x],[0,1,y]])
    (height, width) = img.shape[:2]
    dimensions = (width, height)
    return cv.warpAffine(img, transMat, dimensions)

# -x --> Left shift
# -y --> Up shift
# x --> Right shift
# y --> Down shift

translated = translate(img, 100, 100) # Shift the image right by 100 pixels and down by 100 pixels.
cv.imshow('Translated', translated)

# Rotation
def rotate(img, angle, rotPoint=None):
    """
    Rotate the image by some angle.

    :param img: Image to rotate.
    :param angle: Angle to rotate around.
    :param rotPoint: Rotation point.

    returns: The rotated image.
    """
    (height, width) = img.shape[:2]

    # Rotate the image around the center if rotPoint is None
    if rotPoint is None:
      rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)


# Rotate img 45 degrees clockwise. For unti-clockwise use -45 instead
rotated = rotate(img, 45)
cv.imshow('Rotated Image', rotated)


# Flipping: 0 for vertical flip and 1 for horizontal flip.
flip = cv.flip(img, 0)
cv.imshow('Flipped img', flip)

cv.waitKey(0)
