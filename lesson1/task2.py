import requests
from pprint import pprint
import json
main_link = 'https://api.vk.com/method/groups.get'
params = {
    'user_id' : '21092174',
    'v' : '5.124',
    'access_token' : '5f4c6a135b63e64a8ee36ed5b841a',
    'extendet' : '1'
}
response = requests.get(main_link,params=params,)
j_data = response.json()
pprint(j_data)
with open('response.json', 'w') as f:
    json.dump(response.json(), f)
