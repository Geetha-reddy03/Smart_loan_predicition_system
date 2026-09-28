def calculate_credit_score(applicant_income, coapplicant_income, loan_amount, credit_history):
    income_score = (applicant_income + coapplicant_income) / (loan_amount + 1)
    history_score = 1 if credit_history == 1.0 else 0.5
    score = round(min(100, income_score * history_score * 20), 2)

    if score > 80:
        category = "Low Risk"
    elif score > 50:
        category = "Moderate Risk"
    else:
        category = "High Risk"

    return score, category