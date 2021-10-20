import cv2
import numpy as np

print(cv2.__version__)

evt = 0
xVal = 0
yVal = 0 

def myCallBack(event, xPos, yPos, flags, params):
  global evt
  global xVal
  global yVal
  if event == cv2.EVENT_LBUTTONDOWN:
    evt = event
    xVal = xPos
    yVal = yPos
    print(event)

  if event == cv2.EVENT_RBUTTONUP:
    evt = event
    print(event)


width=640
height=360

cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

cv2.namedWindow('my WEBcam')
cv2.setMouseCallback('my WEBcam', myCallBack)

while True:
    ignore,  frame = cam.read()

    if evt == 1:
      x = np.zeros([250, 250, 3], dtype = np.uint8)
      clr = frame[yVal][xVal]
      print(clr)
      cv2.imshow('Color Picker', x)
      cv2.moveWindow('Color Picker', width, 0)

      # Se não tiver o zero vai repetir várias vezes 
      evt = 0

    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()