import json

import requests

from ispace import client_id, client_secret, space_instance, SESSION, iserv_user, iserv_passwd, iserv_url
import base64

from ispace.iserv.exceptions import LoginError


def get_token() -> str:
    data = client_id + ":" + client_secret
    encoded_bytes = base64.b64encode(data.encode("utf-8"))
    encoded_str = str(encoded_bytes, "utf-8")
    url = space_instance + "/oauth/token"
    payload = f'grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}&scope=**'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Basic ' + encoded_str
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    token = json.loads(response.text)["access_token"]
    return token


def authenticate_iserv():
    headers = {'User-Agent': 'Mozilla/5.0'}
    payload = {'_username': iserv_user, '_password': iserv_passwd}
    res = SESSION.post(iserv_url + '/iserv/app/login', headers=headers, data=payload)
    if "Anmeldung fehlgeschlagen!" in res.text:
        # IServ always returns HTTP 200 OK, therefore this workaround is required
        raise LoginError