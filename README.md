# PriCoSha
CS 3083 Intro to Databases Project  

Maxwell Reddy **mcr517**  
Lucas Pollice **lp1935**  
Khoa Nguyen   **kdn263**  
Andrew Hu     **ah4358**  

## Live demo: <a href='https://pricosha.drew.hu' target="_blank">https://pricosha.drew.hu</a>
## API: <a href='https://pricoshaapi.drew.hu' target='_blank'>https://pricoshaapi.drew.hu</a>
## Todo
* Login
* Post content items
* view content items that are public or that are shared with FriendGroups to which they belong
* propose to tag content items with e-mails of other users, provided the content items are visible to both the user (the tagger) and the person being tagged (the taggee)
* manage tag proposals

## Test accounds
| email     | name | password |
| ------------- | ----- | ------------- |
| AA@nyu.edu    |  Ann Anderson | AA |
|AA2@nyu.edu|Ann Anderson|AA2|



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
