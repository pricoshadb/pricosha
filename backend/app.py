from flask import Flask, session, request, jsonify
from flask_cors import CORS
import pymysql
from helpers import check_pw

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

    # Initialize our cursor with DictCursor to get results back as dictionary
    c = conn.cursor(pymysql.cursors.DictCursor)

    # Check if username and password hash exist in our database
    sql = '''SELECT first_name, last_name, password_hash FROM Person WHERE email=%s'''
    c.execute(sql, (email,))
    person = c.fetchone()

    # Check that person exists
    if person is None:
        return jsonify('login failed')

    # Check password and log user in if success
    if check_pw(password, person['password_hash']):
        # Log the user in and set session variables
        session['email'] = email
        session['first_name'], session['last_name'] = person['first_name'], person['last_name']
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
    # Initialize our cursor with DictCursor to get results back as dictionary
    c = conn.cursor(pymysql.cursors.DictCursor)

    # Get content items that are public AND from the past 24 hours
    sql = '''SELECT * FROM ContentItem WHERE is_pub=1 AND post_time >= NOW() - INTERVAL 1 DAY'''
    c.execute(sql)
    result = c.fetchall()

    # Format results
    content_items = []
    for content_item in result:
        formatted_data = {
            'item_id': content_item['item_id'],
            'email': content_item['email'],
            'post_time': content_item['post_time'],
            'item_name': content_item['item_name'],
            'file_path': content_item['file_path'],
        }
        content_items.append(formatted_data)
    return jsonify(content_items)
