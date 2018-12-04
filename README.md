# pricosha
CS 3083 Intro to Databases Project


## Live demo: <a href='https://pricosha.drew.hu' target="_blank">https://pricosha.drew.hu</a>
## API: <a href='https://api.pricosha.drew.hu' target='_blank'>https://api.pricosha.drew.hu</a>
## Todo
* Login
* Post content items
* view content items that are public or that are shared with FriendGroups to which they belong
* propose to tag content items with e-mails of other users, provided the content items are visible to both the user (the tagger) and the person being tagged (the taggee)
* manage tag proposals

## Users
| user_id       | user_name     | email | password_hash |
| ------------- | ------------- | ----- | ------------- |
| 1     | bill       |  bill@example.com | f0e4c2f76c... |


## Install dependencies
```
sudo apt-get update
sudo apt-get install git python3 python3-pip -y
```

## Usage
Using Flask for webapp and Flask-MySQL for sql
```
git clone https://github.com/pricoshadb/pricosha.git
cd pricosha/
pip install flask pymysql 
export FLASK_APP=app.py
flask run
```

## deploy to gunicorn
```
pip install gunicorn
```
