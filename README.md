# 🩸 Blood Donation Prediction System

A Machine Learning-powered web application that predicts whether a donor is likely to donate blood again based on historical donation data.

---

## 🚀 Live Demo
🔗 https://kartikblooddonationpredictor.streamlit.app/

---

## 📌 Problem Statement

Blood banks often struggle to identify donors who are likely to donate again.  
This project aims to predict donor re-engagement using machine learning, helping organizations optimize donation campaigns and improve efficiency.

---

## 🧠 Solution

This system uses a trained machine learning model to analyze donor behavior and predict the likelihood of future donations.

Users can input donor details and receive:
- Prediction (Will donate or not)
- Confidence score

---

## ⚙️ Tech Stack

- Python 🐍  
- Scikit-learn 🤖  
- Streamlit 🌐  
- NumPy  

---

## 📊 Features

- Interactive web interface using Streamlit  
- Real-time prediction based on user input  
- Confidence score display  
- Clean and intuitive UI  
- Based on real-world dataset  

---

## 🧾 Input Parameters

- Recency (months since last donation)  
- Frequency (number of donations)  
- Monetary (total blood donated in cc)  
- Time (months since first donation)  

---

## 📈 Model Details

- Multiple models were evaluated:
  - Logistic Regression  
  - Decision Tree  
  - Random Forest  
- Final model selected based on performance metrics:
  - Accuracy  
  - Precision  
  - Recall  
  - F1-score  

---

## 🧠 Key Insights

- Recent donors are more likely to donate again  
- Frequent donors show higher engagement  
- Behavioral patterns vary based on donation history  

---

## ▶️ How to Run Locally

1. Clone the repository:

git clone https://github.com/kartik0830/blood-donation-predictor.git


2. Navigate to the project folder:

cd blood-donation-predictor


3. Install dependencies:

pip install -r requirements.txt


4. Run the app:

python -m streamlit run app.py


---

## 📌 Future Improvements

- Deploy using Flask API  
- Add database integration  
- Improve model with more features  
- Add authentication system  

---

## 👨‍💻 Author

Developed by **Kartik Jadhav**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
