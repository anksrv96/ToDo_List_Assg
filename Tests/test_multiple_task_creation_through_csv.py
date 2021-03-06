import json
import csv
from _csv import reader

from Conifg.config import TestData
from Pages.task_page import TaskPage
from Pages.user_page import UserPage


class TestMultipleTaskCreation:
    def test_login(self):
        self.user_page = UserPage()
        tl_response = self.user_page.login_user(TestData.EMAIL, TestData.PASSWORD)
        response_dict = json.loads(tl_response.text)
        TestData.BEARER_TOKEN = response_dict['token']

    def test_iteratively_create_task(self):
        self.task_page = TaskPage()
        with open('TestInput/tasks.csv', 'r') as read_obj:
            csv_reader = reader(read_obj)
            header = next(csv_reader)
            for task in csv_reader:
                tc_response = self.task_page.add_task(task[0])
                assert tc_response.status_code == 201, "TASK NOT CREATED"

    def test_pagination(self):
        self.task_page = TaskPage()
        tp_response = self.task_page.get_task_by_pagination(TestData.PAGINATION_LIMIT, TestData.PAGINATION_SKIP)
        assert tp_response.status_code == 200, "STATUS CODE MISMATCH"
        response_dict = json.loads(tp_response.text)
        assert response_dict['count'] == TestData.PAGINATION_LIMIT, "ERROR IN PAGINATION "


