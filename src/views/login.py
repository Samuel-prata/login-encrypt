from flask import Blueprint, request, jsonify
from flask_login import LoginManager
from src.model import db
from src.model.user_model import User
from src.security.cript import hash_pwd, check_pwd


lm = LoginManager()
login_bp = Blueprint('user', __name__, url_prefix='/user')


@login_bp.route('/login', methods=['POST', ])
def user_login():
    email = request.json.get('email')
    password = request.json.get('password')
    
    print(email)
    print(password)
    from sqlalchemy import select
    stmt = select(User).where(User.email == email)
    user = db.session.execute(stmt).scalar_one()
    print(type(user))    
    
    check_password = check_pwd(password, user.password)
    
    if user and check_password:
        return jsonify({'mensagem': 'Usuario logado com sucesso.'}, f'bem vindo, {user.name}' , 200)
    else:
        return jsonify({'mensagem': 'Usuário não cadastrado'}, 400)
    
    
@login_bp.route('/register', methods=['POST', ])
def user_register():
    name = request.json.get('name')
    last_name = request.json.get('last_name')
    email = request.json.get('email')
    password = request.json.get('password')
    
    if name and last_name and email and password:
        pwd_cript = hash_pwd(password)
        new_user = User(name, last_name, email, pwd_cript)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'Mensagem': 'Usuário cadastrado com sucesso'}, 200)
    else:
        return jsonify({'Mensagem': 'Informações incorretas'}, 400)
    