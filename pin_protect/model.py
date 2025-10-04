from flask import Flask, render_template, request
import cv2
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

app = Flask(__name__)

# Load model
model_url = "https://tfhub.dev/tensorflow/efficientdet/d4/1"
model = hub.load(model_url)

# Secret PIN (change this!)
SECRET_PIN = "1234"


def preprocess_image(image):
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_expanded = np.expand_dims(image_rgb, axis=0)
    input_tensor = tf.convert_to_tensor(image_expanded, dtype=tf.uint8)
    return input_tensor

# Count persons function (same as above)
def count_persons(image, min_confidence=0.3):
    input_tensor = preprocess_image(image)
    results = model(input_tensor)
    boxes = results['detection_boxes'].numpy()[0]
    classes = results['detection_classes'].numpy()[0].astype(int)
    scores = results['detection_scores'].numpy()[0]
    
    person_count = 0
    for i in range(len(scores)):
        if classes[i] == 1 and scores[i] >= min_confidence:
            person_count += 1
    
    return person_count

# Function to check camera
def check_camera():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        persons = count_persons(frame)
    else:
        persons = 0  # Error case
    cap.release()
    return persons

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_pin', methods=['POST'])
def check_pin():
    entered_pin = request.form['pin']
    persons = check_camera()
    
    if persons > 1:
        return "Access Denied: Multiple persons detected! Try alone."
    
    if entered_pin == SECRET_PIN:
        return "Unlocked! Welcome."
    else:
        return "Wrong PIN. Try again."

if __name__ == '__main__':
    app.run(debug=True)