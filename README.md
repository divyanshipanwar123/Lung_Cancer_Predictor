# 🧬 Lung Cancer Risk Prediction App

This is a Streamlit web app that predicts the risk of lung cancer based on survey responses. The machine learning model was trained using a cleaned dataset from Kaggle and deployed with an interactive UI.

## 🔍 Dataset Info (Not Included)
- Source: Kaggle (Lung Cancer Survey Data)
- Total Records: `n = 309`
- Class Distribution:
  - `YES (Lung Cancer Present)`: 270
  - `NO (Lung Cancer Absent)`: 39

> The dataset is not included in this repository due to licensing. You can find it [here](https://www.kaggle.com/datasets/mysarahmadbhat/lung-cancer).

---

## 🚨 Initial Model Issue

When training with an 80-20 split, the model was overfitting to the majority class (`YES`), always predicting “Low risk” due to imbalanced labels.

### ❌ Problem
```plaintext
confusion matrix:
[[ 2  0]
 [60  0]]
