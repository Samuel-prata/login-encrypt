from flask import Blueprint, request, jsonify
from flask_login import LoginManager

lm = LoginManager()
login = Blueprint('user', __name__)

data = {'usuario': 'Samuel', 'senha': '12345'}

@login.route('/login', methods=['GET', 'POST'])
def user_login():
    usuario = request.json.get('nome')
    senha = request.json.get('senha')
    print(usuario)
    print(senha)
    
    if usuario == data['usuario'] and senha == data['senha']:
        return jsonify('usuario logado com sucesso'), 200
    else:
        return jsonify('usuario não encontrado'), 404