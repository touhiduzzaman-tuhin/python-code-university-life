import cv2

#Create the casecade Classifier object

face_cascade = cv2.CascadeClassifier("F:\Final Project\Code\Cascade\haarcascade_frontalface_default.xml")

#Raeding the image as it is

img = cv2.imread("F:\Final Project\Train Images\Afridi\\1.jpg")

#Reading the image as gray scale image


gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Search the co-ordinates of the image

faces = face_cascade.detectMultiScale(img, scaleFactor=1.2, minNeighbors=2)

print(type(faces))

print(faces)

for x,y,w,h in faces:
    img = cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0),3)

cv2.imshow("Gray", img)

cv2.waitKey(0)

cv2.destroyAllWindows()