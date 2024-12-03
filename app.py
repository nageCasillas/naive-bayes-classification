import streamlit as st
import pickle
import numpy as np

# Title of the app
st.title("Predict Time of Day for Restaurant Tips")

@st.dialog("Predict Time of Day")
def predict():
    # Display input parameters
    st.write("Input Parameters:")
    st.write(f"Total Bill: {total_bill}")
    st.write(f"Sex: {sex}")
    st.write(f"Smoker: {smoker}")
    st.write(f"Day: {day}")
    st.write(f"Size: {size}")
    st.write(f"Tip: {tip}")

    # Load the LabelEncoder and OneHotEncoder from pickle files
    with open('model/sex_label.pkl', 'rb') as le_file:
        sex_label_encoder = pickle.load(le_file)

    with open('model/smoker_label.pkl', 'rb') as le_file:
        smoker_label_encoder = pickle.load(le_file)

    with open('model/one_hat.pkl', 'rb') as ohe_file:
        one_hot_encoder = pickle.load(ohe_file)

    # Apply Label Encoding on 'sex' and 'smoker'
    sex_encoded = sex_label_encoder.transform([sex])[0]
    smoker_encoded = smoker_label_encoder.transform([smoker])[0]

    # Apply One-Hot Encoding on 'day'
    day_encoded = one_hot_encoder.transform([[day]])[0]
    print(type(day_encoded))

    # Prepare input data for prediction
    input_data = np.array([[total_bill, sex_encoded, smoker_encoded, *day_encoded, size, tip]])

    # Load the trained model from the pickle file
    with open('model/model.pkl', 'rb') as f:
        model = pickle.load(f)

    # Use the loaded model to predict the 'time' of the restaurant visit
    prediction = model.predict(input_data)
    st.write(f"Predicted Time: {'Dinner' if prediction[0] == 1 else 'Lunch'}")

# Total Bill: Numerical input
total_bill = st.number_input('Total Bill ($)', min_value=0.0, value=20.0, step=0.1)

# Sex: Radio button for selecting male or female
sex = st.radio('Sex', options=['Male', 'Female'])

# Smoker: Radio button for yes or no
smoker = st.radio('Smoker', options=['Yes', 'No'])

# Day: Select the day of the week
day = st.selectbox('Day', options=['Thur', 'Fri', 'Sat', 'Sun'])

# Size: Numerical input for the number of people
size = st.number_input('Size (Number of People)', min_value=1, value=2, step=1)

# Tip: Numerical input for the tip amount
tip = st.number_input('Tip ($)', min_value=0.0, value=3.0, step=0.1)

# Check if any input is missing
inputs_filled = all([
    total_bill is not None,
    sex is not None,
    smoker is not None,
    day is not None,
    size is not None,
    tip is not None
])

# Button to submit the form
if st.button('Predict Time', disabled=not inputs_filled):
    predict()

# Display a message if the button is inactive
if not inputs_filled:
    st.write("Please fill out all the inputs to enable the prediction.")
