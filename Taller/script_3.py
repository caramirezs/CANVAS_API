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
    r = requests.get(url=url_1, headers=headers)
    if r.status_code == 200:
        enrollments = r.json() # esto es una lista de información
        print(enrollments)
        if len(enrollments) == 0:
            print(Fore.RED + "\t No se encontraron matriculas del usuario")
            return None
        for enrollment in enrollments:
            enrollment_id = enrollment['id']
            url_2 = f'{enroll_url}/{enrollment_id}'
            r = requests.delete(url=url_2,
                                headers=headers,
                                data=payload
                                )
            if r.status_code == 200:
                print(Fore.GREEN + "\t La matricula del usuario ha sido eliminada")

        # Falta verificar si la sección quedo vacía y eliminarla

    return None



#string_list = input('Ingrese la lista de cursos separados por coma: ')
#course_list = string_list.split(",")
course_id = input('Ingrese el curso: ')
user_id = input('Ingrese el id del usuario: ')
#rol_id = input('Ingrese el id del rol: ')

token = ACCESS_TOKEN
desmatricular_usuario(api_url, token=ACCESS_TOKEN)