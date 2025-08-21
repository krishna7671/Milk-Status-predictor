import streamlit as st
import pandas as pd
import joblib

# Load the trained model
# Ensure this path is correct and your Drive is mounted
model_load_path = 'my_dairy_model.joblib'
model = joblib.load(model_load_path)

# App title and description
st.title("🥛 AI-Powered Shelf-Life Predictor")
st.write("Enter the product's features to predict its status.")

# Input widgets
st.header("Enter Product Details:")

# The variable names for the inputs can be anything you like
# The key is that the names in the data dictionary at the end must exactly match the model's features
entry_id = st.number_input("Entry ID", value=1001)
microbial_count = st.number_input("Microbial Count (cfu/ml)", value=5000)
smell_score = st.number_input("Smell Score (1-5)", value=2)
temperature = st.number_input("Temperature (ºC)", value=4.5)
time = st.number_input("Time (Hours)", value=48)

# Create a DataFrame for prediction
# The keys in this dictionary must EXACTLY match the names of the features
# that your model was trained on.
data = {
    'Entry ID': [entry_id],
    'Microbial Count (cfu/ml)': [microbial_count],
    'Smell Score (1-5)': [smell_score],
    'Temperature (ºC)': [temperature],
    'Time (Hours)': [time]
}
input_df = pd.DataFrame(data)

# Make a prediction when the button is clicked
if st.button("Predict Status"):
    prediction = model.predict(input_df)
    st.subheader("Prediction Result:")
    st.write(f"The predicted status is: **{prediction[0]}**")
