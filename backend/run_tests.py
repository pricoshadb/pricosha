import requests
import json

base_url = 'https://pricoshaapi.drew.hu'
login_info = {
    'email': 'AA@nyu.edu',
    'password': 'AA'
}

# create session
s = requests.session()

# 1. Test public content
print('Use case 1: View public content')
print('GET /public_content')
public_content = s.get(base_url + '/public_content')
print(json.dumps(public_content.json()[:2], indent=2))

input('Press enter to continue')

# 2. Test login
print('Use case 2: Login')
print('GET /login')
login = s.post(base_url + '/login', data=login_info)
print(login.text)

input('Press enter to continue')

# 3. Test shared content
print('Use case 3: View shared content')
print('GET /get_shared_content')
shared_content = s.get(base_url + '/get_shared_content')
print(json.dumps(shared_content.json()[:2],indent=2))