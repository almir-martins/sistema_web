import streamlit_authenticator as stauth
import streamlit as st


if st.session_state["authentication_status"] == False:
    st.error("Username/password is incorrect")
elif st.session_state["authentication_status"] == None:
    st.warning("Please enter your username and password")
elif st.session_state["authentication_status"]:

    st.write(f'Welcome *{st.session_state["name"]}*')

    st.title("Página 2 - Requer autenticação")

    st.text("Prencha o formulário abaixo")

    st.text_input("Nome")
    st.text_input("Senha")
    st.text_input("Repetir senha")
