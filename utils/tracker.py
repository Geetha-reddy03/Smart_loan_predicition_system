import streamlit as st
import pandas as pd
import os

def track_application(username):
    APPLICATION_FILE = "data/applications.csv"

    st.subheader("📍 Track Your Application")

    if not os.path.exists(APPLICATION_FILE):
        st.warning("No applications submitted yet.")
        return

    df = pd.read_csv(APPLICATION_FILE)

    # Filter applications by username
    user_apps = df[df['username'] == username]

    if user_apps.empty:
        st.info("ℹ️ No applications found under your account.")
        return

    st.dataframe(user_apps[['bank', 'account_no', 'LoanAmount', 'status', 'Prediction', 'submitted_at']])