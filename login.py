import yaml
import streamlit_authenticator as stauth
import streamlit as st

# Caminho absoluto da url
path = "http://localhost:8501/"

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

# Cria uma página de login na página principal
name, authentication_status, username = authenticator.login("Login", "main")


if authentication_status == False:
    st.error("Usuário/senha incorreto")

    cadastro = "Não tem **cadastro**? [Clique aqui](" + path + "cadastro)"
    st.markdown(cadastro, unsafe_allow_html=True)
    senha = "Esqueceu a **senha**? [Clique aqui](#esqueceu_senha)"
    st.markdown(senha, unsafe_allow_html=True)
    st.markdown(
        "Esqueceu o **usuário**? [Clique aqui](#esqueceu_senha)", unsafe_allow_html=True
    )

elif authentication_status == None:
    st.warning("Entre com seu usuário e senha")

    cadastro = '<a href="http://localhost:8501/cadastro" target="_self">Clique aqui</a>'
    st.markdown("Não tem casdastro? " + cadastro, unsafe_allow_html=True)
    senha = (
        '<a href="http://localhost:8501/esqueceu_senha" target="_self">Clique aqui</a>'
    )
    st.markdown("Esqueceu a senha? " + senha, unsafe_allow_html=True)

elif authentication_status:
    authenticator.logout("Logout", "sidebar")
    st.text(f"Bem vindo a área logada, {name}!")
