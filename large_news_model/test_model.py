from tensorflow.keras.models import load_model
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Load the model
model = load_model('final_model.keras')

# Summarize the model
model.summary()

# Get the target size from the model's input shape
input_shape = model.input_shape[1:3]
img_height, img_width = input_shape

# Define the test image URLs
test_image_urls = [
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTmlLeaXuRVwKJ0rvs4WMv5W01pvkxkKt-mFg&s",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSNFOR86h9xry2ZGluSfKGgjq5LPR_IR5lKbg&s",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQDIqaDFYS4RLsnbCNrZ36cTjSFHS1HuoXwlA&s"
]

# Define class names
class_names = ['reliable', 'unreliable']

def preprocess_image(image_path):
    img = tf.keras.utils.load_img(image_path, target_size=(img_height, img_width))
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  # Create a batch
    img_array /= 255.0  # Normalize the image array
    return img_array

for test_image_url in test_image_urls:
    test_image_path = tf.keras.utils.get_file('test_image', origin=test_image_url)

    # Preprocess the image
    img_array = preprocess_image(test_image_path)

    # Make predictions
    predictions = model.predict(img_array)
    predicted_prob = predictions[0][0]

    # Determine the predicted class
    predicted_class = class_names[0] if predicted_prob >= 0.5 else class_names[1]
    confidence = predicted_prob if predicted_prob >= 0.5 else 1 - predicted_prob

    # Print the result
    print(
        "This image most likely belongs to '{}' with a {:.2f} percent confidence."
        .format(predicted_class, 100 * confidence)
    )

    # Display the image and prediction result
    img = tf.keras.utils.load_img(test_image_path, target_size=(img_height, img_width))
    plt.imshow(img)
    plt.title(f"Predicted: {predicted_class}, Confidence: {100 * confidence:.2f}%")
    plt.axis('off')
    plt.show()

    # Check the raw prediction output
    print("Raw predictions:", predictions)

