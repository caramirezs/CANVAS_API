import os
import json
from lib.main_functions import get_function


# se debe agregar el ACCESS_TOKEN de CANAS como variable de entorno de usuario
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')

api_url = f'https://poli.instructure.com/api/v1/'
course_id = 48209
url = api_url+f'courses/{course_id}'
headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}
payload = {
    'include': 'sections'
}

response = get_function(url, token=ACCESS_TOKEN)

print(json.dumps(response.json(), indent=2))