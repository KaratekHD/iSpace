from datetime import datetime

from ispace import space_project
from ispace.formatting import pretty_format
from ispace.iserv.tasks import get_tasks
from ispace.space.issues import Issue

tasks, ids = get_tasks()
for task in tasks:
    print(f"{task.id} : {task.title}")
asked_id = input("Please enter the ID of thee task you need: ")
if asked_id not in ids:
    print("Invalid entry.")
else:
    for task in tasks:
            if task.id == asked_id:
                due_date = datetime.strptime(task.due_date[:-5].replace(" ", ""), "%d.%m.%Y")
                start_date = datetime.strptime(task.start_date, "%d.%m.%Y")
                issue = Issue(task.title, due_date, pretty_format(task.teacher, task.description, start_date, due_date, task.id, task.permalink), space_project)
                print(issue.create())
