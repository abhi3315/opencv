import cv2
print("Open CV imported!")

img = cv2.imread('Resources/lena.png')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Output", img)
cv2.imshow("Gray", imgGray)

cv2.waitKey(0)
