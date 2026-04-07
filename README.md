# 🧬 Blood Group Detection Using Fingerprint

## 📌 Overview

This project predicts a person’s blood group using fingerprint images.
It uses image processing and machine learning techniques to analyze fingerprint patterns and classify them into blood groups.

This method is **non-invasive, fast, and cost-effective** compared to traditional blood testing.

---

## 🎯 Objectives

* Predict blood group from fingerprint images
* Reduce dependency on invasive blood tests
* Build an automated intelligent system
* Apply machine learning for classification

---

## 🛠️ Tech Stack

* **Language:** Python
* **Libraries:** OpenCV, NumPy, Pandas, TensorFlow / Keras
* **Framework:** Flask
* **Tools:** VS Code, Jupyter Notebook

### Concepts Used

* Image Processing
* Feature Extraction
* Deep Learning (CNN Model)
* Web Development (Flask)

---

## 📂 Dataset

The dataset used in this project is collected from Kaggle:

🔗 https://www.kaggle.com/datasets/rajumavinmar/finger-print-based-blood-group-dataset

### Dataset Details

* Contains fingerprint images mapped to blood groups
* Includes categories: **A, B, AB, O (+/-)**
* Used for training and testing the deep learning model

---

## 📂 Project Structure

```
Fingerprint-Based-Blood-Group-Detection/
│── bloodgroup_flask/
│   │── app.py
│   │── model.h5
│   │── instance/
│   │   └── bloodgroup.db
│   │── static/
│   │   ├── css/
│   │   ├── images/
│   │   └── uploads/
│   │── templates/
│   │   ├── base.html
│   │   ├── dashboard.html
│   │   ├── history.html
│   │   ├── index.html
│   │   ├── login.html
│   │   ├── plots.html
│   │   ├── register.html
│   │   └── test.html
│
│── fingerprint_dataset/
│── model.h5
│── Notebook.ipynb
│── requirements.txt
│── vercel.json
│── README.md
```

---

## ⚙️ How It Works

1. **Input:** Fingerprint image uploaded via web interface
2. **Preprocessing:**

   * Convert to grayscale
   * Noise removal
   * Resize image
3. **Feature Extraction:**

   * Extract ridge patterns
4. **Model Prediction:**

   * CNN model (`model.h5`) predicts blood group
5. **Output:**

   * Displays predicted blood group on web page

---

## 🌐 Web Application Features

* User authentication (Login/Register)
* Upload fingerprint image
* View prediction results
* History tracking
* Visualization (plots page)

---

## 🚀 How to Run Locally

### 1. Clone Repository

```
git clone https://github.com/Lahari7781/Blood-Group-Detection-Using-Fingerprint.git
cd Blood-Group-Detection-Using-Fingerprint
```

### 2. Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install Requirements

```
pip install -r requirements.txt
```

### 4. Run Flask App

```
cd bloodgroup_flask
python app.py
```

---

## 🚀 Deployment (Vercel)

This project can be deployed using **Vercel (Flask Serverless)**.

### Requirements:

* `vercel.json`
* `requirements.txt`
* `app.py` inside `bloodgroup_flask`

### Important:

Set **Root Directory = `bloodgroup_flask`** in Vercel.

---

## 📊 Features

* Non-invasive blood group detection
* Deep learning-based prediction
* Web interface using Flask
* Image upload & result display
* History tracking system

---

## 📈 Applications

* Hospitals and emergency services
* Blood donation camps
* Rural healthcare
* Forensic investigations

---

## ⚠️ Disclaimer

This project is for **academic purposes only**.
It is not medically approved and should not be used for real-world medical decisions.

---

## 🔮 Future Scope

* Improve accuracy with larger datasets
* Deploy as mobile application
* Integrate real-time fingerprint scanners
* Use advanced models (ResNet, EfficientNet)

---

## 🙌 Author

**Lahari Reddy**

---

## 📜 License

This project is licensed under the MIT License.
