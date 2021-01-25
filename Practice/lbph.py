import numpy as np
import cv2
import os

database = ["Tom Cruise", "Clinton"]

def face_detection(image):
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    haar_classifier = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
    face = haar_classifier.detectMultiScale(image_gray, scaleFactor=1.3, minNeighbors=7)
    (x,y,w,h) = face[0]
    return image_gray[y:y+w, x:x+h], face[0]


def prepare_data(data_path):
    folders = os.listdir(data_path)
    labels = []
    faces = []
    for folder in folders:
        label = int(folder)
        training_images_path = data_path + '/' + folder
        for image in os.listdir(training_images_path):
            image_path = training_images_path + '/' + image
            training_image = cv2.imread(image_path)
            face, bounding_box = face_detection(training_image)
            faces.append(face)
            labels.append(label)

    print('Training Done')
    return faces, labels


faces = prepare_data('training')
labels = prepare_data('training')
print('Total faces = ', len(faces))
print('Total labels = ', len(labels))


model = cv2.face.createLBPHFaceRecognizer()
model.train(faces, np.array(labels))


def predict_image(test_image):
    img = test_image.copy()
    face, bounding_box = face_detection(img)
    label = model.predict(face)
    label_text = database[label-1]
    print (label)
    print (label_text)
    (x,y,w,h) = bounding_box
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
    cv2.putText(img, label_text, (x,y), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)
    return img



test1 = cv2.imread("F:\Final Project\Images\\ronaldo.jpg")
predict1 = predict_image(test1)
cv2.imshow('Face Recognition', predict1)
cv2.waitKey(0)
cv2.destroyAllWindows()