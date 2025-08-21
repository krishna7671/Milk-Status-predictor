import streamlit as st
import pandas as pd
import joblib

# Load the trained model from the same directory
model_load_path = 'my_dairy_model.joblib'
model = joblib.load(model_load_path)

# App title and description
st.title("🥛 AI-Powered Shelf-Life Predictor")
st.write("Enter the product's features to predict its status.")

# Input widgets for user data
st.header("Enter Product Details:")

# The labels in these widgets are for the user to see, but the
# variable names must match the dictionary keys later.
entry_id = st.number_input("Entry ID", value=1)
temperature = st.number_input("Temperature (ºC)", value=4.5)
time = st.number_input("Time (Hours)", value=48)
ph_level = st.number_input("pH Level", value=6.7)
smell_score = st.number_input("Smell Score (1-5)", value=3)
visual_score = st.number_input("Visual Score (1-5)", value=4)
microbial_count = st.number_input("Microbial Count (cfu/ml)", value=5000)

# Create a DataFrame for prediction
# The keys in this dictionary MUST EXACTLY match the column names
# you just saw from your training data.
data = {
    'Entry ID': [entry_id],
    'Temperature (ºC)': [temperature],
    'Time (Hours)': [time],
    'pH Level': [ph_level],
    'Smell Score (1-5)': [smell_score],
    'Visual Score (1-5)': [visual_score],
    'Microbial Count (cfu/ml)': [microbial_count]
}
input_df = pd.DataFrame(data)

# Make a prediction when the button is clicked
if st.button("Predict Status"):
    prediction = model.predict(input_df)
    st.subheader("Prediction Result:")
    st.write(f"The predicted status is: **{prediction[0]}**")
