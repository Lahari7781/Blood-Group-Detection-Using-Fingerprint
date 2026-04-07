# 🧬 Blood Group Detection Using Fingerprint

## 📌 Overview
This project aims to predict a person’s blood group using fingerprint images.
It uses image processing and machine learning techniques to analyze fingerprint patterns and classify them into blood groups.

This approach is non-invasive, fast, and cost-effective compared to traditional blood testing methods.

## 🎯 Objectives
- Predict blood group from fingerprint images
- Eliminate the need for invasive blood tests
- Build an automated and efficient system
- Apply machine learning for classification

## 🛠️ Tech Stack
- Language: Python
- Libraries: OpenCV, NumPy, Pandas, Scikit-learn / TensorFlow
- Tools: VS Code / Jupyter Notebook
- Concepts:
  - Image Processing
  - Feature Extraction
  - Machine Learning

## 📂 Project Structure
Blood-Group-Detection-Using-Fingerprint/
│── app.py
│── dataset/
│── model/
│── utils/
│── static/
│── templates/
│── requirements.txt
│── README.md

## ⚙️ How It Works
1. Input: Fingerprint image
2. Preprocessing:
   - Convert to grayscale
   - Remove noise
   - Resize image
3. Feature Extraction:
   - Extract ridge patterns and textures
4. Model Prediction:
   - Trained ML model predicts blood group
5. Output:
   - Blood group (A, B, AB, O with + / -)

## 🚀 How to Run

1. Clone the Repository
git clone https://github.com/Lahari7781/Blood-Group-Detection-Using-Fingerprint.git
cd Blood-Group-Detection-Using-Fingerprint

2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate

3. Install Requirements
pip install -r requirements.txt

4. Run the Project
python app.py

## 📊 Features
- Non-invasive blood group detection
- Fast prediction system
- Easy to use
- Automated processing

## 📈 Applications
- Hospitals and emergency services
- Blood donation camps
- Rural healthcare
- Forensic investigations

## ⚠️ Disclaimer
This project is for academic purposes only.
It is not medically approved and should not be used for real medical decisions.

## 🔮 Future Scope
- Improve accuracy with large datasets
- Deploy as web/mobile application
- Integrate real-time fingerprint scanners
- Use deep learning models (CNN, ResNet)

## 🙌 Author
Lahari Reddy

## 📜 License
This project is licensed under the MIT License.
