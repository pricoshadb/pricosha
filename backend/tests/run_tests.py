import requests
import json

base_url = 'https://pricoshaapi.drew.hu'

# create session
s = requests.session()
s1 = requests.session()
# # 1. Test public content
# print('Use case 1: View public content')
# print('GET /public_content')
# public_content = s.get(base_url + '/public_content')
# print(json.dumps(public_content.json()[:2], indent=2))
#
# input('Press enter to continue')

# 2. Test registration/login
print('Use case 2: Login')
print('POST /register')
reg_info = {'email': 'test@nyu.edu',
            'password': 'test',
            'first_name': 'test',
            'last_name': 'user'}
r = s.post(base_url + '/register', data=reg_info)
print(r.status_code, r.text)

# Create some mock data
reg_info_1 = {
    'email': 'test1@nyu.edu',
    'password': 'test1',
    'first_name': 'test1',
    'last_name': 'user'
}
s1.post(base_url + '/register', data=reg_info_1)

print('GET /login')
login_info = {
    'auth': {
        'email': 'test@nyu.edu',
        'password': 'test'
    }
}
r = s.post(base_url + '/login', json=login_info)
print(r.status_code, r.text)

login_info_1 = {
    'auth': {
        'email': 'test1@nyu.edu',
        'password': 'test1'
    }
}
s1.post(base_url + '/login', json=login_info_1)

input('Press enter to continue')


# Create a friend group, owned by test and include test1


# 5. Create new post with image
post_info = {
    'item_name': 'Test post from test user',
    'is_pub': 1,
}
files = {'file': ('test_image.jpg', open('test_image.jpg', 'rb'))}
r = s.post(base_url + '/post/create', data=post_info,files=files)
print(r.status_code, r.text)
input('Press enter to continue')

# 3. Test shared content
print('Use case 3: View shared content')
print('GET /posts/shared')
shared_content = s.get(base_url + '/get_shared_content')
print(json.dumps(shared_content.json()[:2], indent=2))
