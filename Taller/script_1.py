import os
import requests
from colorama import Fore, Back, Style, init

init(autoreset=True)  # reset the previous color and style after each line
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
api_url = f'https://poli.instructure.com/api/v1/'

def settings_course(url='', payload={}, token=''):
    headers = {
        "Authorization": f"Bearer {token}"
    }
    r = requests.put(url, headers=headers, data=payload)
    if r.status_code == 200:
        color = Fore.GREEN
    else:
        color = Fore.RED
    print(color + f'{r.status_code} >> {r.reason}')
    if r.status_code == 200:
       return r
    else:
        return None
    
course_list = [62739, 39217]
token=ACCESS_TOKEN
payload = {
    "filter_speed_grader_by_student_group": True,
}
n, m = 1, len(course_list)
for course_id in course_list:
    print(f'[{n}/{m}]: Ingresando a {course_id}')
    url = f'{api_url}courses/{course_id}/settings' 
    r = settings_course(url, payload, token=ACCESS_TOKEN)
    if r.status_code == 200:
        response = r.json()
        print(f'\t filter_speed_grader: {response["filter_speed_grader_by_student_group"]}')
    else: 
        print('Error')
    n =+ 1