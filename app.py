import streamlit as st
import joblib

# Load the trained model
model = joblib.load('model.pkl')

# Streamlit app
st.title("Injection Molding Price Prediction")

# User input
length = st.number_input("Enter your length:", min_value=0)
width = st.number_input("Enter your width:", min_value=0)
height = st.number_input("Enter your height:", min_value=0)

submit_button = st.button("Submit")

if submit_button:
    # Make a prediction
    prediction = model.predict([[length,width,height]])  # Adjust input shape as needed
    st.write(f'The predicted value is: {prediction[0]}')


