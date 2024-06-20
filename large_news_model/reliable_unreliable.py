import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.utils import Sequence
import numpy as np
import os

class SafeImageDataGenerator(Sequence):
    # Image data generator with error handling for corrupted images
    def __init__(self, generator):
        self.generator = generator
        self.on_epoch_end()

    def __len__(self):
        return len(self.generator)

    def __getitem__(self, idx):
        while True:
            try:
                batch = self.generator[idx]
                return batch
            except Exception as e:
                print(f"[WARNING] Skipping corrupted image in batch {idx}: {e}")
                idx = (idx + 1) % len(self.generator)

    def on_epoch_end(self):
        self.indexes = np.arange(len(self.generator))

# Define directories
train_dir = 'train/'
validation_dir = 'validate/'

# Data augmentation for training
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

# Validation data should only be rescaled
validation_datagen = ImageDataGenerator(rescale=1./255)

# Creating generators
train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(150, 150),
    batch_size=32,
    class_mode='binary'
)

validation_generator = validation_datagen.flow_from_directory(
    validation_dir,
    target_size=(150, 150),
    batch_size=32,
    class_mode='binary'
)

# Wrap generators with safe data generator
train_generator_safe = SafeImageDataGenerator(train_generator)
validation_generator_safe = SafeImageDataGenerator(validation_generator)

# Model architecture
model = keras.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)),
    layers.MaxPooling2D(2, 2),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D(2, 2),
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D(2, 2),
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D(2, 2),
    layers.Flatten(),
    layers.Dense(512, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])

# Model compilation
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Compute steps per epoch and validation steps
train_steps_per_epoch = train_generator.samples // train_generator.batch_size
validation_steps = validation_generator.samples // validation_generator.batch_size

# Define callbacks
callbacks = [
    keras.callbacks.ModelCheckpoint('best_model.keras', save_best_only=True),
    keras.callbacks.EarlyStopping(monitor='val_loss', patience=3),
    keras.callbacks.ReduceLROnPlateau(monitor='val_loss', factor=0.2, patience=5, min_lr=0.001),
    keras.callbacks.TensorBoard(log_dir='./logs')
]

# Model training
history = model.fit(
    train_generator_safe,
    steps_per_epoch=train_steps_per_epoch,
    epochs=10,
    validation_data=validation_generator_safe,
    validation_steps=validation_steps,
    callbacks=callbacks
)

# Save the final model
model.save('final_model.keras')

