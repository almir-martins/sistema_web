import yaml
import streamlit_authenticator as stauth
import streamlit as st

st.title("Recuperar usuário ou senha")

# Abre o arquivo de configurações com usuários cadastrados
with open("config.yaml") as file:
    config = yaml.safe_load(file)

# Cria um objeto autenticador com os dados de usuários cadastrados
authenticator = stauth.Authenticate(
    config["credentials"],
    config["cookie"]["name"],
    config["cookie"]["key"],
    config["cookie"]["expiry_days"],
    config["preauthorized"],
)

# Formulário de Esqueceu a senha
st.text("Recuperar senha")

try:
    (
        username_forgot_pw,
        email_forgot_password,
        random_password,
    ) = authenticator.forgot_password("Forgot password")
    if username_forgot_pw:
        st.success("New password sent securely")
        # Random password to be transferred to user securely
    elif username_forgot_pw == False:
        st.error("Username not found")
except Exception as e:
    st.error(e)

# Formulário de esqueceu usuário
st.text("Recuperar usuário")

try:
    username_forgot_username, email_forgot_username = authenticator.forgot_username(
        "Forgot username"
    )
    if username_forgot_username:
        st.success("Username sent securely")
        # Username to be transferred to user securely
    elif username_forgot_username == False:
        st.error("Email not found")
except Exception as e:
    st.error(e)
