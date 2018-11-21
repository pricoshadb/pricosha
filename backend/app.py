from flask import Flask, session, request, jsonify
from flask_cors import CORS
import pymysql
from helpers import check_pw
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
@app.route('/login/', methods=['GET', 'POST'])
def login():

    # Get info from request
    email = request.form['email']
    password = request.form['password']

    # See if username and password hash exist in our database
    c = conn.cursor()
    sql = '''SELECT first_name, last_name, password_hash FROM Person WHERE email=%s'''
    c.execute(sql, (email,))
    result = c.fetchone()
    password_hash = result[2]

    # Check password and log user in if success
    if check_pw(password, password_hash):
        # Log the user in and set session variables
        session['email'] = email
        session['first_name'], session['last_name'] = result[0], result[1]
        return jsonify('successfully logged in %s %s' % (session['first_name'], session['last_name']))
    else:
        return jsonify('login failed')


@app.route('/logout/')
def logout():
    # remove the username from the session if it's there
    session.pop('email', None)
    return jsonify('logged out')


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
