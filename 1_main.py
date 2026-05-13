
import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("1_ridge_regression_model.pkl", "rb"))

st.title("💼 Salary Prediction App")

experience = st.number_input("Experience (years)", min_value=0.0, step=0.1)
age = st.number_input("Age", min_value=18, max_value=65)
education = st.number_input("Education Level (0=HS, 1=BS, 2=MS, 3=PhD)", min_value=0, max_value=3)
job_level = st.number_input("Job Level (1–5)", min_value=1, max_value=5)

if st.button("Predict Salary"):
    features = np.array([[experience, age, education, job_level]])
    prediction = model.predict(features)
    st.success(f"Predicted Salary: {prediction[0]:,.2f}")
