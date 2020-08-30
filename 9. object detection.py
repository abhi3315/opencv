import cv2
import numpy as np


def stackImages(imgArray, scale=1):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(
                        imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(
                        imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2:
                    imgArray[x][y] = cv2.cvtColor(
                        imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(
                    imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(
                    imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2:
                imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver


img = cv2.imread('Resources/shapes.png')
imgCopy = img.copy()
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
imgCanny = cv2.Canny(imgGray, 50, 50)

contours, hierarchy = cv2.findContours(
    imgCanny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
for cnt in contours:
    area = cv2.contourArea(cnt)
    print(area)
    if area > 500:
        cv2.drawContours(imgCopy, cnt, -1, (255, 0, 0), 3)
        peri = cv2.arcLength(cnt, True)
        print(peri)
        approx = cv2.approxPolyDP(cnt, peri*0.02, True)
        print(len(approx))
        x, y, w, h = cv2.boundingRect(approx)
        if len(approx) == 3:
            objectType = "Triangle"
        elif len(approx) == 4:
            aspRation = w/float(h)
            if aspRation > 0.95 and aspRation < 1.05:
                objectType = 'Square'
            else:
                objectType = "Reactangle"
        elif len(approx) > 4:
            objectType = "Circle"
        else:
            objectType = 'None'
        cv2.rectangle(imgCopy, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(imgCopy, objectType, (x+w//-10, y+h//2-10),
                    cv2.FONT_ITALIC, 0.5, (0, 0, 0), 2)

stack = stackImages(([img, imgGray], [imgCanny, imgCopy]), 0.5)

cv2.imshow('Output', stack)

cv2.waitKey(0)
