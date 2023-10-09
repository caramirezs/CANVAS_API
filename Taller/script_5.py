# Cambiar el periodo de un curso
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

string_list = input("Ingrese la lista de cursos separados por coma: ")
course_list = string_list.split(",")

for id_course in course_list:
    url = f'{api_url}courses/{id_course}'
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }
    payload = {
        "course[term_id]": 1
    }

    r = requests.put(url=url, headers=headers, data=payload)
    prin_status_response(r)

    response = r.json()
    print(json.dumps(response, indent=2))
