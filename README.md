# ✍️ Handwritten Digit Recognition using CNN

A deep learning project that recognizes handwritten digits (0–9) using a Convolutional Neural Network (CNN). The model is trained on the MNIST/EMNIST dataset and deployed with a Streamlit web application.

---

## 📌 Project Overview

This project uses a CNN to classify handwritten digit images into one of the ten classes (0–9). Users can upload an image through a simple Streamlit interface and receive the predicted digit along with the prediction confidence.

---

## 🚀 Features

- Handwritten digit recognition (0–9)
- CNN-based deep learning model
- Image preprocessing (grayscale, resize, normalization)
- Streamlit interactive web application
- Displays prediction confidence
- Clean and user-friendly interface

---

## 🛠️ Technologies Used

- Python
- TensorFlow / Keras
- NumPy
- OpenCV
- Streamlit
- Matplotlib

---

## 📂 Project Structure

```
Handwritten_Digit_Recognition/
│
├── app.py
├── train_model.ipynb
├── handwritten_digit_recognition_model.keras
├── requirements.txt
├── README.md
└── sample_images/
```

---

## 📊 Dataset

This project uses the **MNIST**  handwritten digit dataset.

Dataset contains:

- Training Images: 60,000
- Testing Images: 10,000
- Image Size: 28 × 28 pixels
- Classes: 10 (Digits 0–9)

---

## 🧠 Model Architecture

The CNN model consists of:

- Conv2D Layer
- MaxPooling2D
- Conv2D Layer
- MaxPooling2D
- Flatten Layer
- Dense Layer (ReLU)
- Dropout Layer
- Output Layer (Softmax)

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/palakkhare597/codealpha_handwritten_digit_recognition_model/tree/main
```

```bash
cd Handwritten_Digit_Recognition
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

##  Application Workflow

1. Open the Streamlit application.
2. Upload a handwritten digit image.
3. Image is automatically preprocessed.
4. CNN predicts the digit.
5. Prediction and confidence score are displayed.

---

## 📈 Model Performance

| Metric | Value |
|---------|--------|
| Accuracy | 99%+ |
| Loss | Very Low |
| Optimizer | Adam |
| Loss Function | Sparse Categorical Crossentropy |

*(Performance may vary depending on training parameters.)*

---

## 📌 Future Improvements

- Draw digit directly on canvas
- Support EMNIST letters
- Mobile-friendly UI
- Deploy on Streamlit Cloud
- Improve prediction visualization

---
