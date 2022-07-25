import yaml
import streamlit_authenticator as stauth
import streamlit as st

st.title("Página de cadastro")


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

try:
    if authenticator.register_user("Register user", preauthorization=False):
        st.success("User registered successfully")
except Exception as e:
    st.error(e)
