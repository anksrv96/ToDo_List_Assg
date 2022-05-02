import ast
import json
import requests

from Conifg.config import TestData


class UserPage:
    def create_user(self, name, email, password, age):
        header = {'Content-Type': 'application/json'}
        payload = {
            "name": name,
            "email": email,
            "password": password,
            "age": age
        }

        response = requests.post(url='https://api-nodejs-todolist.herokuapp.com/user/register', json=payload,
                                 headers=header)
        resp_content = json.loads(response.text)
        TestData.BEARER_TOKEN = resp_content['token']
        print(response.status_code)
        return response

    def login_user(self, email, password):
        header = {'content-type': 'application/json'}
        payload = {
            "email": email,
            "password": password
        }

        response = requests.post(url='https://api-nodejs-todolist.herokuapp.com/user/login', json=payload,
                                 headers=header)
        print(response.content)
        return response
