from imaplib import _Authenticator
import pickle
from pathlib import Path
import streamlit_authenticator as stauth


# Configuração da lista de usuários
names = ["Almir Martins", "Leonardo Cordeiro"]
usernames = ["almir", "leo"]
password = ["123", "456"]  # alterar pelos valores gerados pelo hash

# Criptografando as senhas (alterar posteriormente para um sistema mais seguro)
hashed_passwords = stauth.Hasher(["123", "456"]).generate()


file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)