import cv2
from random import randint


face_detector = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
smile_detector = cv2.CascadeClassifier('haarcascade_smile.xml')

webcam = cv2.VideoCapture(0)

while True:
    successful_frame_rate, frame = webcam.read()

    if not successful_frame_rate:
        break

    frame_grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # faces = face_detector.detectMultiScale(frame_grayscale)

    faces = face_detector.detectMultiScale(frame_grayscale)
    smiles = smile_detector.detectMultiScale(frame_grayscale)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (randint(0, 256), randint(0, 256), randint(0, 256)), 5)

    for (x, y, w, h) in smiles:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (randint(0, 256), randint(0, 256), randint(0, 256)), 5)

    print(faces)

    cv2.imshow("Why so serious?", frame)

    cv2.waitKey(1)
#
webcam.release()
cv2.destroyAllWindows()




print("WHAT IS UP!!")
