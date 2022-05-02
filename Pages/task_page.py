import requests

from Conifg.config import TestData


class TaskPage:
    def add_task(self, task):
        bearer_token = 'Bearer '+TestData.BEARER_TOKEN
        header = {'Authorization': bearer_token, 'content-type': 'application/json'}
        payload = {
            "description": task
        }

        response = requests.post(url='https://api-nodejs-todolist.herokuapp.com/task', json=payload,
                                 headers=header)
        print(response.content)
        return response
