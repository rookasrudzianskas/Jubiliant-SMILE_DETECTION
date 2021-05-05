import cv2
from random import randint


face_detector = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

webcam = cv2.VideoCapture(0)

while True:
    successful_frame_rate, frame = webcam.read()

    if not successful_frame_rate:
        break

    frame_grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # faces = face_detector.detectMultiScale(frame_grayscale)

    faces = face_detector.detectMultiScale(frame_grayscale)

    print(faces)

    cv2.imshow("Why so serious?", frame_grayscale)

    cv2.waitKey(1)
#
webcam.release()
cv2.destroyAllWindows()




print("WHAT IS UP!!")
