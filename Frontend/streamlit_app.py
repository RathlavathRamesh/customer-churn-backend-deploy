import streamlit as st
import requests

# 🔧 Page config
st.set_page_config(
    page_title="Customer Churn Prediction App",
    page_icon="💳",
    layout="centered"
)

# 🎯 Title
st.title("💳 Bank Customer Churn Prediction App")
st.caption("Powered by Deep Learning | FastAPI Backend | Deployed on Render")
st.markdown("---")

# 🌐 Backend API Endpoint
BACKEND_URL = "https://customer-churn-deploy-cyay.onrender.com/predict"

# 📥 Input Form
with st.form("churn_form"):
    st.subheader("📊 Enter Customer Details")

    col1, col2 = st.columns(2)
    with col1:
        credit_score = st.number_input("Credit Score", min_value=300, max_value=900, value=650)
        geography = st.selectbox("Geography", options=["France", "Spain", "Germany"])
        tenure = st.number_input("Tenure (Years)", min_value=0, max_value=20, value=5)
        has_cr_card = st.selectbox("Has Credit Card", [1, 0], help="1 = Yes, 0 = No")
        estimated_salary = st.number_input("Estimated Salary", min_value=0.0, value=50000.0)

    with col2:
        gender = st.selectbox("Gender", options=["Male", "Female"])
        age = st.number_input("Age", min_value=18, max_value=100, value=30)
        balance = st.number_input("Account Balance", min_value=0.0, value=100000.0)
        num_of_products = st.number_input("Number of Products", min_value=1, max_value=4, value=1)
        is_active_member = st.selectbox("Is Active Member", [1, 0], help="1 = Active, 0 = Inactive")

    submitted = st.form_submit_button("🔍 Predict Churn")

# 🚀 API Call on submit
if submitted:
    with st.spinner("Calling model... please wait..."):
        data = {
            'CreditScore': credit_score,
            'Geography': geography,
            'Gender': gender,
            'Tenure': tenure,
            'Balance': balance,
            'Age': age,
            'NumOfProducts': num_of_products,
            'HasCrCard': has_cr_card,
            'IsActiveMember': is_active_member,
            'EstimatedSalary': estimated_salary
        }

        try:
            response = requests.post(BACKEND_URL, json=data)
            if response.status_code == 200:
                prediction = response.json()
                st.success(f"✅ Churn Prediction Result: **{prediction}**")
            else:
                st.error("❌ Error in prediction. Please check the input data or try again later.")
        except Exception as e:
            st.error(f"⚠️ Request failed: {str(e)}")
else:
    st.info("Click the button to predict churn based on the entered customer details.")

# 📌 Footer credits
st.sidebar.markdown("---")
st.sidebar.markdown("Made with ❤️ by [Rathlavath Ramesh](https://www.linkedin.com/in/ramesh-nayak-rathlavath/)")
