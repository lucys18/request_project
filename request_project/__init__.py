import requests
import pprint
r = requests.get('https://api.github.com/')
print(r.status_code)
json_response = r.json()
pprint.pprint(json_response)
