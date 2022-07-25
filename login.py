import yaml
import streamlit_authenticator as stauth
import streamlit as st

st.write(st.__version__)

# # Abre o arquivo de configurações com usuários cadastrados
# with open("config.yaml") as file:
#     config = yaml.safe_load(file)

# # Cria um objeto autenticador com os dados de usuários cadastrados
# authenticator = stauth.Authenticate(
#     config["credentials"],
#     config["cookie"]["name"],
#     config["cookie"]["key"],
#     config["cookie"]["expiry_days"],
#     config["preauthorized"],
# )

# # Cria uma página de login na página principal
# name, authentication_status, username = authenticator.login("Login", "main")


# if authentication_status == False:
#     st.error("Usuário/senha incorreto")

#     link = "Não tem **cadastro**? [Clique aqui](http://localhost:8501/cadastro)"
#     st.markdown(link, unsafe_allow_html=True)

#     st.markdown("Esqueceu a **senha**? [Clique aqui](#senha)", unsafe_allow_html=True)
#     st.markdown("Esqueceu o **usuário**? [Clique aqui](#usuario)", unsafe_allow_html=True)

# elif authentication_status == None:
#     st.warning("Entre com seu usuário e senha")

#     link = "Não tem **cadastro**? [Clique aqui](http://localhost:8501/cadastro)"
#     st.markdown(link, unsafe_allow_html=True)
#     st.markdown('Please <a href="http://localhost:8501/cadastro" target="_self">click</a>')

# elif authentication_status:
#     authenticator.logout("Logout", "sidebar")    
#     st.text(f'Bem vindo a área logada, {name}!')
