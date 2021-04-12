from datetime import datetime

from ispace import space_instance, SESSION
from ispace.auth import get_token


class Issue:
    def __init__(self, title: str, due: datetime, description: str, project: str):
        self.title = title
        self.due = due,
        self.description = description
        self.project = project

    def create(self) -> str:
        print(self.due[0].date)
        headers = {"Content-type": "application/json",
            "Accept": "application/json",
            "Authorization" : "Bearer " + get_token()}
        data = {"title" : self.title, "description" : self.description, "status" : "4Si8Wt3CIvg4" , "dueDate" : self.due[0].strftime("%Y-%m-%d")}
        url = f"{space_instance}/api/http/projects/id:{self.project}/planning/issues"
        response = SESSION.post(url, json=data, headers=headers)
        return response.text