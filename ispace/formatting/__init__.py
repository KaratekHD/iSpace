from datetime import datetime
import socket


def pretty_format(teacher: str, description: str, start_date: datetime, due_date: datetime, id, permalink: str):
    return """
-------------------
Teacher: {}
Start: {}
Due: {}
Permalink: {}
ID: {}
-------------------
{}
   
Generated {} by {} (IservBot/1.1)
    """.format(teacher, start_date.strftime("%A, %d %B %Y"), due_date.strftime("%A, %d %B %Y"), permalink, id, description, datetime.now().strftime("%A, %d %B %Y %H:%M:%S %Z"), socket.gethostname())