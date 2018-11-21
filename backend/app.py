from flask import Flask, request
import pymysql
from helpers import *
import hashlib

app = Flask(__name__)

app.secret_key = 'super secret key!98nu9f8u2f'

conn = pymysql.connect(host='localhost',
                       user='user',
                       password='haha',
                       db='pricosha')



@app.route('/login', methods=['POST'])
def login():
    # Info we get from the request
    email = request.form['email']
    password = request.form['password']

    # Check the password hash
    c = conn.cursor()
    password_hash = hashlib.sha256(password.encode('utf8')).hexdigest()
    sql = '''SELECT count(*) FROM Person WHERE email=%s AND password_hash=%s'''
    c.execute(sql, (email, password_hash))
    result = c.fetchone()
    # Does not exist
    if len(result)>0:
        return 'login success'
    else:
        return 'login failed'

