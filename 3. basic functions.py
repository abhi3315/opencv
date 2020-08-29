import cv2
import numpy as np

kernel = np.ones((5, 5), np.uint8)
print(kernel)

img = cv2.imread('Resources/lena.png')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (9, 9), 2)
imgCanny = cv2.Canny(img, 100, 100)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)

cv2.imshow('Original', img)
cv2.imshow('Image Gray', imgGray)
cv2.imshow('Image Blur', imgBlur)
cv2.imshow('Image Canny', imgCanny)
cv2.imshow('Dialated Image', imgDialation)
cv2.imshow('Eroded Image', imgEroded)

cv2.waitKey(0)
