import os
import requests
import json

ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
api_url = f'https://poli.instructure.com/api/v1/'
id_course = 12345
url = f'{api_url}courses/{id_course}'
headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}
payload = {
        "course[term_id]": 1
    }


r = requests.put(url=url, headers=headers, data=payload)


if r.status_code == 200:
    response = r.json()
    print(json.dumps(response, indent=2))
else:
    print(f'{r.status_code} >> {r.reason}')