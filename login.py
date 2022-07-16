import yaml
import streamlit_authenticator as stauth
import streamlit as st
import webbrowser

with open("config.yaml") as file:
    config = yaml.safe_load(file)

authenticator = stauth.Authenticate(
    config["credentials"],
    config["cookie"]["name"],
    config["cookie"]["key"],
    config["cookie"]["expiry_days"],
    config["preauthorized"],
)


name, authentication_status, username = authenticator.login("Login", "main")


if authentication_status == False:
    st.error("Usuário/senha incorreto")

    # st.markdown("Esqueci minha **senha**. [Clique aqui](/cadastro)")
    st.markdown(
        "Não tem **cadastro**? [Clique aqui](#cadastro)", unsafe_allow_html=True
    )
    st.markdown("Esqueceu a **senha**? [Clique aqui](#senha)", unsafe_allow_html=True)
    st.markdown(
        "Esqueceu o **usuário**? [Clique aqui](#usuario)", unsafe_allow_html=True
    )

elif authentication_status == None:
    st.warning("Entre com seu usuário e senha")
    # st.markdown("Esqueci minha **senha**. [Clique aqui](/cadastro)")
    st.markdown(
        "Não tem **cadastro**? [Clique aqui](#cadastro)", unsafe_allow_html=True
    )
    st.markdown("Esqueceu a **senha**? [Clique aqui](#senha)", unsafe_allow_html=True)
    st.markdown(
        "Esqueceu o **usuário**? [Clique aqui](#usuario)", unsafe_allow_html=True
    )

elif authentication_status:
    authenticator.logout("Logout", "sidebar")
    webbrowser.open("http://localhost:8501/home", new=0)
