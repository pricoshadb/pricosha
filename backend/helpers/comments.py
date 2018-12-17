from helpers.import_helpers import *

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

def delete_comment(email, comment_id):
    c = conn.cursor(pymysql.cursors.DictCursor)
    sql = '''   DELETE Comments 
                FROM (Comments JOIN ContentItem ON Comments.item_id = ContentItem.item_id) 
              WHERE ((Comments.email=%s OR ContentItem.email =%s) AND comment_id = %s)'''