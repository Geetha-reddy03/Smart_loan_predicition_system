💰 **Smart Loan Approval Prediction**

A machine learning–powered web application that predicts loan approval outcomes based on applicant details. Built with Streamlit and deployed on Streamlit Community Cloud.

🔗 Live App:https://smartloanpredicitionsystem-2tizdwudlgmigypme4urmc.streamlit.app/

📌 Overview
The Smart Loan Approval Prediction system allows users to sign up, log in, and apply for a loan through a simple web interface. A trained machine learning model predicts whether the loan is likely to be approved, and an admin dashboard provides visual insights into application trends. The app also uses SHAP to explain individual predictions, making the model's decisions transparent.

✨ Features
🔐 User Authentication — Sign up and log in securely
📝 Loan Application — Users can submit loan details for prediction
🤖 ML-Based Prediction — Trained scikit-learn model predicts approval status
📊 Admin Dashboard — Visual analytics using Plotly charts
🔍 Model Explainability — SHAP values explain individual predictions
📈 Application Tracking — Track submitted applications over time

🛠️ Tech Stack
Category	Technology
Frontend / App Framework	Streamlit
Machine Learning	scikit-learn, joblib
Data Handling	pandas, numpy
Visualization	Plotly, Matplotlib
Explainability	SHAP
Deployment	Streamlit Community Cloud
Version Control	Git & GitHub

📂 Project Structure
smart_loan_predicition_system/
│
├── app.py                     # Main application entry point
├── requirements.txt           # Python dependencies
│
├── dashboard/
│   └── admin_dashboard.py     # Admin dashboard with charts
│
├── utils/
│   ├── auth.py                 # Login & signup logic
│   ├── application.py          # Loan application & prediction logic
│   └── tracker.py              # Application tracking logic
│
├── model/
│   └── loan_model.pkl          # Trained ML model
│
└── README.md
🚀 Getting Started (Run Locally)
Clone the repository
bash
   git clone https://github.com/geetha-reddy03/smart_loan_predicition_system.git
   cd smart_loan_predicition_system
Create and activate a virtual environment
bash
   python -m venv venv
   venv\Scripts\activate       # Windows
   source venv/bin/activate    # macOS/Linux
Install dependencies
bash
   pip install -r requirements.txt
Run the app
bash
   streamlit run app.py
Open the local URL shown in the terminal (usually http://localhost:8501).
🌐 Deployment

This app is deployed using Streamlit Community Cloud:

Push the project to a public GitHub repository.
Go to share.streamlit.io and sign in with GitHub.
Click Create app → select the repository, branch, and app.py as the main file.
Click Deploy.

📋 How It Works
A new user signs up or an existing user logs in.
The user fills out the loan application form with their details.
The trained ML model predicts whether the loan is likely to be approved or rejected.
SHAP explains which factors influenced the prediction.
The admin can view all applications and trends through the dashboard.
🔮 Future Improvements
Move from local file storage to a proper database (e.g., PostgreSQL / Firebase) for user data
Add email notifications for loan status updates
Improve model accuracy with additional features and hyperparameter tuning
Add role-based access control for admin vs. regular users

👩‍💻 Author
Appidi Anjili Sai Geetha.
GitHub: @geetha-reddy03

📄 License

This project is open source and available for educational purposes.
