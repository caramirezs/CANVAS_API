import os
import requests
from colorama import Fore, Back, Style, init

# OPERATOR_ROLE = {'estudiante': 3, 'profesor': 4, 'profesor_auxiliar': 5, 'diseñador': 6,
#                  'observador': 7, 'master': 30, 'operador': 35, 'sim': 115}
#

init(autoreset=True)  # reset the previous color and style after each line
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
api_url = f'https://poli.instructure.com/api/v1/'


def matricular_usuario(url='', payload={}, token=''):
    headers = {
        "Authorization": f"Bearer {token}"
    }
    r = requests.post(url, headers=headers, data=payload)
    if r.status_code == 200:
        color = Fore.GREEN
    else:
        color = Fore.RED
    print(color + f'{r.status_code} >> {r.reason}')
    return r


string_list = input('Ingrese la lista de cursos separados por coma: ')
course_list = string_list.split(",")
user_id = input('Ingrese el id del usuario: ')
rol_id = input('Ingrese el id del rol: ')

token = ACCESS_TOKEN
payload = {
    "enrollment[user_id]": user_id,
    "enrollment[role_id]": rol_id,
    "enrollment[enrollment_state]": "active"
}


n, m = 1, len(course_list)
for course_id in course_list:
    print(Fore.BLUE + f'[{n}/{m}]: Ingresando a {course_id}')
    url = f'{api_url}/courses/{course_id}/enrollments'
    r = matricular_usuario(url, payload, token=ACCESS_TOKEN)
    if r.status_code == 200:
        response = r.json()
        print(Fore.LIGHTGREEN_EX + f'\t El usuario {user_id} ha sido matriculado')
    else:
        print('Error')
    n = + 1
