from bs4 import BeautifulSoup
from ispace import iserv_url, SESSION
import ispace.auth as auth


class Task:
    def __init__(self, id: str, title: str, teacher: str, start_date: str, due_date: str, description: str, done: bool, permalink: str):
        self.id = id
        self.title = title
        self.teacher = teacher
        self.start_date = start_date
        self.due_date = due_date
        self.description = description
        self.permalink = permalink
        self.done = done


def get_tasks():
    tasks = []
    session = SESSION
    auth.authenticate_iserv()
    task_response = session.get(iserv_url + "/iserv/exercise?filter[status]=current")
    soup = BeautifulSoup(task_response.text, 'lxml')
    task_table = soup.find("table", {"id": "crud-table"})
    rows = task_table.find_all("tr")
    ids = []
    for row in rows:
        columns = row.find_all("td")
        if len(columns) == 7:
            title = columns[0].find("a").text
            id = columns[0].find("a")["href"].replace(iserv_url + "/iserv/exercise/show/", "")
            start_date = columns[1].text
            due_date = columns[2].text
            done = False
            if columns[4].find("span", {"class": "glyphicon-ok"}):
                done = True
            singletask = BeautifulSoup(session.get(iserv_url + "/iserv/exercise/show/" + id).text, "lxml").find_all("div", {"class" : "panel-default"})[0]
            teacher = singletask.find("tbody").find("tr").find_all("td")[0].find("a").text
            description = singletask.find("div", {"class" : "text-break-word"}).text
            tasks.append(Task(id, title, teacher, start_date, due_date, description, done, iserv_url + "/iserv/exercise/show/" + id))
            ids.append(id)
    return tasks, ids
