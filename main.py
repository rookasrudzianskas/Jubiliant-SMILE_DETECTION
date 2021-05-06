import cv2
from random import randint

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
smile_detector = cv2.CascadeClassifier('haarcascade_smile.xml')
eye_detector = cv2.CascadeClassifier('haarcascade_eye.xml')

webcam = cv2.VideoCapture(0)

while True:
    successful_frame_rate, frame = webcam.read()

    if not successful_frame_rate:
        break

    frame_grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # faces = face_detector.detectMultiScale(frame_grayscale)

    faces = face_detector.detectMultiScale(frame_grayscale)
    eyes = eye_detector.detectMultiScale(frame_grayscale)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (randint(0, 256), randint(0, 256), randint(0, 256)), 5)

        #  GEt the sub frame
        the_face = frame[y:y + h, x:x + w]

        face_grayscale = cv2.cvtColor(the_face, cv2.COLOR_BGR2GRAY)

        # it says how much to blur the image scale factor means and minNei... it must be 20 rectangles on one area to count as a smile
        smiles = smile_detector.detectMultiScale(face_grayscale, scaleFactor=1.7, minNeighbors=20)

        # find all smiles in the face
        if len(smiles) > 0:
            cv2.putText(frame, 'Rokas is smiling', (x, y + h + 40), fontScale=3, fontFace=cv2.FONT_HERSHEY_PLAIN,
                        color=(randint(0, 256), randint(0, 256), randint(0, 256)))

        eyes_detect = eye_detector.detectMultiScale(face_grayscale, scaleFactor=1.7, minNeighbors=30)

        for (X, Y, W, H) in eyes:

                cv2.rectangle(frame, (X, Y), (X + W, Y + H), (randint(0, 256), randint(0, 256), randint(0, 256)), 5)

        # for (x_, y_, w_, h_) in smiles:
        #     cv2.rectangle(the_face, (x_, y_), (x_ + w_, y_ + h_), (randint(0, 256), randint(0, 256), randint(0, 256)), 5)

    # for (x, y, w, h) in smiles:
    #     cv2.rectangle(frame, (x, y), (x + w, y + h), (randint(0, 256), randint(0, 256), randint(0, 256)), 5)

    # print(faces)

    cv2.imshow("Why so serious?", frame)

    cv2.waitKey(1)
#
webcam.release()
cv2.destroyAllWindows()

print("WHAT IS UP!!")
