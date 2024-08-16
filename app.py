
import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open('clf.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

# Streamlit app
st.title('Diabetes Prediction App')
st.write("Designed & Developed by Dr. Shabir Ahmad")

st.subheader("""
This app predicts the likelihood of diabetes based on the input features.
""")

# Define input fields(
col1, col2 = st.columns(2)
with col1:
    gender = st.selectbox('Gender', options=['Male', 'Female'])
with col2:
    age = st.slider('Age', min_value=0, max_value=100, value=25)
col3, col4, col5 = st.columns(3)
with col3:
    hypertension = st.selectbox('Hypertension', options=['No', 'Yes'])
with col4:
    heart_disease = st.selectbox('Heart Disease', options=['No', 'Yes'])
with col5:
    smoking_history = st.selectbox('Smoking History', options=['No', 'Yes'])
col6, col7, col8 = st.columns(3)
with col6:
    bmi = st.slider('BMI', min_value=10.0, max_value=40.0, value=22.0)
with col7:
    HbA1c_level = st.number_input('HbA1c Level', min_value=2.0, max_value=12.0, value=5.0)
with col8:
    blood_glucose_level = st.slider('Blood Glucose Level', min_value=70.0, max_value=500.0, value=100.0)

# Map the values
gender = 1 if gender == 'Male' else 0
hypertension = 1 if hypertension == 'Yes' else 0
heart_disease = 1 if heart_disease == 'Yes' else 0
smoking_history = 1 if heart_disease == 'Yes' else 0

# Prepare input data
input_data = {
    'gender': [gender],
    'age': [age],
    'hypertension': [hypertension],
    'heart_disease': [heart_disease],
    'smoking_history': [smoking_history],
    'bmi': [bmi],
    'HbA1c_level': [HbA1c_level],
    'blood_glucose_level': [blood_glucose_level]
}

# Create a DataFrame from the input data
input_df = pd.DataFrame(input_data)

# Predict the outcome
if st.button('Predict'):
    prediction = loaded_model.predict(input_df)
    st.write('Prediction:', 'Diabetic' if prediction[0] == 1 else 'Not Diabetic')