import hashlib
import pymysql
from helpers.util import response

conn = pymysql.connect(host='localhost',
                       user='user',
                       password='pricosha',
                       db='pricosha')


# Helper functions

# Checks if user can see content item, bc item is public
def can_see(email, item_id):
    c = conn.cursor(pymysql.cursors.DictCursor)
    sql = '''select count(*) AS cnt from ContentItem 
                NATURAL JOIN Share 
                NATURAL JOIN Belong 
                WHERE (email_member=%s OR is_pub=True) AND item_id=%s'''
    c.execute(sql, (email, item_id))
    result = c.fetchone()
    return result['cnt'] > 0



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

def get_post(item_id):
    c = conn.cursor(pymysql.cursors.DictCursor)

    sql = '''SELECT * FROM ContentItem 
              WHERE is_pub=1 AND item_id=%s'''
    c.execute(sql, (item_id,))
    result = c.fetchall()
    return result

# 2. Gets user login info
def get_login(email, password):
    # Initialize our cursor with DictCursor to get results back as dictionary
    c = conn.cursor(pymysql.cursors.DictCursor)

    # Check if username and password hash exist in our database
    sql = '''SELECT * FROM Person WHERE email=%s'''
    c.execute(sql, (email,))
    person = c.fetchone()

    if person is None:
        return {'success': False}

    # Check password and log user in if success
    if person['password_hash'] == hashlib.sha256(password.encode('utf8')).hexdigest():
        # Log the user in and set session variables
        user_data = {
            'email': email,
            'first_name': person['first_name'],
            'last_name': person['last_name'],
            'avatar': person['avatar']
        }
        return {'success': True, 'response': user_data}
    else:
        return {'success': False}


def register(email, password, first_name, last_name):
    c = conn.cursor(pymysql.cursors.DictCursor)

    # Check if user with email already exists
    sql = '''SELECT COUNT(*) AS cnt FROM Person WHERE email=%s'''
    c.execute(sql, (email,))
    user_count = c.fetchone()
    if user_count['cnt'] > 0:
        return {'success': False, 'response': 'User with email already exists'}

    # Create new user
    sql = '''INSERT INTO Person(email, password_hash, first_name, last_name)
              VALUES (%s,SHA2(%s, 256), %s, %s)'''
    c.execute(sql, (email, password, first_name, last_name))
    conn.commit()
    return {'success': True, 'response': f'Successfully registered user {first_name} {last_name}'}


def reset_password(email, old_password, new_password):
    c = conn.cursor(pymysql.cursors.DictCursor)
    sql = '''UPDATE Person SET password_hash=SHA2(%s,256) 
              WHERE password_hash=SHA2(%s,256) AND email=%s'''
    c.execute(sql, (new_password, old_password, email))
    conn.commit()
    return ( f'Successfully changed password for {email}')


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
def get_proposed_tags(email, page=1, results_per_page=10):
    c = conn.cursor(pymysql.cursors.DictCursor)
    sql = '''SELECT * FROM Tag WHERE email_tagged=%s AND status=False
              ORDER BY tag_time DESC LIMIT %s,%s'''
    start = (page - 1) * results_per_page
    c.execute(sql, (email, start, results_per_page))
    tags = c.fetchall()
    return tags


def modify_proposed_tag(email_tagger, email_tagged, item_id, decision):
    c = conn.cursor(pymysql.cursors.DictCursor)
    if decision == 'no decision':
        return "No decision made"
    elif decision == 'accept':
        sql = '''UPDATE Tag SET status=1 WHERE email_tagger=%s AND email_tagged=%s AND item_id=%s'''
        c.execute(sql, (email_tagger, email_tagged, item_id))
        conn.commit()
        return
    elif decision == 'decline':
        sql = '''DELETE FROM Tag WHERE email_tagger=%s AND email_tagged=%s AND item_id=%s'''
        c.execute(sql, (email_tagger, email_tagged, item_id))
        conn.commit()


# 5. Post a content item
def create_content_item(email, item_name, is_pub, file_path):
    c = conn.cursor(pymysql.cursors.DictCursor)
    sql = '''INSERT INTO 
              ContentItem(email, post_time, item_name, is_pub, file_path)
              VALUES (%s,NOW(),%s,%s,%s)'''
    c.execute(sql, (email, item_name, is_pub, file_path))
    sql = '''SELECT * FROM ContentItem WHERE item_id=(SELECT LAST_INSERT_ID())'''
    c.execute(sql)
    last_insert = c.fetchone()
    conn.commit()
    return last_insert


# 6. Tag a content item
def tag_item(tagger_email, tagee_email, item_id):
    c = conn.cursor(pymysql.cursors.DictCursor)

    # Check if users have access to item
    if not can_see(tagger_email, item_id):
        return 'Tagger does not have access to this item'

    if not can_see(tagee_email, item_id):
        return 'Tagee does not have access to this item'

    confirmed = False

    # Check if user is self-tagging
    if tagger_email == tagee_email:
        confirmed = True

    # Check if user is already tagged
    sql = '''SELECT COUNT(*) AS cnt FROM Tag 
              WHERE email_tagger=%s AND email_tagged=%s AND item_id=%s'''
    c.execute(sql, (tagger_email, tagee_email, item_id))
    result = c.fetchone()
    if result['cnt'] > 0:
        return 'User is already tagged'

    sql = '''INSERT INTO Tag(email_tagger, email_tagged, item_id, tag_time, status)
              VALUES (%s,%s,%s,NOW(),%s)'''
    c.execute(sql, (tagger_email, tagee_email, item_id, confirmed))
    conn.commit()


# 7. Add friend
def add_member(owner_email, fg_name, friend_fname, friend_lname):
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

def remove_member(email_owner, email_member, fg_name):
    c = conn.cursor(pymysql.cursors.DictCursor)
    sql = '''DELETE FROM Belong WHERE email_owner=%s AND email_member=%s AND fg_name=%s'''
    c.execute(sql, (email_owner, email_member, fg_name))
    conn.commit()
    return (True, 'Removed friend from fg')

def create_group(email_owner, fg_name, description):
    c = conn.cursor(pymysql.cursors.DictCursor)
    sql = '''INSERT INTO FriendGroup(fg_name, email, description)
              VALUES (%s,%s,%s)'''
    c.execute(sql, (fg_name, email_owner, description))
    conn.commit()

def remove_group(email_owner, fg_name):
    c = conn.cursor(pymysql.cursors.DictCursor)
    sql = '''DELETE FROM FriendGroup WHERE fg_name=%s and email=%s'''
    c.execute(sql, (fg_name, email_owner))
    conn.commit()

def get_groups(email_owner):
    c = conn.cursor(pymysql.cursors.DictCursor)
    sql = '''SELECT fg_name, description, email_member FROM FriendGroup JOIN Belong 
            ON email=email_owner AND FriendGroup.fg_name=Belong.fg_name 
            where email=%s GROUP BY fg_name'''
    c.execute(sql, (email_owner,))
    g = c.fetchall()
    return g

# Optional feature 2: Profile pages
def get_profile_info(email):
    c = conn.cursor(pymysql.cursors.DictCursor)
    sql = '''SELECT avatar, bio FROM Person WHERE email=%s'''
    c.execute(sql, (email,))
    profile = c.fetchone()
    return profile

def set_profile_bio(email, bio):
    c = conn.cursor(pymysql.cursors.DictCursor)
    sql = '''UPDATE Person SET bio=%s WHERE email=%s'''
    c.execute(sql, (bio, email))
    conn.commit()
    return True

def set_profile_avatar(email, avatar):
    c = conn.cursor(pymysql.cursors.DictCursor)
    sql = '''UPDATE Person SET avatar=%s WHERE email=%s'''
    c.execute(sql, (avatar, email))
    conn.commit()
    return True

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


def save_post(email, item_id):
    if not can_see(email, item_id):
        return 'User is not allowed to save this content'
    c = conn.cursor(pymysql.cursors.DictCursor)
    sql = '''INSERT INTO Saved(email, save_time, item_id)
              VALUES (%s,NOW(),%s)'''
    c.execute(sql, (email, item_id))
    conn.commit()


def unsave_post(email, item_id):
    c = conn.cursor(pymysql.cursors.DictCursor)
    sql = '''DELETE FROM Saved WHERE email=%s AND item_id=%s'''
    c.execute(sql, (email, item_id))
    conn.commit()


# Optional feature 6. Post comments
def post_comment(email, item_id, comment):
    if not can_see(email, item_id):
        return 'User is not allowed to comment on this content'
    c = conn.cursor(pymysql.cursors.DictCursor)
    sql = '''INSERT INTO Comments(item_id, email, post_time, content) 
              VALUES (%s, %s, NOW(), %s)'''
    c.execute(sql, (item_id, email, comment))
    conn.commit()
    return True


def get_comments(email, item_id):
    if not can_see(email, item_id):
        return 'User is not allowed to see this post'
    c = conn.cursor(pymysql.cursors.DictCursor)
    sql = '''SELECT * FROM Comments WHERE item_id=%s'''
    c.execute(sql, (item_id,))
    comments = c.fetchall()
    return comments


def get_friends(email):
    c = conn.cursor(pymysql.cursors.DictCursor)
    sql = '''SELECT email_friend FROM Friends WHERE email=%s'''
    c.execute(sql, (email,))
    return c.fetchall()

def add_friend(email, email_friend):
    c = conn.cursor(pymysql.cursors.DictCursor)
    sql = '''INSERT INTO Friends(email, email_friend) 
              VALUES (%s, %s)'''
    c.execute(sql, (email, email_friend))
    conn.commit()
    return (True, 'Added friend.')


def remove_friend(email, email_friend):
    c = conn.cursor(pymysql.cursors.DictCursor)
    sql = '''DELETE FROM Friends WHERE email=%s AND email_friend=%s'''
    c.execute(sql, (email, email_friend))
    conn.commit()
