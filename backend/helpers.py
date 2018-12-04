import hashlib
import pymysql

conn = pymysql.connect(host='localhost',
                        user='user',
                        password='pricosha',
                        db='pricosha')


# 1. Gets public content from past 24 hours
#    Also paginates results
def get_public_content(page=1, results_per_page=10):
    # Initialize our cursor with DictCursor to get results back as dictionary
    c = conn.cursor(pymysql.cursors.DictCursor)

    # Get content items that are public AND from the past 24 hours

    sql = '''SELECT * FROM ContentItem 
              WHERE is_pub=1 AND post_time >= NOW() - INTERVAL 1 DAY 
              ORDER BY post_time DESC LIMIT %s,%s'''
    start = (page-1)*results_per_page
    c.execute(sql, (start, results_per_page))
    result = c.fetchall()

    # Format results
    content_items = []
    for content_item in result:
        formatted_data = {
            'item_id': content_item['item_id'],
            'email': content_item['email'],
            'post_time': content_item['post_time'],
            'item_name': content_item['item_name'],
            'file_path': '%simg/%s' % ('https://pricosha.drew.hu/', content_item['file_path']),
            'tagged': ['temp', 'vals']
            # TODO: tagged people
        }
        content_items.append(formatted_data)
    return content_items


# 2. Logs user in

def get_login(email, password):
    # Initialize our cursor with DictCursor to get results back as dictionary
    c = conn.cursor(pymysql.cursors.DictCursor)

    # Check if username and password hash exist in our database
    sql = '''SELECT first_name, last_name, password_hash FROM Person WHERE email=%s'''
    c.execute(sql, (email,))
    person = c.fetchone()

    # Check that person exists
    if person is None:
        return False

    # Check password and log user in if success
    if person['password_hash'] == hashlib.sha256(password.encode('utf8')).hexdigest():
        # Log the user in and set session variables
        return {
            'email': email,
            'first_name': person['first_name'],
            'last_name': person['last_name'],
            'avatar': person['avatar']
        }
    else:
        return False


def check_pw(password, password_hash):
    return password_hash == hashlib.sha256(password.encode('utf8')).hexdigest()


# Hash password with sha256 and store as hex string
def hash_pw(password):
    return hashlib.sha256(password.encode('utf8')).hexdigest()


def create_content_item(email, item_name, is_pub, file_path):
    c = conn.cursor()
    sql = '''INSERT INTO 
              ContentItem(email, post_time, item_name, is_pub, file_path)
              VALUES (%s,NOW(),%s,%s,%s)'''
    c.execute(sql, (email, item_name, is_pub, file_path))
    conn.commit()