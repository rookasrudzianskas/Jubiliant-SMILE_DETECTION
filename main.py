import cv2

face_detector = cv2.CascadeClassifier('haarcascade_frontalcatface')

webcam = cv2.VideoCapture(0)

while True:
    successful_frame_rate, frame = webcam.read()

    if not successful_frame_rate:
        break
    cv2.imshow("Why so seriour", frame)

    cv2.waitKey(1)
#
webcam.release()
cv2.destroyAllWindows()


print("WHAT IS UP!!")
