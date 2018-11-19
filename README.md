# pricosha
CS 3083 Intro to Databases Project

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
sudo apt-get install git python python-pip -y
```

## Usage
Using Flask for webapp and Flask-MySQL for sql
```
git clone https://github.com/pricoshadb/pricosha.git
cd pricosha/
pip install flask flask-mysql
export FLASK_APP=app.py
flask run
```
