import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np

# Define class names (must match lung_cancer_cnn.py)
classes = ['Bengin cases', 'Malignant cases', 'Normal cases']

# Load the trained model
model_path = r'C:\Users\lenovo\OneDrive\Desktop\CSS\best_model.keras'  # Absolute path
model = tf.keras.models.load_model(model_path)

# Define inference function
def predict_image(img_path):
    img = image.load_img(img_path, target_size=(128, 128), color_mode='rgb')  # Use 'grayscale' if needed
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    pred = model.predict(img_array)
    class_idx = np.argmax(pred, axis=1)[0]
    return classes[class_idx]

# Streamlit app
st.title("Lung Cancer Detection")
uploaded_file = st.file_uploader("Upload a CT scan image", type=['jpg', 'png', 'jpeg'])
if uploaded_file:
    with open("temp_image.jpg", "wb") as f:
        f.write(uploaded_file.getbuffer())
    prediction = predict_image("temp_image.jpg")
    st.write(f"Prediction: {prediction}")