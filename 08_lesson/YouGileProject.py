import requests

class YouGileProjectApi:
    def __init__(self, url, login, password, company) -> None:
        self.url = url
        self.token = self.get_token(login, password, company)

    def get_token(self, login, password, name):
        payload = {
            "login": login,
            "password": password,
            "name": name
        }
        headers = {"Content-Type": "application/json"}
        response = requests.request("POST", self.url + 'auth/keys/get', json=payload, headers=headers)
        response_data = response.json()
        return response_data[0]['key']


    def get_project_list(self):
        key = self.token
        headers = {
            "Authorization": f'Bearer {key}'
        }
        resp = requests.get(self.url + '/projects', headers=headers)
        return resp.json()["content"]

    def create_project(self, title, users):
        key = self.token
        headers = {
            "Content-Type": "application/json; charset=utf-8",
            "Authorization": f'Bearer {key}',
            'Accept': "application/json; charset=utf-8"
        }
        project = {
            "title" : title,
            "users": users
        }
        response = requests.request("POST", url + 'projects', headers=headers, json=project)
        return response

    def get_project_with_id(self, project_id):
        key = self.token
        headers = {
            "Authorization": f'Bearer {key}'
        }
        response = requests.request("POST", url + f'projects/{project_id}', json=project, headers=headers)
        return response

    def edit_project(self, project_id, new_deleted, new_title, new_users):
        key = self.token
        headers = {
            "Content-Type": "application/json; charset=utf-8",
            "Authorization": f'Bearer {key}',
            'Accept': "application/json; charset=utf-8"
        }
        response = requests.request("POST", url + f'projects/{project_id}', json=project, headers=headers)
        return response



