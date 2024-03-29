from fastapi import status

from .utils import *
from ..routers.users import  get_current_user, get_db
from ..models import Todos

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

def test_return_user(test_user):
    response = client.get('/user')
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['username'] == test_user.username


def test_change_password_success(test_user):
    response = client.put('/user/password', json={"password": "12345", "new_password": "123456"})
    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_change_password_invalid_current_password(test_user):
    response = client.put('/user/password', json={"password": "wrong_password", "new_password": "123456"})
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() == {'detail':'Error on password change'}

def test_change_phone_number_success(test_user):
    response = client.put('/user/phonenumber/2222222222')
    assert response.status_code == status.HTTP_204_NO_CONTENT