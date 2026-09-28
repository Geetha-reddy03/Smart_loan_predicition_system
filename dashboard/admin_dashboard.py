import streamlit as st
import pandas as pd
import os
import plotly.express as px
import joblib

def show_dashboard():
    st.subheader("📊 Admin Dashboard")

    APPLICATION_FILE = "data/applications.csv"
    MODEL_FILE = "model/loan_model.pkl"
    FEATURE_ORDER_FILE = "model/feature_order.pkl"

    if not os.path.exists(APPLICATION_FILE):
        st.warning("No applications submitted yet.")
        return

    df = pd.read_csv(APPLICATION_FILE)

    if not os.path.exists(MODEL_FILE) or not os.path.exists(FEATURE_ORDER_FILE):
        st.error("❌ Trained model or feature order file not found.")
        return

    model = joblib.load(MODEL_FILE)
    feature_order = joblib.load(FEATURE_ORDER_FILE)

    # Preprocessing for prediction
    required_columns = [
        'Gender', 'Married', 'Dependents', 'Education',
        'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
        'Loan_Amount_Term', 'Credit_History', 'Property_Area'
    ]

    # Ensure required features exist
    missing = [col for col in required_columns if col not in df.columns]
    if missing:
        st.error(f"⚠️ Missing columns in application data: {missing}")
        return

    X = df[required_columns].copy()
    X.fillna(0, inplace=True)

    # Encode categorical features
    categorical_cols = ['Gender', 'Married', 'Dependents', 'Education', 'Property_Area']
    for col in categorical_cols:
        X[col] = X[col].astype(str)
    X_encoded = pd.get_dummies(X)
    if X_encoded.empty:
        st.error("⚠️ No valid application data found for prediction.")
        st.stop()

    # Align columns to match model feature order
    for col in feature_order:
        if col not in X_encoded.columns:
            X_encoded[col] = 0
    X_encoded = X_encoded[feature_order]

    try:
        predictions = model.predict(X_encoded)
        df["Prediction"] = ["✅ Approved" if p == 1 else "❌ Rejected" for p in predictions]
    except Exception as e:
        st.error(f"❌ Prediction failed: {e}")
        return

    # Save predictions
    df.to_csv(APPLICATION_FILE, index=False)

    # Show application data
    st.markdown("### 🗂️ Loan Applications with Predictions")
    st.dataframe(df)

    # Show summary chart
    st.markdown("### 📊 Prediction Summary")
    pie_df = df['Prediction'].value_counts().reset_index()
    pie_df.columns = ['Result', 'Count']
    fig = px.pie(pie_df, names='Result', values='Count', title='Loan Approval Summary')
    st.plotly_chart(fig)

    # Download option
    with st.expander("⬇️ Download Predictions"):
        st.download_button("Download CSV", df.to_csv(index=False).encode(), "predicted_applications.csv", "text/csv")
    

    # Notify users if their loan is approved or rejected
    notified_users = set()  # Prevent multiple SMS for same user in session

    for _, row in df.iterrows():
        mobile = str(row.get("mobile", ""))
        decision = row.get("Prediction", "")

        if mobile and decision in ["✅ Approved", "❌ Rejected"] and mobile not in notified_users:
            # Simulate sending SMS
            st.info(f"📱 Sending SMS to {mobile}: Your loan has been {decision.replace('✅ ', '').replace('❌ ', '').lower()}.")
            print(f"SMS to {mobile}: Your loan has been {decision.replace('✅ ', '').replace('❌ ', '').lower()}.")
            notified_users.add(mobile)