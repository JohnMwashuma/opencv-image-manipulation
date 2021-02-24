import cv2 as cv

# Reading video
capture = cv.VideoCapture('Video/dog.mp4')

while True:
  isTrue, frame = capture.read()
  cv.imshow('Video', frame)

  # Break from the loop when the `d` key is pressed.
  if cv.waitKey(20) & 0xFF==ord('d'):
    break;

cap.release()
cv.destroyAllWindows()