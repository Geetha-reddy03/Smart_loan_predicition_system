import streamlit as st 
import pandas as pd
import os 
from datetime import datetime 
import joblib 
import shap

def apply_for_loan(username): 
    model = joblib.load("model/loan_model.pkl") 
    APPLICATION_FILE = "data/applications.csv"

    st.subheader("📝 Apply for a Loan")

    # Step 1: Bank Verification
    st.subheader("🔍 Bank Verification")
    bank_list = ['HDFC', 'SBI', 'ICICI', 'Axis', 'Kotak']
    selected_bank = st.selectbox("Select Bank", bank_list)
    account_no = st.text_input("Enter Bank Account Number")
    mobile = st.text_input("Enter your mobile number")

    if st.button("Validate Bank Details"):
        if not selected_bank or not account_no:
            st.error("❌ Please select a bank and enter an account number.")
        elif not account_no.isdigit():
            st.warning("⚠️ Account number must contain only digits")
        elif len(account_no) != 13:
            st.warning("⚠️ Bank account number must be exactly 13 digits.")
        else:
            st.success("✅ Bank validated.")
            st.session_state["bank_verified"] = True

    # Step 2: Loan Application Form
    if st.session_state.get("bank_verified", False):
        st.subheader("📄 Loan Application Form")

        gender = st.selectbox("Gender", ["Male", "Female"])
        married = st.selectbox("Married", ["Yes", "No"])
        dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
        education = st.selectbox("Education", ["Graduate", "Not Graduate"])
        applicant_income = st.number_input("Applicant Income", min_value=0)
        coapplicant_income = st.number_input("Coapplicant Income", min_value=0)
        loan_amount = st.number_input("Loan Amount", min_value=0)
        loan_amount_term = st.number_input("Loan Term (in days)", min_value=0)
        credit_history = st.selectbox("Credit History", [1.0, 0.0])
        property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

        if st.button("Submit Loan Application"):
    # Check all required fields are filled
            if not all([
                gender, married, dependents, education,
                applicant_income > 0,
                coapplicant_income >= 0,
                loan_amount > 0,
                loan_amount_term > 0,
                mobile,
                credit_history in [1.0, 0.0],
                property_area
            ]):
                st.warning("⚠️ All fields are required. Please ensure none are left empty or zero.")
            
            elif not (mobile.isdigit() and len(mobile) == 10):
                st.warning("⚠️ Mobile number must be exactly 10 digits and numeric.")
            
            else:
                new_application = {
                    "username": username,
                    "bank": selected_bank,
                    "account_no": account_no,
                    "Gender": gender,
                    "Married": married,
                    "Dependents": dependents,
                    "Education": education,
                    "ApplicantIncome": applicant_income,
                    "CoapplicantIncome": coapplicant_income,
                    "LoanAmount": loan_amount,
                    "Loan_Amount_Term": loan_amount_term,
                    "Credit_History": credit_history,
                    "Property_Area": property_area,
                    "mobile": mobile,
                    "status": "Under Review",
                    "submitted_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "Prediction":""
                }

                # Save to CSV
                if os.path.exists(APPLICATION_FILE) and os.path.getsize(APPLICATION_FILE) > 0:
                    df = pd.read_csv(APPLICATION_FILE)
                else:
                    df = pd.DataFrame(columns=new_application.keys())

                new_df = pd.DataFrame([new_application])
                if not df.empty:
                    new_df = new_df[df.columns]  # Ensure same columns
                df = pd.concat([df, new_df], ignore_index=True)
                df.to_csv(APPLICATION_FILE, index=False)

                st.success("🎉 Successfully applied! You'll receive a status update via email or mobile within a few days.")
                