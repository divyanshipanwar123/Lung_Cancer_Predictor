# 🧬 Lung Cancer Risk Prediction App

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://lungcancerpredictor-fk7avq9ecmjttpkmjkabqd.streamlit.app/)

This is a Streamlit web app that predicts the risk of lung cancer based on user-provided health and lifestyle inputs. The machine learning model was trained using a cleaned dataset from Kaggle and deployed with an interactive UI.
## 📌 Overview

This project began as a classification task using a medical survey dataset for lung cancer detection. Initially, the model suffered from **overfitting** and **class imbalance**, but these issues were identified, analyzed, and resolved through effective data handling and evaluation techniques.

The final result is a fully functional, interactive web app deployed using Streamlit Cloud.

## 📊 Dataset Summary
- Source: Kaggle [Lung Cancer Survey Data](https://www.kaggle.com/datasets/mysarahmadbhat/lung-cancer)
-**Total Records**: 309
- **Label Distribution**:
  - ✅ YES (Lung Cancer Present): 270
  - ❌ NO (Lung Cancer Absent): 39

⚠️ **Dataset not included** due to licensing. You can download it directly from Kaggle.

---

## 🚨 Initial Challenges Faced
- The original dataset was **highly imbalanced** (YES: 270, NO: 39), leading to poor generalization.
- With an 80:20 train-test split, the model **overfitted**, always predicting the majority class.
- Features like `"FATIGUE "` and `"ALLERGY "` had trailing spaces, causing mismatches in input.
- Model always returned “Low risk” regardless of inputs.

---

## ✅ What Was Fixed

- Cleaned all feature names by stripping trailing spaces.
- Re-encoded target label (`YES` → 1, `NO` → 0).
- Switched to a 70:30 split to avoid overfitting.
- Used **SMOTE (Synthetic Minority Over-sampling Technique)** to balance the training data.
- Retrained the model using `RandomForestClassifier`.
---

## 🧠 Model Pipeline

- **Preprocessing**: Label encoding, feature cleaning
- **Balancing**: `SMOTE` from `imbalanced-learn`
- **Model**: `RandomForestClassifier` (scikit-learn)
- **Evaluation**: `confusion_matrix`, `classification_report`

---

## 🖥️ Streamlit App

The app takes inputs from users in the form of dropdowns/sliders for health habits, symptoms, and demographics.

### 🔢 Features Used:
- AGE
- SMOKING
- YELLOW_FINGERS
- ANXIETY
- PEER_PRESSURE
- CHRONIC DISEASE
- FATIGUE
- ALLERGY
- WHEEZING
- ALCOHOL CONSUMING
- COUGHING
- SHORTNESS OF BREATH
- SWALLOWING DIFFICULTY
- CHEST PAIN

---
