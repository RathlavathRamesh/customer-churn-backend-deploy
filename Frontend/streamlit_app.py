import streamlit as st 
import pandas as pd
import requests


st.title("Bank Customer Churn Prediction")
st.write("Enter the customer details below:")

# Input fields for customer details
credit_score=st.number_input("Credit Score", min_value=300 , max_value=900, value=650)
geography=st.selectbox("Geography", options=["France", "Spain", "Germany"])
gender=st.selectbox("Gender",['Male', 'Female'])
tenure=st.number_input("Tenure (Years)", min_value=0, max_value=10, value=5)
balance=st.number_input("Balance", min_value=0.0, value=5000.0)
age=st.number_input("Age", min_value=18, max_value=100, value=30)
num_of_products=st.number_input("Number of Products", min_value=1, max_value=5, value=2)
has_cr_card=st.selectbox("Has Credit Card", [0,1])
is_active_member=st.selectbox("Is Active Member", [0,1])
estimated_salary=st.number_input("Estimated Salary", min_value=0.0, value=50000.0)

if st.button("Predict Churn"):
    # Create a DataFrame with the input data
    data={
        'CreditScore': credit_score,
        'Geography': geography,
        'Gender':gender,
        'Tenure':tenure,
        'Balance': balance,
        'Age': age,
        'NumOfProducts': num_of_products,
        'HasCrCard': has_cr_card,
        'IsActiveMember': is_active_member,
        'EstimatedSalary': estimated_salary
    }
    response=requests.post("http://localhost:8000/predict", json=data)
    if response.status_code == 200:
        prediction = response.json()
        st.success(f"Churn Prediction: {prediction}")
    else:
        st.error("Error in prediction. Please check the input data.")
else:
    st.write("Click the button to predict churn based on the entered customer details.")
