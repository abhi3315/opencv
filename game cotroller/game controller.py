import cv2
import numpy as np
from input import *
import time

time.sleep(2)

A, S, D, W = 0x1E, 0x1F, 0x20, 0x11

blueLower = np.array([62, 142, 0])
blueUpper = np.array([123, 255, 255])

cap = cv2.VideoCapture(0)
current_key_pressed = set()

while True:

    key_pressed = False
    key_pressed_lr = False

    success, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (400, 300))
    width = frame.shape[1]
    height = frame.shape[0]

    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, blueLower, blueUpper)
    up_mask = mask[0:height//2, 0:width]
    down_mask = mask[height//2:height, width//4:3*width//4]
    cnt_up = cv2.findContours(
        up_mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnt_up = cnt_up[0]
    cnt_down = cv2.findContours(
        down_mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnt_down = cnt_down[0]

    if len(cnt_up) > 0:
        c = max(cnt_up, key=cv2.contourArea)  # max enclosing circle
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center_up = (int(M["m10"]/(M["m00"]+0.000001)),
                     int(M["m01"]/(M["m00"]+0.000001)))
        if radius > 30:
            cv2.circle(frame, center_up, 5, (0, 0, 255), -1)
            cv2.circle(frame, (int(x), int(y)),
                       int(radius), (0, 255, 0))

            if(center_up[0] < (width//2-40)):
                PressKey(A)
                current_key_pressed.add(A)
                key_pressed = True
                key_pressed_lr = True
            elif (center_up[0] > (width//2+40)):
                PressKey(D)
                current_key_pressed.add(D)
                key_pressed = True
                key_pressed_lr = True

    if len(cnt_down) > 0:
        c2 = max(cnt_down, key=cv2.contourArea)  # max enclosing circle
        ((x2, y2), radius2) = cv2.minEnclosingCircle(c2)
        M2 = cv2.moments(c2)
        center_down = (int(M2['m10']/(M2['m00']+0.000001)),
                       int(M2["m01"]/(M2["m00"]+0.000001)))
        center_down = (center_down[0]+width//4, center_down[1]+height//2)

        if radius2 > 30:
            cv2.circle(frame, (int(x2+width//4), int(y2+height//2)),
                       int(radius2), (0, 255, 255), 2)
            cv2.circle(frame, center_down, 5, (0, 0, 255), -1)
            if (height//2) < center_down[1] < (3*height//4) and (width//4) < center_down[0] < (3*width//4):
                PressKey(W)
                key_pressed = True
                current_key_pressed.add(W)
            elif center_down[1] > (3*height//4+10) and width//4 < center_down[0] < (3*width//4):
                PressKey(S)
                key_pressed = True
                current_key_pressed.add(S)

    cv2.rectangle(frame, (0, 0), (width//2-40, height//2), (255, 255, 255), 1)
    cv2.putText(frame, 'Left', (10, 30),
                cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255))
    cv2.rectangle(frame, (width//2+40, 0),
                  (width-2, height//2), (255, 255, 255), 1)
    cv2.putText(frame, 'Right', (300, 30),
                cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255))
    cv2.rectangle(frame, (width//4, (height//2+5)),
                  (3*width//4, 3*height//4), (255, 255, 255), 1)
    cv2.putText(frame, 'Up', (width//4, (height//2)+33),
                cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255))
    cv2.rectangle(frame, (width//4, (3*height//4)+5),
                  (3*width//4, height), (255, 255, 255), 1)
    cv2.putText(frame, 'Down', ((3*width//4)-100, height//2+108),
                cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255))

    cv2.imshow('Output', frame)

    if not key_pressed and len(current_key_pressed) != 0:
        for key in current_key_pressed:
            ReleaseKey(key)
            current_key_pressed = set()
    if not key_pressed_lr and (A in current_key_pressed) or (D in current_key_pressed):
        if A in current_key_pressed:
            ReleaseKey(A)
            current_key_pressed.remove(A)
        elif D in current_key_pressed:
            ReleaseKey(D)
            current_key_pressed.remove(D)

    if cv2.waitKey(1) == ord('q'):
        break
