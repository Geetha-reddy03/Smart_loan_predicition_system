import hashlib
import os
import pandas as pd

USERS_FILE = "data/users.csv"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Ensure user file exists
def init_user_store():
    if not os.path.exists(USERS_FILE):
        df = pd.DataFrame(columns=["username", "password", "role"])
        df.to_csv(USERS_FILE, index=False)

def signup(username, password, role):
    init_user_store()
    df = pd.read_csv(USERS_FILE)

    if username in df['username'].values:
        return False

    new_user = {
        "username": username,
        "password": hash_password(password),
        "role": role
    }
    new_user_df = pd.DataFrame([new_user])
    df = pd.concat([df, new_user_df], ignore_index=True)
    df.to_csv(USERS_FILE, index=False)
    return True

def login(username, password, role):
    init_user_store()
    df = pd.read_csv(USERS_FILE)

    if username in df['username'].values:
        stored_pw = df[df['username'] == username]['password'].values[0]
        stored_role = df[df['username'] == username]['role'].values[0]
        return stored_pw == hash_password(password) and stored_role == role

    return False