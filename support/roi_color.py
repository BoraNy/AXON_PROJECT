import cv2
import numpy as np

img = cv2.imread('img/desktop.png')

roi = img[100:150, 10:60]

b, g, r = cv2.split(roi)

print(np.sum(r))
print(np.sum(g))
print(np.sum(b))

cv2.rectangle(img, (10, 100), (60, 150), (0, 255, 0), 1)
cv2.imshow('color', img)
cv2.imshow('roi', roi)

cv2.waitKey(0)
cv2.destroyAllWindows()
