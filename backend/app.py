from flask import Flask, request, jsonify
from flask_cors import CORS
import pymysql
from helpers import *
import hashlib

# Initialize Flask app
app = Flask(__name__)

# Set secret key for sessions
app.secret_key = 'super secret key!98nu9f8u2f'

# Allow all clients to access our api
CORS(app, resources={r"/*": {"origins": '*'}})

# MySQL connection info
conn = pymysql.connect(host='localhost',
                       user='user',
                       password='haha',
                       db='pricosha')


# Login route - POST email and password
@app.route('/login/', methods=['POST'])
def login():
    # Get info from request
    email = request.form['email']
    password = request.form['password']

    # Check the password hash
    c = conn.cursor()

    # Hash the password
    password_hash = hashlib.sha256(password.encode('utf8')).hexdigest()

    # See if username and password hash exist in our database
    sql = '''SELECT count(*) FROM Person WHERE email=%s AND password_hash=%s'''
    c.execute(sql, (email, password_hash))
    result = c.fetchone()

    # If the length of the result is 0, then the Person does not exist or
    # the password is incorrect so we return 'login failed' as JSON.
    if len(result) > 0:
        return jsonify('login success')
    else:
        return jsonify('login failed')


# Gets public content
@app.route('/public_content/')
def public_content():
    # Get content items that are public AND from the past 24 hours
    c = conn.cursor()
    sql = '''SELECT * FROM ContentItem WHERE is_pub=1 AND post_time >= NOW() - INTERVAL 1 DAY'''
    c.execute(sql)
    result = c.fetchall()

    # Format results
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
