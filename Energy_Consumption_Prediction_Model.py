import streamlit as st
import numpy as np
import tensorflow as tf
import pandas as pd

# Load the trained model (.h5 format)
@st.cache_resource()
def load_model():
    model = tf.keras.models.load_model("Energy_Consumption_Prediction_Model.h5")
    return model

model = load_model()

# Streamlit App Title
st.title("Energy Consumption Prediction")

# User Inputs
hour = st.number_input("Enter Hour (0-23):", min_value=0, max_value=23, step=1)
month = st.number_input("Enter Month (1-12):", min_value=1, max_value=12, step=1)
year = st.number_input("Enter Year:", min_value=2000, max_value=2100, step=1)
day = st.number_input("Enter Day (1-31):", min_value=1, max_value=31, step=1)
weekday = st.number_input("Enter Weekday (0=Monday, 6=Sunday):", min_value=0, max_value=6, step=1)

# Prepare input features for model prediction
if st.button("Predict Energy Consumption"):
    input_data = np.array([[hour, month, year, day, weekday]])
    prediction = model.predict(input_data)
    
    # Display prediction
    st.success(f"Predicted Energy Consumption: {prediction[0][0]:.2f} kWh")
