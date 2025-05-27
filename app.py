# Streamlit web app
import streamlit as st
import joblib
import pandas as pd

model = joblib.load('readmission_model.pkl')
st.title("🏥 Patient Readmission Prediction")

st.write("### Enter Patient Information")

user_input = {
    'race': st.selectbox("Race", [0, 1, 2, 3]),
    'gender': st.selectbox("Gender", [0, 1]),
    'age': st.slider("Age Bucket", 0, 10, 5),
    'admission_type_id': st.selectbox("Admission Type", [1, 2, 3, 4]),
    'time_in_hospital': st.slider("Days in Hospital", 1, 20, 5)
}

if st.button("Predict Readmission"):
    input_df = pd.DataFrame([user_input])
    prediction = model.predict(input_df)[0]
    result = "Likely to be readmitted" if prediction == 1 else "Unlikely to be readmitted"
    st.success(result)

import os

model_path = os.path.join(os.path.dirname(__file__), 'readmission_model.pkl')
model = joblib.load(model_path)
