import cv2

face_detector = cv2.CascadeClassifier('haarcascade_frontalcatface')

webcam = cv2.VideoCapture(0)

successful_frame_rate, frame = webcam.read()

cv2.imshow("Why so seriour", frame)

cv2.waitKey()

# while True:
#
#

# webcam.release()
# cv2.destroyAllWubdiws()





print("WHAT IS UP!!")