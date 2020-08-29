import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
print(img.shape)

cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 0, 255), 3)
cv2.rectangle(img, (0, 0), (250, 350), (0, 255, 0), 2)
cv2.circle(img, (400, 50), 30, (255, 255, 0), -1)
cv2.putText(img, "OPENCV", (300, 200),
            cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 2)

cv2.imshow('Output', img)

cv2.waitKey(0)
