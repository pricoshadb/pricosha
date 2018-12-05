import hashlib
import pymysql

conn = pymysql.connect(host='localhost',
                       user='user',
                       password='pricosha',
                       db='pricosha')


# Helper functions

# Checks if user can see content item
def can_see(email, item_id):
    c = conn.cursor(pymysql.cursors.DictCursor)
    sql = '''select count(*) AS count from ContentItem 
                NATURAL JOIN Share 
                NATURAL JOIN Belong 
                WHERE email_member=%s AND item_id=%s'''
    c.execute(sql, (email, item_id))
    result = c.fetchone()
    return result['count'] > 0


# 1. Gets public content from past 24 hours
#    Also paginates results
def get_public_content(page=1, results_per_page=10):
    # Initialize our cursor with DictCursor to get results back as dictionary
    c = conn.cursor(pymysql.cursors.DictCursor)

    # Get content items that are public AND from the past 24 hours

    sql = '''SELECT * FROM ContentItem 
              WHERE is_pub=1 AND post_time >= NOW() - INTERVAL 1 DAY 
              ORDER BY post_time DESC LIMIT %s,%s'''
    start = (page - 1) * results_per_page
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
        if content_item['file_path'] is None:
            formatted_data['file_path'] = 'https://pricosha.drew.hu/img/none.jpg'
        content_items.append(formatted_data)
    return content_items


# 2. Gets user login info
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


# 3. Get content shared with email
def get_shared_content(email, page=1, results_per_page=10):
    c = conn.cursor(pymysql.cursors.DictCursor)
    sql = '''select * from ContentItem 
                NATURAL JOIN Share 
                NATURAL JOIN Belong WHERE email_member=%s
                ORDER BY post_time DESC LIMIT %s,%s'''
    start = (page - 1) * results_per_page
    c.execute(sql, (email, start, results_per_page))
    results = c.fetchall()
    return results


# 4. Manage tags
# 4a. Get proposed tags
def get_proposed_tags(email):
    c = conn.cursor(pymysql.cursors.DictCursor)
    sql = '''SELECT * FROM Tag WHERE email_tagged=%s AND status=False'''
    c.execute(sql, (email,))
    tags = c.fetchall()
    return tags


def modify_proposed_tag(email_tagger, email_tagged, item_id, decision):
    c = conn.cursor(pymysql.cursors.DictCursor)
    if decision == 'no decision':
        return "No decision made"
    if decision == 'accept':
        sql = '''UPDATE Tag SET status=True WHERE email_tagger=%s AND email_tagged=%s AND item_id=%s'''
        c.execute(sql, (email_tagger, email_tagged, item_id))
        conn.commit()


# 5. Post a content item
def create_content_item(email, item_name, is_pub, file_path):
    c = conn.cursor()
    sql = '''INSERT INTO 
              ContentItem(email, post_time, item_name, is_pub, file_path)
              VALUES (%s,NOW(),%s,%s,%s)'''
    c.execute(sql, (email, item_name, is_pub, file_path))
    conn.commit()


# 6. Tag a content item
def tag_item(current_user, tagee_email, item_id):
    c = conn.cursor(pymysql.cursors.DictCursor)

    # Check if user has access to item
    if not can_see(current_user, item_id):
        return 'User does not have access to this item'
    confirmed = False
    # Check if user is self-tagging
    if current_user == tagee_email:
        confirmed = True

    sql = '''INSERT INTO Tag(email_tagger, email_tagged, item_id, tag_time, status)
              VALUES (%s,%s,%s,NOW(),%s)'''
    c.execute(sql, (current_user, tagee_email, item_id, confirmed))
    conn.commit()


# 7. Add friend
def add_friend(owner_email, fg_name, friend_fname, friend_lname):
    c = conn.cursor(pymysql.cursors.DictCursor)
    sql = '''SELECT * FROM Person WHERE first_name=%s AND last_name=%s'''
    c.execute(sql, (friend_fname, friend_lname))
    person = c.fetchall()

    # Check if person exists
    if len(person) == 0:
        return 'Person does not exist'

    # Check if more than one person exists
    if len(person) > 1:
        return 'More than one person exists with name'

    # Check if friend already exists in Friend Group
    sql = '''SELECT COUNT(*) as count FROM Person INNER JOIN Belong 
              ON Person.email = Belong.email_member 
              WHERE first_name=%s AND last_name=%s AND fg_name = %s;'''

    c.execute(sql, (friend_fname, friend_lname, fg_name))
    r = c.fetchone()
    if r['count'] > 0:
        return 'Person already exists in FriendGroup'

    # Add friend to friend group
    sql = '''INSERT INTO Belong(email_owner, email_member, fg_name)
              VALUES (%s,%s,%s)'''
    c.execute(sql, (owner_email, person[0]['email'], fg_name))
    conn.commit()
    return 'Successfully added friend'


# Optional feature 3: Saved posts. Returns post saved by user
def get_saved_posts(email, page, results_per_page):
    c = conn.cursor(pymysql.cursors.DictCursor)
    sql = '''SELECT * FROM Saved INNER JOIN ContentItem 
              ON Saved.item_id = ContentItem.item_id 
              WHERE Saved.email=%s
              ORDER BY post_time DESC LIMIT %s,%s'''
    start = (page - 1) * results_per_page
    c.execute(sql, (email, start, results_per_page))
    saved_posts = c.fetchall()
    return saved_posts
