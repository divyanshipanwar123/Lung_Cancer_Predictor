import streamlit as st
import pandas as pd
import pickle

# Load the trained model
model = pickle.load(open("lung_cancer_model.pkl", "rb"))

# Feature list (must match training exactly!)
FEATURES = [
    "AGE", "SMOKING", "YELLOW_FINGERS", "ANXIETY", "PEER_PRESSURE",
    "CHRONIC DISEASE", "FATIGUE", "ALLERGY", "WHEEZING", "ALCOHOL CONSUMING",
    "COUGHING", "SHORTNESS OF BREATH", "SWALLOWING DIFFICULTY", "CHEST PAIN"
]

st.set_page_config(page_title="Lung Cancer Predictor", layout="centered")
st.title("🧬 Lung Cancer Risk Prediction")

# Helper to convert YES/NO to 1/0
def encode(val): return 1 if val == "YES" else 0

# Collect input
user_inputs = {
    "AGE": st.slider("Age", 15, 100, 45),
    "SMOKING": encode(st.selectbox("Do you smoke?", ["YES", "NO"])),
    "YELLOW_FINGERS": encode(st.selectbox("Do you have yellow fingers?", ["YES", "NO"])),
    "ANXIETY": encode(st.selectbox("Do you experience anxiety?", ["YES", "NO"])),
    "PEER_PRESSURE": encode(st.selectbox("Do you feel peer pressure?", ["YES", "NO"])),
    "CHRONIC DISEASE": encode(st.selectbox("Do you have a chronic disease?", ["YES", "NO"])),
    "FATIGUE": encode(st.selectbox("Do you feel fatigue?", ["YES", "NO"])),
    "ALLERGY": encode(st.selectbox("Do you have allergies?", ["YES", "NO"])),
    "WHEEZING": encode(st.selectbox("Do you experience wheezing?", ["YES", "NO"])),
    "ALCOHOL CONSUMING": encode(st.selectbox("Do you consume alcohol?", ["YES", "NO"])),
    "COUGHING": encode(st.selectbox("Do you often cough?", ["YES", "NO"])),
    "SHORTNESS OF BREATH": encode(st.selectbox("Do you experience shortness of breath?", ["YES", "NO"])),
    "SWALLOWING DIFFICULTY": encode(st.selectbox("Do you have difficulty swallowing?", ["YES", "NO"])),
    "CHEST PAIN": encode(st.selectbox("Do you feel chest pain?", ["YES", "NO"]))
}

# Prediction
if st.button("Predict"):
    try:
        input_df = pd.DataFrame([user_inputs])[FEATURES]
        prediction = model.predict(input_df)[0]

        if prediction == 1:
            st.error("🔴 High risk of Lung Cancer")
        else:
            st.success("🟢 Low risk of Lung Cancer")
    except Exception as e:
        st.exception(f"⚠️ Prediction failed: {e}")
