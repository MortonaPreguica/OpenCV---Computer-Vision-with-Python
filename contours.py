import cv2 as cv


img = cv.imread('Resources/Photos/Boston.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray cats',gray)

canny = cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)


# Contours é uma pyhton list com a coordenadas do pontos
contours,  hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

cv.drawContours(blank, canny, -1, (0, 0, 255), thickness=2)
cv.imshow('Dale', blank)

# Usar canny para achar os ponteiros