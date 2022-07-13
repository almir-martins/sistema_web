import pickle
from pathlib import Path
import streamlit_authenticator as stauth
import streamlit as st

# User authentication
names = ["Almir Martins", "Leonardo Cordeiro"]
usernames = ["almir", "leo"]

# Load hashed passwords
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(
    names,
    usernames,
    hashed_passwords,
    "cookie_named_name",
    "abcdef",
    cookie_expiry_days=0,
)


name, authenticattion_status, username = authenticator.login("Login", "main")

if authenticattion_status == False:
    st.error("Usuário ou senha incorreta")
    st.session_state["authentication_status"] = False

if authenticattion_status is None:
    st.warning("Caso não seja cadastrado visite: \nhttp://www.gmail.com")
    st.session_state["authentication_status"] = None

if authenticattion_status:
    st.text("Login funcionou - deu tudo certo")
    authenticator.logout("Logout", "sidebar")
    st.session_state["authentication_status"] = True
    st.session_state["name"] = name
