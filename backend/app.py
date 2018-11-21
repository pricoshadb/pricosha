from flask import Flask, request, jsonify
import pymysql
from helpers import *
import hashlib

app = Flask(__name__)

app.secret_key = 'super secret key!98nu9f8u2f'

conn = pymysql.connect(host='localhost',
                       user='user',
                       password='haha',
                       db='pricosha')


@app.route('/login/', methods=['POST'])
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

    # If the length of the result is 0, then the Person does not exist or
    # the password is incorrect so we return 'login failed' as JSON.
    #
    if len(result) > 0:
        return jsonify('login success')
    else:
        return jsonify('login failed')


@app.route('/public_content/')
def public_content():
    c = conn.cursor()
    sql = '''SELECT * FROM ContentItem WHERE is_pub=1 AND post_time >= NOW() - INTERVAL 1 DAY'''
    c.execute(sql)
    result = c.fetchall()
    content_items = []
    for content_item in result:
        formatted_data = {
            'item_id': content_item[0],
            'email': content_item[1],
            'post_time': content_item[2],
            'item_name': content_item[3],
            'file_path': content_item[5],
        }
        content_items.append(formatted_data)
    return jsonify(content_items)
