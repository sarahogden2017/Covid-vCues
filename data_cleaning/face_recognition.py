import cv2
import os
import shutil

def process_images(input_folder, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            imagePath = os.path.join(input_folder, filename)
            img = cv2.imread(imagePath)

            if img is None:
                print(f"Error: Could not read the image {filename}.")
                continue

            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

            if face_classifier.empty():
                print("Error: Could not load Haar Cascade classifier.")
                return

            faces = face_classifier.detectMultiScale(
                gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40)
            )

            if len(faces) > 0:
                for (x, y, w, h) in faces:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 4)

                output_path = os.path.join(output_folder, filename)
                shutil.move(imagePath, output_path)
                print(f"Moved {filename} with detected faces to {output_folder}")

# Specify the input and output folders
input_folder = 'unreliable'
output_folder = 'unreliable_faces'

# Process the images
process_images(input_folder, output_folder)

