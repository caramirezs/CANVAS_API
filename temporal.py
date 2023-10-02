import os
import json
from lib.main_functions import get_function


# se debe agregar el ACCESS_TOKEN de CANAS como variable de entorno de usuario
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
api_url = f"https://poli.instructure.com/api/v1"
course_id = 62739
payload = {
    'include': 'sections'
}

r = get_function(url=f"{api_url}/courses/{course_id}",
                           payload=payload,
                           token=ACCESS_TOKEN,
                           verbose=False)
info_course = r.json()
print(json.dumps(info_course, indent=2))