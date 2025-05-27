
import streamlit as st
import pandas as pd
import joblib

st.title("🏥 Patient Readmission Prediction")

st.markdown("Predict if a patient will be readmitted within 30 days of discharge.")

# Load model
model = joblib.load("models/readmission_model.pkl")

# Input fields
st.header("Enter Patient Information:")
race = st.selectbox("Race", ['Caucasian', 'AfricanAmerican'])
gender = st.selectbox("Gender", ['Male', 'Female'])
age = st.selectbox("Age Range", ['[70-80)', '[60-70)'])
time_in_hospital = st.slider("Time in Hospital (days)", 1, 14, 3)
num_lab_procedures = st.slider("Number of Lab Procedures", 1, 100, 40)
num_medications = st.slider("Number of Medications", 1, 50, 10)
number_outpatient = st.slider("Number of Outpatient Visits", 0, 20, 0)
number_emergency = st.slider("Number of Emergency Visits", 0, 20, 0)
number_inpatient = st.slider("Number of Inpatient Visits", 0, 20, 0)
diabetesMed = st.selectbox("On Diabetes Medication?", ['Yes', 'No'])

# Simple encoding
def encode_features():
    return pd.DataFrame([{
        'race': 0 if race == 'Caucasian' else 1,
        'gender': 0 if gender == 'Male' else 1,
        'age': 0 if age == '[70-80)' else 1,
        'time_in_hospital': time_in_hospital,
        'num_lab_procedures': num_lab_procedures,
        'num_medications': num_medications,
        'number_outpatient': number_outpatient,
        'number_emergency': number_emergency,
        'number_inpatient': number_inpatient,
        'diabetesMed': 1 if diabetesMed == 'Yes' else 0
    }])

if st.button("Predict"):
    input_df = encode_features()
    prediction = model.predict(input_df)[0]
    if prediction == 1:
        st.error("🔁 Patient is likely to be readmitted within 30 days.")
    else:
        st.success("✅ Patient is not likely to be readmitted within 30 days.")
