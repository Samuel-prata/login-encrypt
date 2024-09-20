from flask import Flask
from src.views.login import login_bp
from src.model import db
from src.config import Config 

def create_app():
    app = Flask(__name__)
    app.register_blueprint(login_bp)
    app.config.from_object(Config)
    db.init_app(app)
    
    with app.app_context():
        db.create_all()    
    
    return app