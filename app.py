import streamlit as st
import pandas as pd
import joblib

# Load the trained regression model
# The model file 'shelflife_regressor_model.joblib' must be in your GitHub repository
model_load_path = 'shelflife_regressor_model.joblib'
try:
    model = joblib.load(model_load_path)
except FileNotFoundError:
    st.error("Error: The model file 'shelflife_regressor_model.joblib' was not found. Please upload it to your GitHub repository.")
    st.stop()

# --- App Layout and UI (based on the image) ---
st.markdown(
    """
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .st-bu {
        background-color: #E2E8F0;
        border-radius: 1rem;
        padding: 2rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .st-cy {
        background-color: #ffffff;
        border-radius: 1rem;
        padding: 2rem;
        text-align: center;
        margin-top: 1rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .fresh {
        background-color: #34D399; /* Green for Fresh */
        color: white;
        padding: 1rem;
        border-radius: 0.5rem;
        font-weight: bold;
        text-align: center;
    }
    .spoiled {
        background-color: #EF4444; /* Red for Spoiled */
        color: white;
        padding: 1rem;
        border-radius: 0.5rem;
        font-weight: bold;
        text-align: center;
    }
    .custom-error-container {
        background-color: #FFCDD2;
        padding: 1rem;
        border-radius: 0.5rem;
        color: #B71C1C;
        text-align: left;
    }
    .error-text {
        font-weight: bold;
        color: #B71C1C;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🥛 AI-Powered Dairy Predictor")
st.write("A professional dashboard for predicting dairy product shelf life.")

# Create two columns for the input and output panels
col1, col2 = st.columns(2)

# Input Panel
with col1:
    st.header("Input")
    st.markdown('<div class="st-bu">', unsafe_allow_html=True)
    # Input fields that match the features from your dataset
    entry_id = st.number_input("Entry ID", value=1, step=1)
    temperature_c = st.number_input("Temperature (°C)", value=4.5, format="%.1f")
    time_hours = st.number_input("Time (Hours)", value=48, step=1)
    ph_level = st.number_input("pH Level", value=6.8, format="%.2f")
    smell_score = st.number_input("Smell Score (1-5)", value=3, step=1)
    visual_score = st.number_input("Visual Score (1-5)", value=4, step=1)
    microbial_count = st.number_input("Microbial Count (cfu/ml)", value=5000, step=1)
    st.markdown('</div>', unsafe_allow_html=True)

# Create a DataFrame for prediction
input_data = {
    'Entry ID': [entry_id],
    'Temperature (°C)': [temperature_c],
    'Time (Hours)': [time_hours],
    'pH Level': [ph_level],
    'Smell Score (1-5)': [smell_score],
    'Visual Score (1-5)': [visual_score],
    'Microbial Count (cfu/ml)': [microbial_count]
}
input_df = pd.DataFrame(input_data)

# Results Panel
with col2:
    st.header("Results")
    st.markdown('<div class="st-cy">', unsafe_allow_html=True)

    if st.button("Predict Shelf Life"):
        try:
            # Make the prediction
            prediction = model.predict(input_df)
            predicted_days = int(round(prediction[0]))

            # Display the result
            if predicted_days > 0:
                status = "Fresh"
                st.markdown(f'<div class="fresh">Milk Status: {status}</div>', unsafe_allow_html=True)
                st.success(f"Shelf-life remaining: {predicted_days} days")
            else:
                status = "Spoiled"
                st.markdown(f'<div class="spoiled">Milk Status: {status}</div>', unsafe_allow_html=True)
                st.error("Product is spoiled.")

        except Exception as e:
            st.markdown(f'<div class="custom-error-container"><p class="error-text">An error occurred:</p><p>{e}</p></div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)



