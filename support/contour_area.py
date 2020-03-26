import cv2
import numpy as np
from support import color

cap = cv2.VideoCapture(0)

while True:
    _, img = cap.read()

    noise_reduced = cv2.GaussianBlur(img, (5, 5), 0)
    hsv = cv2.cvtColor(noise_reduced, cv2.COLOR_BGR2HSV)

    lower_yellow = np.array([0, 215, 110])
    upper_yellow = np.array([74, 255, 255])

    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    _, contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 5000:
            cv2.drawContours(img, contour, -1, color.white(), 3)

    cv2.imshow('output', img)
    cv2.imshow('hsv', mask)
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
