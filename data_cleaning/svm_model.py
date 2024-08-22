import pandas as pd
import os
from skimage.transform import resize
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import accuracy_score, classification_report
import imageio
import gc


def process_images_in_batches(data_dir, categories, batch_size=50):
    flat_data_arr = []
    target_arr = []

    for i in categories:
        print(f'loading... category: {i}')
        path = os.path.join(data_dir, i)
        images = [img for img in os.listdir(path) if img.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.gif'))]
        for batch_start in range(0, len(images), batch_size):
            batch_images = images[batch_start:batch_start + batch_size]
            for img in batch_images:
                try:
                    img_array = imageio.imread(os.path.join(path, img))
                    img_resized = resize(img_array, (150, 150, 3))
                    flat_data_arr.append(img_resized.flatten())
                    target_arr.append(categories.index(i))
                except Exception as e:
                    print(f"Could not load image {img}: {e}")
            gc.collect()
        print(f'loaded category: {i} successfully')

    flat_data = np.array(flat_data_arr)
    target = np.array(target_arr)
    return flat_data, target


# Step 2: Loading the images and converting them to a DataFrame
Categories = ['reliable', 'unreliable']
data_dir = 'final'

flat_data, target = process_images_in_batches(data_dir, Categories)

# Create a DataFrame
df = pd.DataFrame(flat_data)
df['Target'] = target
print(df.shape)  # Should print (number of images, number of features + 1)

# Step 3: Separate input features and targets
x = df.iloc[:, :-1]
y = df.iloc[:, -1]

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=77, stratify=y)

# Step 5: Model Construction
# Define a smaller parameter grid for GridSearchCV
param_grid = {'C': [0.1, 1], 'gamma': [0.0001, 0.001], 'kernel': ['rbf']}

# Create a support vector classifier
svc = svm.SVC(probability=True)

# Create a model using GridSearchCV with the parameters grid
model = GridSearchCV(svc, param_grid, verbose=3, n_jobs=-1)

# Model Training
model.fit(x_train, y_train)

# Step 6: Model Evaluation
# Testing the model using the testing data
y_pred = model.predict(x_test)

# Calculating the accuracy of the model
accuracy = accuracy_score(y_pred, y_test)

# Print the accuracy of the model
print(f"The model is {accuracy * 100}% accurate")

print(classification_report(y_test, y_pred, target_names=['reliable', 'unreliable']))

# Step 7: Prediction
path = '/Users/shreetikapoudel/Downloads/tst2.png.avif' #put a random image to test the model.
img = imageio.imread(path)
plt.imshow(img)
plt.show()
img_resize = resize(img, (150, 150, 3))
l = [img_resize.flatten()]
probability = model.predict_proba(l)
for ind, val in enumerate(Categories):
    print(f'{val} = {probability[0][ind] * 100}%')
print("The predicted image is: " + Categories[model.predict(l)[0]])

