from src.model.user_model import User
import pytest

def create_user(name, last_name, email, age):
    user =  User(name, last_name, email, age)
    return True

def test_create_user_with_success():
    user = create_user('samuel', 'silverio', 'samuel@email.com', '24') 
    assert isinstance(user, User)