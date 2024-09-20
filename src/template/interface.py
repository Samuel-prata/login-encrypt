import streamlit as st
import requests

def get_response(user, pwd):
    url = 'http://localhost:5000/user/login'
    payload = {'usuario': user, 'senha': pwd}
    response = requests.post(url, json=payload)
    return response

st.title('Tela de login')

user = st.text_input('digite o nome de usuario')
pwd = st.text_input('digite a senha: ')

if st.button('Entrar'):
    if user and pwd:
        response = get_response(user, pwd)
        st.write(response)
    else:
        st.write('Preencha os campos')
    
