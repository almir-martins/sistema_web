import pickle
from pathlib import Path
import streamlit as st
import streamlit_authenticator as stauth

# User authentication
names = ["Almir Martins", "Leonardo Cordeiro"]
usernames = ["almir", "leo"]

# Load hashed passwords
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(
    names, usernames, hashed_passwords, 
    'cookie_named_name', 'abcdef', cookie_expiry_days=1)

name, authenticattion_status, username = authenticator.login('Login', 'main')

if authenticattion_status == False:
    st.error('Username/password is incorrect')

if authenticattion_status == None:
    st.warning('Please enter your username and password')

if authenticattion_status:
    st.text('Login funcionou - deu tudo certo')