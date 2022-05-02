from Conifg.config import TestData
from Pages.task_page import TaskPage
from Pages.user_page import UserPage
import json
import logging


class TestCreateUserAddTask:
    logging.basicConfig(filename='logs/app.log', level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')

    def test_create_user(self):
        self.create_user = UserPage()
        logging.info("Creating User")
        cu_response = self.create_user.create_user(TestData.USERNAME, TestData.EMAIL,
                                                   TestData.PASSWORD, TestData.AGE)
        if cu_response.status_code == 201:
            logging.info("USER created")
        else:
            logging.info("Error in creating user")
        assert cu_response.status_code == 201, "STATUS CODE DO NOT MATCH DURING USER CREATION"


    def test_login(self):
        self.user_page = UserPage()
        tl_response = self.user_page.login_user(TestData.EMAIL, TestData.PASSWORD)
        response_dict = json.loads(tl_response.text)
        TestData.BEARER_TOKEN = response_dict['token']
        assert tl_response.status_code == 200, "LOGIN STATUS CODE DO NOT MATCH"
        assert response_dict['user']['age'] == TestData.AGE, "AGE DO NOT MATCH"
        assert response_dict['user']['name'] == TestData.USERNAME, "USERNAME DO NOT MATCH"
        assert response_dict['user']['email'].casefold() == TestData.EMAIL.casefold(), "EMAIL DO NOT MATCH"

    def test_task_creation(self):
        self.task_page = TaskPage()
        tc_response = self.task_page.add_task(TestData.DEFAULT_TASK)
        assert tc_response.status_code == 201, "CREATE TASK STATUS CODE DO NOT MATCH"


