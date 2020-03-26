import cv2
import numpy as np
from support import font, color

cap = cv2.VideoCapture(0)

while True:
    _, img = cap.read()

    AOI0 = img[0:159, 0:212]
    AOI1 = img[0:159, 212:424]
    AOI2 = img[0:159, 424:636]

    AOI3 = img[159:318, 0:212]
    AOI4 = img[159:318, 212:424]
    AOI5 = img[159:318, 424:636]

    AOI6 = img[318:480, 0:212]
    AOI7 = img[318:480, 212:424]
    AOI8 = img[318:480, 424:636]

    cv2.line(img, (212, 0), (212, 480), color.white(), 1)
    cv2.line(img, (424, 0), (424, 480), color.white(), 1)
    cv2.line(img, (0, 159), (640, 159), color.white(), 1)
    cv2.line(img, (0, 318), (640, 318), color.white(), 1)

    cv2.imshow('MAIN', img)
    # cv2.imshow('AOI0', AOI0)
    # cv2.imshow('AOI1', AOI1)
    # cv2.imshow('AOI2', AOI2)
    # cv2.imshow('AOI3', AOI3)
    # cv2.imshow('AOI4', AOI4)
    # cv2.imshow('AOI5', AOI5)
    # cv2.imshow('AOI6', AOI6)
    # cv2.imshow('AOI7', AOI7)
    # cv2.imshow('AOI8', AOI8)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
