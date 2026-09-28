import streamlit as st 
from utils.auth import login, signup 
from dashboard.admin_dashboard import show_dashboard 
from utils.application import apply_for_loan 
from utils.tracker import track_application
import re

st.set_page_config(page_title="Smart Loan Approval System", layout="centered")

#Inject custom CSS

with open("style/style.css") as f: 
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("""

<div class="title-container">
    <h1>💰 Smart Loan Approval Prediction</h1>
</div>
""", unsafe_allow_html=True)
#Initialize session

if 'logged_in' not in st.session_state: 
    st.session_state.logged_in = False 
    if 'role' not in st.session_state: 
        st.session_state.role = None 
        if 'user' not in st.session_state:
            st.session_state.user = ""

#Home Navigation

menu = ["Home", "Login", "Sign Up"] 
choice = st.sidebar.radio("Navigation", menu)

if choice == "Home": 
    st.markdown("""
                 <div class="content-box"> 
                    <h3>📌 Welcome to the Smart Loan Approval System</h3>
                    <p>Please use the sidebar to <strong>Login</strong> or <strong>Sign Up</strong> to continue.</p>
                 </div> """, unsafe_allow_html=True)

elif choice == "Login":
     with st.container(): 
        st.markdown(""" <div class="content-box"> <h3>🔐 Login</h3> """, unsafe_allow_html=True)
        role = st.selectbox("Login as", ["User", "Admin"])
        username = st.text_input("Username")
        password = st.text_input("Password", type="password") 
        if st.button("Login", use_container_width=True):
            if username and password:
                if login(username, password, role): 
                    st.session_state.logged_in = True
                    st.session_state.role = role
                    st.session_state.user = username
                    st.success(f"Welcome back, {username} ({role})!") 
                else:
                    st.error("Invalid credentials.") 
            else:
                st.error("please enter both username and password")
        st.markdown("</div>", unsafe_allow_html=True)

elif choice == "Sign Up":
    with st.container():
        st.markdown("<div class='content-box'><h3>📝 Sign Up</h3>", unsafe_allow_html=True)
        role = st.selectbox("Sign up as", ["User", "Admin"])
        username = st.text_input("New Username")
        password = st.text_input("New Password", type="password")

        if st.button("✅ Create Account", use_container_width=True):
            # Strong password validation
            if not password:
                st.warning("⚠️ Please enter a password.")
            elif len(password) < 8:
                st.warning("⚠️ Password must be at least 8 characters long.")
            elif not re.search(r"[A-Z]", password):
                st.warning("⚠️ Password must include at least one uppercase letter.")
            elif not re.search(r"[a-z]", password):
                st.warning("⚠️ Password must include at least one lowercase letter.")
            elif not re.search(r"[0-9]", password):
                st.warning("⚠️ Password must include at least one digit.")
            elif not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
                st.warning("⚠️ Password must include at least one special character.")
            elif signup(username, password, role):
                st.success("🎉 Account created successfully! Please log in.")
            else:
                st.warning("⚠️ User already exists.")
        st.markdown("</div>", unsafe_allow_html=True)
#Dashboard After Login

if st.session_state.logged_in: 
    st.sidebar.markdown("---") 
    st.sidebar.write(f"👤 Logged in as: {st.session_state.user} ({st.session_state.role})")

    if st.session_state.role == "Admin":
        show_dashboard()

    elif st.session_state.role == "User":
        user_menu = st.sidebar.radio("User Options", ["Apply for Loan", "Track Application"])
        if user_menu == "Apply for Loan":
            apply_for_loan(st.session_state.user)
        elif user_menu == "Track Application":
            track_application(st.session_state.user)

    if st.sidebar.button("Logout", use_container_width=True):
        st.session_state.logged_in = False
        st.session_state.role = None
        st.session_state.user = ""
        st.success("Logged out.")