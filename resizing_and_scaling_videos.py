import cv2 as cv

# Reading video
capture = cv.VideoCapture('Video/dog.mp4')

# Resizing and rescaling images. Used to reduce the amount of time it takes for
# an image to be processed. (reduce computational straighn)
# Rescaling an images means modifying it's height and width to a particular height and width.
# Changing your video files h & w to a smaller value than the origin video is always encouraged.

def rescale_frame(frame, scale=0.75):
  width = int(frame.shape[1] * scale)
  height = int(frame.shape[0] * scale)
  dimensions = (width,height)

  return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# Only works for live videos.
def changeRes(width, height):
  capture.set(3,width)
  capture.set(4,height)


while True:
  isTrue, frame = capture.read()

  frame_resized = rescale_frame(frame)

  cv.imshow('Video', frame)
  cv.imshow('Video Resized', frame_resized)

  # Break from the loop when the `d` key is pressed.
  if cv.waitKey(20) & 0xFF==ord('d'):
    break;

cap.release()
cv.destroyAllWindows()