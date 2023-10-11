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
url = f'{api_url}accounts/{account_id}/courses'
headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}
payolad = {
    "course[name]": "PRUEBA_OCT_11"
}

r = requests.post(url=url, headers=headers, data=payolad)
prin_status_response(r)

if r.status_code == 200:
    response = r.json()
    print(json.dumps(response, indent=2))


