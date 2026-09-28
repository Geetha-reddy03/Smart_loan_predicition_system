import pandas as pd
import joblib
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# 1. Load dataset
df = pd.read_csv("loan_data.csv")

# 2. Convert target variable
df["Loan_Status"] = df["Loan_Status"].map({"Y": 1, "N": 0})

# 3. Define categorical columns (excluding Self_Employed)
cat_cols = ['Gender', 'Married', 'Dependents', 'Education', 'Property_Area']
for col in cat_cols:
    df[col] = df[col].astype(str)

# 4. Define X and y
X = df.drop("Loan_Status", axis=1)
y = df["Loan_Status"]

# 5. One-hot encoding
X_encoded = pd.get_dummies(X)

# 6. Save the column order used during training
os.makedirs("model", exist_ok=True)
joblib.dump(list(X_encoded.columns), "model/feature_order.pkl")

# 7. Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_encoded, y)

# 8. Save the trained model
joblib.dump(model, "model/loan_model.pkl")

print("✅ Model trained and saved successfully.")