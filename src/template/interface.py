import streamlit as st
import requests

def get_response_register(name: str, last_name: str, email: str, pwd: str):
    url = 'http://localhost:5000/user/register'
    payload = {'name': name, 'last_name': last_name, 'email': email, 'password': pwd}
    response = requests.post(url, json=payload)
    return response.json()

def get_response_login(email: str, pwd: str):
    url = 'http://localhost:5000/user/login'
    payload = {'email': email, 'password': pwd}
    response = requests.post(url, json=payload)
    return response.json()

def screen_register(): 
    st.title('Tela de registro')

    name = st.text_input('digite o seu nome: ')
    last_name = st.text_input('Digite seu sobrenome: ')
    email = st.text_input('Digite seu email: ')
    pwd = st.text_input('digite a senha: ')

    if st.button('Entrar'):
        if name and last_name and email and pwd:
            response = get_response_register(name, last_name, email, pwd)
            st.write(response)
        else:
            st.write('Preencha os campos')
    
def screen_login():
    st.title('Tela de login')
    
    email = st.text_input('Digite seu email: ')
    senha = st.text_input('Digite sua senha: ')
    
    if st.button('Entrar'):
        if email and senha:
            response = get_response_login(email, senha)
            st.write(response)
        else:
            st.write('Preencha todos os campos')
    
st.sidebar.title('Navegação')
page_selected = st.sidebar.selectbox('Escolha a opção', ['Sign in', 'Sign up'])

if page_selected == 'Sign in':
    screen_login()
elif page_selected == 'Sign up':
    screen_register()