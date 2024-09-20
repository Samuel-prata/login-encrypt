from flask import Flask
from src.views.login import login

def create_app():
    app = Flask(__name__)
    app.register_blueprint(login)
    
    return app