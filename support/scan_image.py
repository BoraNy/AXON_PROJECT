import cv2
import numpy as np
from support import color, font


def scan_circles(_img):
    _gray = cv2.cvtColor(_img, cv2.COLOR_BGR2GRAY)
    _detected_circles = cv2.HoughCircles(
        _gray,
        cv2.HOUGH_GRADIENT,
        1,
        150,
        param1=50,
        param2=30,
        minRadius=1,
        maxRadius=40
    )

    if _detected_circles is not None:
        for _circle in _detected_circles:
            _circle_count = len(_circle)

        _detected_circles = np.uint16(np.around(_detected_circles))
        for _pt in _detected_circles[0, :]:
            _x, _y, _r = _pt[0], _pt[1], _pt[2]

    return _x, _y, _r, _circle_count


if __name__ == '__main__':

    cap = cv2.VideoCapture(0)

    while True:
        _, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray_blurred = cv2.blur(gray, (3, 3))

        detected_circles = cv2.HoughCircles(
            gray_blurred,
            cv2.HOUGH_GRADIENT,
            1,
            150,
            param1=50,
            param2=30,
            minRadius=1,
            maxRadius=40
        )

        if detected_circles is not None:
            for circle in detected_circles:
                cv2.putText(img, f'Detected Circle: {len(circle)}', (3, 25), font.hershey_simplex(), 1, color.yellow())

        if detected_circles is not None:
            detected_circles = np.uint16(np.around(detected_circles))
            for pt in detected_circles[0, :]:
                x, y, r = pt[0], pt[1], pt[2]
                cv2.circle(img, (x, y), r, color.green(), 2)
                cv2.circle(img, (x, y), 1, color.yellow(), 2)

        cv2.imshow('f1', img)
        if cv2.waitKey(1) == 27:
            break
    cap.release()
    cv2.destroyAllWindows()
