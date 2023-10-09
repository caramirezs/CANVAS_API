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
url = f'{api_url}accounts/1/terms?per_page=100'
headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}
print("Recuperando la información de los periodos")
r = requests.get(url=url, headers=headers)
response = r.json()['enrollment_terms']
links = r.links

n = 2
while links.get('next') is not None:
    url = r.links['next']['url']
    r = requests.get(url, headers=headers)
    response += r.json()['enrollment_terms']
    links = r.links
    n += 1
print(f'Se exportaron {n-1} páginas\n'
      f'total periodos: {len(response)}')
#Crear DataFrame

df = pd.DataFrame(response)
df.to_excel(f'periodos.xlsx', index=False)