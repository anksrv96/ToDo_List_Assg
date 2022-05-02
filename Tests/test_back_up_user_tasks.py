import json
from _csv import writer

from Conifg.config import TestData
from Pages.task_page import TaskPage
from Pages.user_page import UserPage


class TestBackupUserTasks():
    def test_login(self):
        self.user_page = UserPage()
        tl_response = self.user_page.login_user(TestData.EMAIL, TestData.PASSWORD)
        response_dict = json.loads(tl_response.text)
        TestData.BEARER_TOKEN = response_dict['token']

    def test_back_up_user_tasks(self):
        self.task_page = TaskPage()
        tl_response = self.task_page.get_all_task()
        assert tl_response.status_code == 200
        response_dict = json.loads(tl_response.text)
        count = response_dict['count']
        print('Total tasks. . .', count)
        with open('TestOutput/tasks_backup.csv', 'a', newline='') as f_object:
            header_row = ["completed", "_id", "description", "owner", "createdAt", "updatedAt", "__v"]
            writer_object = writer(f_object)
            writer_object.writerow(header_row)
            for data in response_dict['data']:
                temp_list = []

                for elements in header_row:
                    temp_list.append(data[elements])
                writer_object.writerow(temp_list)

            f_object.close()

