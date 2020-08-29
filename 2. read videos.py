import cv2

cap = cv2.VideoCapture(0)

while True:

    success, frame = cap.read()

    frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Gray", frameGray)

    cv2.imshow("Video", frame)

    if cv2.waitKey(1) == ord('q'):
        break
