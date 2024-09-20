import requests

def test_get_user_id():
    response = requests.get('http://localhost:5000/get_id/1')
    assert response.status_code == 200
