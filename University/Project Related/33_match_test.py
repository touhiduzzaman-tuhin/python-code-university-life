import cv2

face_cascade = cv2.CascadeClassifier("F:\Final Project\Code\Cascade\haarcascade_frontalface_default.xml")


img1 = cv2.imread("F:\Final Project\Images\\group.jpg")

img = cv2.resize(img1, (1200, 800))

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


faces = face_cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=3)

print(type(faces))

print(faces)

print(faces.shape)

print("Number of faces detected: " + str(faces.shape[0]))

for x,y,w,h in faces:
    img = cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0),2)

cv2.imshow("Gray", img)

cv2.waitKey(0)

cv2.destroyAllWindows()