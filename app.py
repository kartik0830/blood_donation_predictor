import streamlit as st
import pickle
import numpy as np

# Page config
st.set_page_config(
    page_title="Blood Donation AI",
    page_icon="🩸",
    layout="centered"
)

# Load model
model = pickle.load(open('blood_donation_model.pkl', 'rb'))

# --- Custom Styling ---
st.markdown("""
    <style>
    .main {
        background-color: #0E1117;
    }
    .stButton>button {
        background-color: #FF4B4B;
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 100%;
        font-size: 18px;
    }
    .stSlider label {
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown("""
# 🩸 Blood Donation Intelligence System
### Predict donor re-engagement using machine learning
""")

st.write("")

# --- Card Style Description ---
st.markdown("""
<div style="background-color:#1c1f26;padding:15px;border-radius:10px">
This AI system helps blood banks identify donors who are more likely to donate again,  
allowing better planning and targeted outreach.
</div>
""", unsafe_allow_html=True)

st.write("")

# --- Input Section ---
st.markdown("## 📋 Donor Information")

col1, col2 = st.columns(2)

with col1:
    recency = st.slider("Recency (months since last donation)", 0, 100, 2)
    frequency = st.slider("Number of donations", 0, 100, 10)

with col2:
    monetary = st.slider("Total blood donated (cc)", 0, 50000, 1000)
    time = st.slider("Time since first donation (months)", 0, 100, 12)

st.write("")

# --- Prediction Button ---
if st.button("🚀 Analyze Donor"):

    input_data = np.array([[recency, frequency, monetary, time]])

    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)

    st.markdown("## 📊 Analysis Result")

    confidence = round(probability[0][1] * 100, 2)

    if prediction[0] == 1:
        st.markdown(f"""
        <div style="background-color:#0f5132;padding:20px;border-radius:10px">
        <h3 style="color:#d1e7dd;">✅ High Probability of Re-Donation</h3>
        <p style="color:white;">Confidence Score: {confidence}%</p>
        </div>
        """, unsafe_allow_html=True)

    else:
        st.markdown(f"""
        <div style="background-color:#842029;padding:20px;border-radius:10px">
        <h3 style="color:#f8d7da;">❌ Low Probability of Re-Donation</h3>
        <p style="color:white;">Confidence Score: {confidence}%</p>
        </div>
        """, unsafe_allow_html=True)

    st.info("This prediction is based on patterns learned from historical donor data.")

# --- Insights Section ---
st.markdown("## 🧠 Insights")

st.markdown("""
- 📌 Recent donors are more likely to return  
- 📌 Frequent donors show higher engagement  
- 📌 Behavioral trends vary across individuals  
""")

# --- Footer ---
st.markdown("""
<hr>
<p style='text-align: center; color: gray;'>
Built with ❤️ using Machine Learning & Streamlit
</p>
""", unsafe_allow_html=True)