# recommend/recommender.py

def recommend_loan(user_data):
    if user_data['income'] > 50000 and user_data['credit_score'] > 700:
        return "🎯 Recommended: Premium Loan Plan"
    elif user_data['income'] > 30000:
        return "✅ Recommended: Standard Loan Plan"
    else:
        return "⚠️ Recommended: Basic or Micro Loan"
    

    