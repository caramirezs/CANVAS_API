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


def desmatricular_usuario(url='', token=''):
    headers = {
        "Authorization": f"Bearer {token}"
    }
    payload = {
        "task": "delete"
    }
    enroll_url = f"{url}courses/{course_id}/enrollments"
    url_1 = f"{enroll_url}?user_id={user_id}"
    print(url_1)
    print("Recuperando las matriculaciones del usuario...")
    r = requests.get(url=url_1, headers=headers)
    prin_status_response(r)
    if r.status_code == 200:
        enrollments = r.json() # esto es una lista de información
        if len(enrollments) == 0:
            print(Fore.RED + "\t No se encontraron matriculas del usuario")
            return None
        for enrollment in enrollments:
            enrollment_id = enrollment['id']
            url_2 = f'{enroll_url}/{enrollment_id}'
            print("Desmatriculando usuario")
            r = requests.delete(url=url_2, headers=headers,
                                data=payload)
            prin_status_response(r)
            if r.status_code == 200:
                print(Fore.GREEN + "\t La matricula del usuario ha sido eliminada")
            else:
                print(Fore.RED + "\t ERROR: no es posible desmatricular al usuario")

        r = requests.get(url=f"{api_url}/courses/{course_id}/sections",
                         headers=headers)
        info_sections = r.json()
        for section_id in info_sections:
            r = requests.delete(f"{api_url}/sections/{section_id['id']}",
                                params=payload, headers=headers)
            if r.status_code == 200:
                print(f">> WARNING: Se ha eliminado una sección vacía {course_id}")
    return None



#string_list = input('Ingrese la lista de cursos separados por coma: ')
#course_list = string_list.split(",")
course_id = 62739
user_id = 52
#rol_id = input('Ingrese el id del rol: ')

token = ACCESS_TOKEN
desmatricular_usuario(api_url, token=ACCESS_TOKEN)