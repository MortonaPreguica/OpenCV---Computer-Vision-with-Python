import cv2 as cv

def rescale(frame, scale=0.75):
  # Change images, videod and live videos
  width = int(frame.shape[1] * scale)
  height = int(frame.shape[0] * scale)

  dimension = (width, height)

  return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)

# Changing resolution
def changeRes(width, height):
  # Change live videos
  capture.set(3, width)
  capture.set(4, height)

capture = cv.VideoCapture('Resources/Videos/dog.mp4')

while True:
  isTrue, frame = capture.read()
  cv.imshow('Video', frame)

  if cv.waitKey(20) & 0xFF == ord('q'):
    break

capture.release()
cv.destroyAllWindows()