import cv2
import numpy as np
import tkinter as tk
from tkinter import *
from support import font, color


def color_extractor(camera_id=0):
    cap = cv2.VideoCapture(camera_id)

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


def circle_detection(camera_id=0):
    def nothing(x):
        pass

    cap = cv2.VideoCapture(camera_id)
    blur_val = 3
    while True:
        _, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray_blurred = cv2.GaussianBlur(gray, (blur_val, blur_val), 0)

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


def gui_control():
    def get_all_value():
        label.config(text=f'x = {x_coordinate.get()}, y = {y_coordinate.get()}, camera = {select_camera.get()}')

    root = Tk()
    root.title('Control Panel')
    root.geometry('320x240')
    root.resizable(width=False, height=False)

    select_camera = IntVar()

    x_label = Label(root, text='X-Axis')
    x_label.grid(row=0, column=0)
    x_coordinate = tk.Scale(root, length=150, from_=0, to=180, resolution=1, orient=HORIZONTAL)
    x_coordinate.grid(row=0, column=1)

    y_label = Label(root, text='Y-Axis')
    y_label.grid(row=1, column=0)
    y_coordinate = tk.Scale(root, length=150, from_=0, to=180, resolution=1, orient=HORIZONTAL)
    y_coordinate.grid(row=1, column=1)

    internal_camera = tk.Radiobutton(root, text='Built-in Camera', variable=select_camera, value=0)
    internal_camera.grid(row=2, column=0)
    external_camera = tk.Radiobutton(root, text='External Camera', variable=select_camera, value=1)
    external_camera.grid(row=2, column=1)

    get_val = Button(root, text='Get', command=get_all_value)
    get_val.place(x=265, y=200)

    label = Label(root, text='x = 0, y = 0, camera = 0')
    label.place(x=5, y=210)

    root.mainloop()


def face_detection():
    face_cascade = cv2.CascadeClassifier(
        'haarcascade/haarcascade_frontalface_default.xml'
    )
    cap = cv2.VideoCapture(0)

    while True:
        _, img = cap.read()
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        blurred_gray = cv2.GaussianBlur(
            gray_img,
            (3, 3),
            0
        )

        faces = face_cascade.detectMultiScale(
            blurred_gray,
            1.3,
            5
        )

        for (x, y, w, h) in faces:
            img = cv2.rectangle(
                img,
                (x, y),
                (x + w, y + h),
                color.green(),
                2
            )
            if x > 0 and y > 0:
                roi_color = img[y:y + h, x:x + w]
            else:
                roi_color = img[215:265, 295:345]

        cv2.imshow('Detection', img)
        cv2.imshow('ROI', roi_color)

        if cv2.waitKey(1) == 27:
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    face_detection()
