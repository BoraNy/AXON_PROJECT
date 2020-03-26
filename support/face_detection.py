import cv2
from support import color


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
