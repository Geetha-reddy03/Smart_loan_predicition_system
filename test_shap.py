import pandas as pd
import joblib
import shap

# Load your model
model = joblib.load("model/loan_model.pkl")

# Sample input (10 numerical features)
model_input = pd.DataFrame([{
    "Gender": 1,
    "Married": 1,
    "Dependents": 0,
    "Education": 1,
    "Self_Employed": 0,
    "ApplicantIncome": 5000,
    "CoapplicantIncome": 2000,
    "LoanAmount": 150,
    "Loan_Amount_Term": 360,
    "Credit_History": 0.0,
    "Property_Area": 2
}])

# SHAP explanation
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(model_input)

print("SHAP values:")
print(shap_values)