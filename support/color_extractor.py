import cv2
import numpy as np

cap = cv2.VideoCapture(0)
# img = cv2.imread('img/color_balls.jpg')


def nothing(x):
    pass


cv2.namedWindow('control')
cv2.createTrackbar('save', 'control', 0, 1, nothing)
cv2.createTrackbar('l-h', 'control', 0, 179, nothing)
cv2.createTrackbar('l-s', 'control', 0, 255, nothing)
cv2.createTrackbar('l-v', 'control', 0, 255, nothing)
cv2.createTrackbar('u-h', 'control', 179, 179, nothing)
cv2.createTrackbar('u-s', 'control', 255, 255, nothing)
cv2.createTrackbar('u-v', 'control', 255, 255, nothing)

while True:
    _, img = cap.read()
    height, width, chn = img.shape
    if width > 640:
        img = cv2.resize(img, (int(width / 2), int(height / 2)))
    else:
        pass

    img = cv2.GaussianBlur(img, (3, 3), 0)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    save = cv2.getTrackbarPos('save', 'control')
    lh = cv2.getTrackbarPos('l-h', 'control')
    ls = cv2.getTrackbarPos('l-s', 'control')
    lv = cv2.getTrackbarPos('l-v', 'control')
    uh = cv2.getTrackbarPos('u-h', 'control')
    us = cv2.getTrackbarPos('u-s', 'control')
    uv = cv2.getTrackbarPos('u-v', 'control')

    if save == 1:
        with open('backdoor/hsv.txt', 'w') as f:
            f.write(f'LowerHSV: {lh}:{ls}:{lv}\nUpperHSV: {uh}:{us}:{uv}')
            f.close()
            print('HSV Saved')
    else:
        pass

    lower_hsv = np.array([lh, ls, lv])
    upper_hsv = np.array([uh, us, uv])

    mask = cv2.inRange(hsv, lower_hsv, upper_hsv)
    extracted = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow('HSV Extractor', extracted)
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
