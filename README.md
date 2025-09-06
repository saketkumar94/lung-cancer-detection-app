# Lung Cancer Detection App

This is a Streamlit web application that uses a convolutional neural network (CNN) to classify lung CT scan images as **Benign**, **Malignant**, or **Normal**. The app is built with TensorFlow and deployed on [Streamlit Community Cloud](https://streamlit.io/cloud) for public use.

**Live Demo**: [Try the app here](https://lung-cancer-detection-saket.streamlit.app) *(Update with your actual deployed URL)*

**Disclaimer**: This app is for educational and research purposes only. Consult a medical professional for actual diagnosis.

## Features
- Upload a lung CT scan image (`.jpg`, `.png`, or `.jpeg`).
- Receive a prediction with probabilities for Benign, Malignant, or Normal cases.
- Built with a TensorFlow CNN model trained on the [IQ-OTH/NCCD Lung Cancer Dataset](https://www.kaggle.com/datasets/khaledmostafaiq/iqothnccd-lung-cancer-dataset).
  
## Prerequisites
To run this app locally, ensure you have:
- Python 3.9 or higher
- Git and Git LFS installed
- A compatible GPU (optional, for faster model inference)

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/saketkumar94/lung-cancer-detection-app.git
   cd lung-cancer-detection-app
