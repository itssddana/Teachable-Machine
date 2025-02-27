# -*- coding: utf-8 -*-
"""Teachable_Machine_code.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1R__5yWsiBRx8_QvqObUktnk_m18BgVXo
"""

# Install necessary libraries if not already installed
!pip install tensorflow pillow numpy

import tensorflow as tf
import numpy as np
from PIL import Image
import os

# Upload files
from google.colab import files

print("Upload the model file (.h5):")
model_file = files.upload()  # Upload model file
model_path = list(model_file.keys())[0]

print("Upload the labels file (labels.txt):")
labels_file = files.upload()  # Upload labels file
labels_path = list(labels_file.keys())[0]

print("Upload the image file (.jpg):")
image_file = files.upload()  # Upload image file
image_path = list(image_file.keys())[0]

# Load the model
try:
    model = tf.keras.models.load_model(model_path)
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")

# Load labels
try:
    with open(labels_path, "r") as file:
        labels = [line.strip() for line in file.readlines()]
    if len(labels) != 2 or labels != ["Robot" , "Human"]:
        print("Error: Labels file must contain exactly 'Human' and 'Robot' in separate lines.")
        labels = None
    else:
        print("Labels loaded successfully!")
except Exception as e:
    print(f"Error loading labels: {e}")

# Predict the image
if labels:
    try:
        image = Image.open(image_path).convert("RGB")
        image = image.resize((224, 224))  # Resize to match model input size
        image_array = np.array(image) / 255.0  # Normalize
        image_array = np.expand_dims(image_array, axis=0)  # Add batch dimension

        # Predict
        predictions = model.predict(image_array)
        class_index = np.argmax(predictions[0])  # Get the class index
        confidence = predictions[0][class_index]  # Confidence score

        print(f"\nPredicted Class: {labels[class_index]}")
        print(f"Confidence: {confidence:.2%}")
    except Exception as e:
        print(f"Error processing image: {e}")