# intruder-looker
This will be an leveled up "LOCK". The upgradation will be that, it will check for any other person (intruder) , if present in the camera frame and will not unlock if it so

**Overview**
This is a simple web application that enhances PIN-based security by using deep learning to detect if someone is trying to spy on your PIN entry (like "shoulder surfing"). It uses your webcam to check if more than one person is in the frame. If it detects multiple people, it won't unlock even if the PIN is correct. This project is great for beginners in machine learning (ML) and deep learning (DL) to learn about computer vision, object detection, and web integration.
The core uses TensorFlow for person detection with a pre-trained model (EfficientDet). The web app is built with Flask.
Features

PIN Entry: A basic web form to enter your PIN.
Person Detection: Uses DL to count people in the webcam view.
Security Check: Only unlocks if PIN is correct and only one person is detected.
Live Testing: Scripts to test detection on images or webcam before integrating.

# Prerequisites

Python 3 (version 3.8 or higher recommended).
A webcam on your computer.
Basic libraries: Install them using pip (run in your terminal):
textpip install tensorflow tensorflow-hub opencv-python flask numpy


# Installation

Create a new folder for the project, e.g., pin-security-app.
Inside the folder, create these files:

app.py: The main web app code.
detector.py: For testing the DL model (optional, but helpful).
A subfolder called templates with index.html inside it.


Copy the code from the instructions below into these files.
Open a terminal in the project folder and install the prerequisites (as above).

# How to Run
Step 1: Test the Detector (Optional but Recommended)

Run python detector.py to test person detection.
It will open your webcam and print/count people live. Press 'q' to quit.
This helps you verify the DL part works before the full app.

Step 2: Run the Web App

Run python app.py in your terminal.
Open a web browser and go to http://127.0.0.1:5000/.
Enter your PIN (default is "1234"—change it in app.py).
The app will check your webcam on submit:
  If alone and PIN correct: Unlocks.
  If multiple people: Denies access.
  If wrong PIN: Says so.


# How It Works

DL Model: EfficientDet (pre-trained) detects "persons" in images/frames. It uses neural networks to find and count people.
Webcam Integration: On PIN submit, grabs a frame, counts people.
Security Logic: If >1 person, block. Else, check PIN.
Customization: Change min_confidence for better accuracy, or swap models for speed.

# Troubleshooting

Camera Issues: Ensure no other apps use the webcam. Try camera ID 1 if 0 fails.
Slow Performance: Use a lighter model like EfficientDet D0 (change URL to https://tfhub.dev/tensorflow/efficientdet/d0/1).
Errors: Check terminal for messages. Common: Missing libraries—reinstall them.

# Learning Tips

Experiment: Add features like saving detection images.
Resources: TensorFlow docs (tensorflow.org/tutorials), Flask quickstart.
This is a starting point—build on it to learn more DL!

# Visuals of working :
<img width="744" height="429" alt="Screenshot 2025-10-04 232018" src="https://github.com/user-attachments/assets/2eaa39bd-cdc8-410c-86d0-8941a0a41905" />

<img width="796" height="248" alt="Screenshot 2025-10-04 232920" src="https://github.com/user-attachments/assets/5828daa6-440d-4c26-b4cb-6bb32580654b" />

<img width="641" height="156" alt="Screenshot 2025-10-04 232801" src="https://github.com/user-attachments/assets/7fd4be69-cb79-4336-9ae2-6c9391d490fb" />
