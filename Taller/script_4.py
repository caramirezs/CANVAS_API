import os
import requests
import json
from colorama import Fore, Back, Style, init

# OPERATOR_ROLE = {'estudiante': 3, 'profesor': 4, 'profesor_auxiliar': 5, 'diseñador': 6,
#                  'observador': 7, 'master': 30, 'operador': 35, 'sim': 115}
#


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
url = f'{api_url}accounts/1/terms'
headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}
print("Recuperando la información de los periodos")
r = requests.get(url=url, headers=headers)

prin_status_response(r)
print(r.json())