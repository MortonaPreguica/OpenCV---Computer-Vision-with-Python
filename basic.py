import cv2 as cv

img = cv.imread('Resources/Photos/cat.jpg')

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade
canny = cv.Canny(img, 125, 175) # Passar a img borrada
cv.imshow('Bordas', canny)

# Dilating the image
dilated = cv.dilate(canny, (3, 3), iterations=1)
cv.imshow("Dilated", dilated)


# Eroding the image
eroding = cv.erode(dilated, (3, 3), iterations=1)
cv.imshow("Eroding", eroding)

# Resizing the image
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_LINEAR)
cv.imshow("Resized", resized)

# Cropping the image
cropping = img[50:200, 200:300]
cv.imshow("Cropping", cropping)

cv.waitKey(0)
