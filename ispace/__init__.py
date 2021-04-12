import requests
from ispace.config import Config

SESSION = requests.Session()
client_id = Config.client_id
client_secret = Config.client_secret
space_instance = Config.space_instance
space_project = Config.space_project
iserv_url = Config.iserv_url
iserv_user = Config.iserv_user
iserv_passwd = Config.iserv_passwd