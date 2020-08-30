import cv2

faceCascade = cv2.CascadeClassifier("Resources/face_detection.xml")
img = cv2.imread('Resources/lena.png')
faces = faceCascade.detectMultiScale(img, 1.1, 4)
print(faces)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow('Result', img)

cv2.waitKey(0)
