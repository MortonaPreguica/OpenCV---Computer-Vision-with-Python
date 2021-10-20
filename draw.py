import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)

# # 1. Paint the image a certain color
# blank[:] = 0, 255, 0
# cv.imshow('Green', blank)

# 2. Draw a rectangle
# cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness=2)
# cv.imshow('Rectangle', blank)

# 3. Draw a circle
# cv.circle(blank, (250, 250), 40, (0, 255, 0), thickness=3)
# cv.imshow('Circle', blank)

# Draw a line
# cv.line(blank, (0, 0), (250, 250), (0, 255, 0), thickness=2)
# cv.imshow('Line', blank)

# Write a text
cv.putText(blank, 'Hello', (225, 225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255, 243, 0), thickness=2)
cv.imshow('Text', blank)
cv.waitKey(0)
