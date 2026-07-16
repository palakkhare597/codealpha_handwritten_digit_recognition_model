import streamlit as st
import numpy as np
import cv2
from tensorflow.keras.models import load_model

# Page configuration
st.set_page_config(
    page_title="Handwritten Digit Recognition",
    page_icon="✍️",
    layout="centered"
)

st.title("✍️ Handwritten Digit Recognition")
st.write("Upload a handwritten digit image (0-9) and predict the digit.")

# Load trained model
model = load_model("handwritten_digit_recognition_model.keras")

uploaded_file = st.file_uploader(
    "Choose an image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:

    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_GRAYSCALE)

    st.image(img, caption="Uploaded Image", width=250)

    # Resize to 28x28
    img = cv2.resize(img, (28, 28))

    # Invert if background is white
    if np.mean(img) > 127:
        img = 255 - img

    # Normalize
    img = img.astype("float32") / 255.0

    # Reshape for CNN
    img = img.reshape(1, 28, 28, 1)

    prediction = model.predict(img)

    digit = np.argmax(prediction)
    confidence = np.max(prediction) * 100

    st.success(f"Predicted Digit: **{digit}**")
    st.info(f"Confidence: **{confidence:.2f}%**")

    st.subheader("Prediction Probabilities")

    for i in range(10):
        st.progress(float(prediction[0][i]))
        st.write(f"{i}: {prediction[0][i]*100:.2f}%")