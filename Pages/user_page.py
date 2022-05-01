import requests

from Conifg.config import TestData


class UserPage:
    def create_user(self, name, email, password, age):
        header = {'content-type': 'application/json'}
        payload = {
            "name": name,
            "email": email,
            "password": password,
            "age": age
        }

        response = requests.get(url='https://api-nodejs-todolist.herokuapp.com/user/register', json=payload,
                                headers=header)
        TestData.set_bearer_token(response["token"])
        return response

    def login_user(self, email, password):
        header = {'content-type': 'application/json'}
        payload = {
            "email": email,
            "password": password
        }

        response = requests.get(url='https://api-nodejs-todolist.herokuapp.com/user/register', json=payload,
                                headers=header)
        return response

