from src.model import db

class User (db.Model):
    __tablename__ = 'tb_user'
    id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String (100), unique=True)
    password = db.Column(db.String (100))
    
    
    def __init__(self, name: str, last_name: str, email: str, password: str) -> None:
        self.name = name
        self.last_name = last_name
        self.email = email
        self.password = password

        
    def __repr__(self) -> dict:
        return {
            'nome': self.name,
            'sobrenome': self.last_name,
            'email': self.email
        }