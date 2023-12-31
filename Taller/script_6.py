import os
import requests
import json
import pandas as pd
from colorama import Fore, Back, Style, init

init(autoreset=True)  # reset the previous color and style after each line
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
api_url = f'https://poli.instructure.com/api/v1/'

def prin_status_response(r):
    if r.status_code == 200:
        color = Fore.GREEN
    else:
        color = Fore.RED
    print(color + f'{r.status_code} >> {r.reason}')

api_url = f'https://poli.instructure.com/api/v1/'
account_id = 20
headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}

source_course_id = 62739
for n in range(3):
    url = f'{api_url}accounts/{account_id}/courses'
    payload = {
        "course[name]": f"PRUEBA_OCT_11.CAMILO-{n+1}",
        "enroll_me": True
    }

    r = requests.post(url=url, headers=headers, data=payload)
    prin_status_response(r)

    if r.status_code == 200:
        response = r.json()
        course_id = response["id"]
        print(f'Curso creado, id: {response["id"]}')

    url = f'{api_url}courses/{course_id}/content_migrations'
    payload = {
        "migration_type": "course_copy_importer",
        "settings[source_course_id]": str(source_course_id)
    }

    r = requests.post(url=url, headers=headers, data=payload)
    prin_status_response(r)
    if r.status_code == 200:
        response = r.json()
        print(json.dumps(response, indent=2))