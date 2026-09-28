import shap
import streamlit as st
import matplotlib.pyplot as plt

def explain_prediction(model, input_df):
    st.subheader("📌 Explainable AI (SHAP)")
    try:
        explainer = shap.Explainer(model)
        shap_values = explainer(input_df)

        st.set_option('deprecation.showPyplotGlobalUse', False)
        shap.plots.waterfall(shap_values[0], show=False)
        st.pyplot(bbox_inches='tight')
    except Exception as e:
        st.warning(f"Explanation could not be generated. Error: {e}")