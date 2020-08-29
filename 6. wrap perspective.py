import cv2
import numpy as np

width = 250
height = 350
img = cv2.imread('Resources/cards.jpg')
pts1 = np.float32([[112, 220], [290, 190], [350, 440], [155, 480]])
pts2 = np.float32([[0, 0], [width, 0], [width, height], [0, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow('Original', img)
cv2.imshow('Output', imgOutput)

cv2.waitKey(0)
