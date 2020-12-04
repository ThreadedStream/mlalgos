from __future__ import unicode_literals
import cv2
import numpy as np

import os

LBP_CLASSIFIER_PATH = 'models/lbpcascade.xml'
HAAR_CLASSIFIER_PATH = 'models/haarcascade.xml'

trainee = ['John Carmack','Donald Knuth', 'Gamid FBI', 'Musa']

def draw_rectangle(image,rect):
    (x,y,w,h) = rect
    cv2.rectangle(image, (x,y), (x+w, y+h), (0,255,0), 2)

def draw_text(image, text, x, y):
    cv2.putText(image, text, (x,y), cv2.FONT_HERSHEY_TRIPLEX,4, (0, 255, 0), 3)

def detect_face(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier(LBP_CLASSIFIER_PATH)

    bboxes = face_cascade.detectMultiScale(gray)
    
    return gray, list(bboxes)

def prepare_training_data(folder):
    faces  = []
    labels = []
    training_folders = os.listdir(folder)

    for dir in training_folders:
        path = folder + '/' + dir
        images_raw = os.listdir(path)
        for image_raw in images_raw:
            label = int(image_raw[0])
            full_path = folder + '/' + dir + '/' + image_raw
            print(f"Loading {full_path}...")
            image = cv2.imread(full_path,cv2.IMREAD_UNCHANGED)
            grayscale, bboxes = detect_face(image)
            print(f'{bboxes} for {image_raw}')
            for bbox in bboxes:
                (x,y,w,h) = bbox
                face = grayscale[x:x+w,y:y+h]
                if face is not None:
                    faces.append(face)
                    labels.append(label)
                else:
                    print('it is none', face)

    cv2.destroyAllWindows()
    cv2.waitKey(1)

    return faces, labels

def train():
    model = cv2.face.LBPHFaceRecognizer_create(
        radius=1, neighbors=8,
        grid_x=8, grid_y=8
    )
    faces, labels = prepare_training_data('G:/mlnotebooks/facialrecoginition/training-data/')
    model.train(faces, np.array(labels))
    return model

def detect_faces(path_to_images):
    images = os.listdir(path_to_images)
    detected_faces = []
    for raw_image in images:
        full_path = path_to_images + '/' + raw_image
        image = cv2.imread(full_path)
        face,rect = detect_face(image)
        draw_rectangle(image, rect)
        detected_faces.append(image)
    
    return detected_faces


def predict(model, test_image):
    image = test_image.copy()
    
    face,rect = detect_face(image)

    label, conf=model.predict(face)
    print(label)
    text = trainee[label]

    draw_rectangle(image, rect)
    draw_text(image, text, rect[0], rect[1]-170)
    draw_text(image, str(conf), rect[0], rect[1]-60)
    return image

def main():
    print("Starting training process...")
    model = train()
    print("Training process is completed")
    test_image_raw = 'test-data/gamid_and_musa.jpg'
    test_image = cv2.imread(test_image_raw)
    bboxes = detect_face(test_image)
    for bbox in bboxes:
        draw_rectangle(test_image, bbox)
    image = predict(model, test_image)
    print('Doing some resizing beforehand...')
    height,width, channels = image.shape
    h = 720
    scale = height/h
    image = cv2.resize(image,(int(width/scale), int(height/scale)), interpolation=cv2.INTER_CUBIC)
    cv2.imshow('Predicted image', image)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()
    


main()
