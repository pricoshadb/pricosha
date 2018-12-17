import hashlib
import pymysql
import flask


def connect_db():
    return pymysql.connect(host='localhost',
                             user='user',
                             password='pricosha',
                             db='pricosha',
                             charset="utf8mb4",
                             cursorclass=pymysql.cursors.DictCursor)



# Helper functions

# Checks if user can see content item, bc item is public
def can_see(email, item_id):
    cursor = flask.g.connection.cursor()
    sql = '''select count(*) AS cnt from ContentItem 
                LEFT JOIN Share USING(email, item_id)
                LEFT JOIN Belong ON(email_owner=email and Share.fg_name=Belong.fg_name)
                WHERE (email_member=%s OR email_owner=%s OR is_pub=1) AND item_id=%s'''
    cursor.execute(sql, (email,email, item_id))
    result = cursor.fetchone()
    
    return result['cnt'] > 0



# 1. Gets public content from past 24 hours
#    Also paginates results
def get_public_content(page=1, results_per_page=10):
    # Initialize our cursor with DictCursor to get results back as dictionary
    cursor = flask.g.connection.cursor()

    # Get content items that are public AND from the past 24 hours

    sql = '''SELECT * FROM ContentItem 
              WHERE is_pub=1 AND post_time >= NOW() - INTERVAL 1 DAY 
              ORDER BY post_time DESC LIMIT %s,%s'''
    start = (page - 1) * results_per_page
    cursor.execute(sql, (start, results_per_page))
    result = cursor.fetchall()

    # Format results
    content_items = []
    for content_item in result:
        formatted_data = {
            'item_id': content_item['item_id'],
            'email': content_item['email'],
            'post_time': content_item['post_time'],
            'item_name': content_item['item_name'],
            # FIXME: file images
            'file_path': '%simg/%s' % ('', content_item['file_path']),
            'tagged': []
            # TODO: tagged people
        }
        if content_item['file_path'] is None:
            formatted_data['file_path'] = '' # backup
        content_items.append(formatted_data)
    
    return content_items

def get_post(item_id):
    cursor = flask.g.connection.cursor()

    sql = '''SELECT * FROM ContentItem 
              WHERE is_pub=1 AND item_id=%s'''
    cursor.execute(sql, (item_id,))
    result = cursor.fetchall()
    
    return result

# 2. Gets user login info
def get_login(email, password):
    # Initialize our cursor with DictCursor to get results back as dictionary
    cursor = flask.g.connection.cursor()

    # Check if username and password hash exist in our database
    sql = '''SELECT * FROM Person WHERE email=%s'''
    cursor.execute(sql, (email,))
    person = cursor.fetchone()
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
    cursor = flask.g.connection.cursor()

    # Check if user with email already exists
    sql = '''SELECT COUNT(*) AS cnt FROM Person WHERE email=%s'''
    cursor.execute(sql, (email,))
    user_count = cursor.fetchone()
    if user_count['cnt'] > 0:
        
        return {'success': False, 'response': 'User with email already exists'}

    # Create new user
    sql = '''INSERT INTO Person(email, password_hash, first_name, last_name)
              VALUES (%s,SHA2(%s, 256), %s, %s)'''
    cursor.execute(sql, (email, password, first_name, last_name))
    flask.g.connection.commit()
    
    return {'success': True, 'response': f'Successfully registered user {first_name} {last_name}'}


def reset_password(email, old_password, new_password):
    cursor = flask.g.connection.cursor()
    sql = '''UPDATE Person SET password_hash=SHA2(%s,256) 
              WHERE password_hash=SHA2(%s,256) AND email=%s'''
    cursor.execute(sql, (new_password, old_password, email))
    flask.g.connection.commit()
    
    return ( f'Successfully changed password for {email}')


# 3. Get content shared with email
def get_shared_content(email, page=1, results_per_page=10):
    cursor = flask.g.connection.cursor()
    sql = '''select * from ContentItem 
                NATURAL JOIN Share 
                NATURAL JOIN Belong WHERE email_member=%s
                ORDER BY post_time DESC LIMIT %s,%s'''
    start = (page - 1) * results_per_page
    cursor.execute(sql, (email, start, results_per_page))
    results = cursor.fetchall()
    
    return results


# 4. Manage tags
# 4a. Get proposed tags
def get_proposed_tags(email, page=1, results_per_page=10):
    cursor = flask.g.connection.cursor()
    sql = '''SELECT * FROM Tag WHERE email_tagged=%s AND status=False
              ORDER BY tag_time DESC LIMIT %s,%s'''
    start = (page - 1) * results_per_page
    cursor.execute(sql, (email, start, results_per_page))
    tags = cursor.fetchall()
    
    return tags


def modify_proposed_tag(email_tagger, email_tagged, item_id, decision):
    cursor = flask.g.connection.cursor()
    if decision == 'no decision':
        
        return "No decision made"
    elif decision == 'accept':
        sql = '''UPDATE Tag SET status=1 WHERE email_tagger=%s AND email_tagged=%s AND item_id=%s'''
        cursor.execute(sql, (email_tagger, email_tagged, item_id))
        flask.g.connection.commit()
        
        return
    elif decision == 'decline':
        sql = '''DELETE FROM Tag WHERE email_tagger=%s AND email_tagged=%s AND item_id=%s'''
        cursor.execute(sql, (email_tagger, email_tagged, item_id))
        flask.g.connection.commit()
        


# 5. Post a content item
def create_content_item(email, item_name, is_pub, file_path):
    cursor = flask.g.connection.cursor()
    sql = '''INSERT INTO 
              ContentItem(email, post_time, item_name, is_pub, file_path)
              VALUES (%s,NOW(),%s,%s,%s)'''
    cursor.execute(sql, (email, item_name, is_pub, file_path))
    sql = '''SELECT * FROM ContentItem WHERE item_id=(SELECT LAST_INSERT_ID())'''
    cursor.execute(sql)
    last_insert = cursor.fetchone()
    flask.g.connection.commit()
    
    return last_insert


# 6. Tag a content item
def tag_item(tagger_email, tagee_email, item_id):

    # Check if users have access to item
    if not can_see(tagger_email, item_id):
        return 'Tagger does not have access to this item'

    if not can_see(tagee_email, item_id):
        return 'Tagee does not have access to this item'

    confirmed = False

    # Check if user is self-tagging
    if tagger_email == tagee_email:
        confirmed = True

    cursor = flask.g.connection.cursor()
    # Check if user exists
    sql = '''SELECT COUNT(*) AS cnt FROM Person 
              WHERE email=%s'''
    cursor.execute(sql, (tagee_email,))
    result = cursor.fetchone()
    if result['cnt'] == 0:
        return 'User does not exist'


    # Check if user is already tagged
    sql = '''SELECT COUNT(*) AS cnt FROM Tag 
              WHERE email_tagger=%s AND email_tagged=%s AND item_id=%s'''
    cursor.execute(sql, (tagger_email, tagee_email, item_id))
    result = cursor.fetchone()
    if result['cnt'] > 0:
        return 'User is already tagged'

    sql = '''INSERT INTO Tag(email_tagger, email_tagged, item_id, tag_time, status)
              VALUES (%s,%s,%s,NOW(),%s)'''
    cursor.execute(sql, (tagger_email, tagee_email, item_id, confirmed))
    flask.g.connection.commit()
    


# 7. Add friend
def add_member(email_owner, email_member, fg_name):
    cursor = flask.g.connection.cursor()
    # sql = '''SELECT * FROM Person WHERE first_name=%s AND last_name=%s'''
    # cursor.execute(sql, (friend_fname, friend_lname))
    # person = cursor.fetchall()

    # Check if person exists
    # if len(person) == 0:
    #
    #     return 'Person does not exist'
    #
    # # Check if more than one person exists
    # if len(person) > 1:
    #
    #     return 'More than one person exists with name'

    # Check if friend already exists in Friend Group
    sql = '''SELECT COUNT(*) as count FROM Belong  
              WHERE email_member=%s AND fg_name = %s;'''

    cursor.execute(sql, (email_member, fg_name))
    r = cursor.fetchone()
    if r['count'] > 0:
        
        return False, 'Person already exists in FriendGroup'

    # Add friend to friend group
    sql = '''INSERT INTO Belong(email_owner, email_member, fg_name)
              VALUES (%s,%s,%s)'''
    cursor.execute(sql, (email_owner, email_member, fg_name))
    flask.g.connection.commit()
    
    return True, 'Successfully added friend'

def remove_member(email_owner, email_member, fg_name):
    cursor = flask.g.connection.cursor()
    sql = '''DELETE FROM Belong WHERE email_owner=%s AND email_member=%s AND fg_name=%s'''
    cursor.execute(sql, (email_owner, email_member, fg_name))
    flask.g.connection.commit()
    
    return True, 'Removed friend from fg'

def create_group(email_owner, fg_name, description):
    cursor = flask.g.connection.cursor()
    sql = '''INSERT INTO FriendGroup(fg_name, email, description)
              VALUES (%s,%s,%s)'''
    cursor.execute(sql, (fg_name, email_owner, description))
    flask.g.connection.commit()
    

def remove_group(email_owner, fg_name):
    cursor = flask.g.connection.cursor()
    sql = '''DELETE FROM FriendGroup WHERE fg_name=%s and email=%s'''
    cursor.execute(sql, (fg_name, email_owner))
    flask.g.connection.commit()
    

def get_groups(email_owner, names_only):
    cursor = flask.g.connection.cursor()
    sql = '''
    SELECT FriendGroup.fg_name, description, email_member FROM FriendGroup LEFT OUTER JOIN Belong 
            ON email=email_owner AND FriendGroup.fg_name=Belong.fg_name 
            where email=%(user)s
            UNION
    SELECT FriendGroup.fg_name, description, email_member FROM FriendGroup LEFT OUTER JOIN Belong 
            ON email=email_owner AND FriendGroup.fg_name=Belong.fg_name 
            where email=%(user)s
            Group BY FriendGroup.fg_name'''
    if names_only:
        sql = '''SELECT fg_name FROM FriendGroup
            where email=%(user)s'''
    cursor.execute(sql, {'user':email_owner})
    raw = cursor.fetchall()
    if names_only:
        return [d['fg_name'] for d in raw]
    else:

        formatted = []
        obj = None
        name = None
        for entry in raw:
            # if not any(obj['fg_name'] == entry['fg_name'] for obj in formatted):
            #     formatted.append({
            #         'fg_name': entry['fg_name'],
            #         'description': entry['description'],
            #         'members': [
            #             entry['email_member']
            #         ]
            #     })
            if name == entry['fg_name']:
                obj['members'].append(entry['email_member'])
            else:
                if obj:
                    formatted.append(obj)
                name = entry['fg_name']
                obj = entry.copy()
                del obj['email_member']
                obj['members'] = []
                if entry['email_member']:
                    obj['members'].append(entry['email_member'])
        formatted.append(obj)
        return formatted





# Optional feature 2: Profile pages
def get_profile_info(email, email_other):
    cursor = flask.g.connection.cursor()
    sql = '''SELECT first_name, last_name, avatar, bio, IF(friends.email_friend IS NULL, FALSE, TRUE) as friend
    FROM Person LEFT JOIN Friends ON(Person.email=Friends.email_friend AND Friends.email=%s) 
    WHERE Person.email=%s'''
    cursor.execute(sql, (email, email_other))
    profile = cursor.fetchone()
    
    return profile

def set_profile_bio(email, bio):
    cursor = flask.g.connection.cursor()
    sql = '''UPDATE Person SET bio=%s WHERE email=%s'''
    cursor.execute(sql, (bio, email))
    flask.g.connection.commit()
    
    return True

def set_profile_avatar(email, avatar):
    cursor = flask.g.connection.cursor()
    sql = '''UPDATE Person SET avatar=%s WHERE email=%s'''
    cursor.execute(sql, (avatar, email))
    flask.g.connection.commit()
    
    return True

# Optional feature 3: Saved posts. Returns post saved by user
def get_saved_posts(email, page, results_per_page):
    cursor = flask.g.connection.cursor()
    sql = '''SELECT * FROM Saved INNER JOIN ContentItem 
              USING(item_id)
              WHERE Saved.email=%s
              ORDER BY save_time DESC LIMIT %s,%s'''
    start = (page - 1) * results_per_page
    cursor.execute(sql, (email, start, results_per_page))
    saved_posts = cursor.fetchall()
    
    return saved_posts


def save_post(email, item_id):
    if not can_see(email, item_id):
        return 'User is not allowed to save this content'
    cursor = flask.g.connection.cursor()
    sql = '''INSERT INTO Saved(email, save_time, item_id)
              VALUES (%s,NOW(),%s)'''
    cursor.execute(sql, (email, item_id))
    flask.g.connection.commit()
    


def unsave_post(email, item_id):
    cursor = flask.g.connection.cursor()
    sql = '''DELETE FROM Saved WHERE email=%s AND item_id=%s'''
    cursor.execute(sql, (email, item_id))
    flask.g.connection.commit()
    


# Optional feature 6. Post comments
def post_comment(email, item_id, comment):
    if not can_see(email, item_id):
        return 'User is not allowed to comment on this content'
    cursor = flask.g.connection.cursor()
    sql = '''INSERT INTO Comments(item_id, email, post_time, content) 
              VALUES (%s, %s, NOW(), %s)'''
    cursor.execute(sql, (item_id, email, comment))
    flask.g.connection.commit()
    
    return True


def get_comments(email, item_id):
    if not can_see(email, item_id):
        return False, "Unauthorized"
    cursor = flask.g.connection.cursor()
    sql = '''SELECT * FROM Comments WHERE item_id=%s'''
    cursor.execute(sql, (item_id,))
    comments = cursor.fetchall()
    
    return True, comments


def get_friends(email):
    cursor = flask.g.connection.cursor()
    sql = '''SELECT email_friend FROM Friends WHERE email=%s'''
    cursor.execute(sql, (email,))
    
    return cursor.fetchall()

def add_friend(email, email_friend):
    cursor = flask.g.connection.cursor()
    sql = '''INSERT INTO Friends(email, email_friend) 
              VALUES (%s, %s)'''
    cursor.execute(sql, (email, email_friend))
    flask.g.connection.commit()
    
    return True, 'Added friend.'


def remove_friend(email, email_friend):
    cursor = flask.g.connection.cursor()
    sql = '''DELETE FROM Friends WHERE email=%s AND email_friend=%s'''
    cursor.execute(sql, (email, email_friend))
    flask.g.connection.commit()


def rate_post(email, item_id, emoji):
    if not can_see(email, item_id):
        return 'User is not allowed to save this content'
    cursor = flask.g.connection.cursor()
    sql = '''INSERT INTO Posted(email, item_id, rate_time, emoji)
              VALUES (%s,%s,NOW(),%s)'''
    cursor.execute(sql, (email, item_id, emoji))
    flask.g.connection.commit()



def post_ratings(email, item_id):
    if not can_see(email, item_id):
        return False, 'User is not allowed to save this content'
    cursor = flask.g.connection.cursor()
    sql = '''SELECT emoji FROM Posted WHERE item_id=%s'''
    cursor.execute(sql, (item_id,))

    return True, cursor.fetchall()
