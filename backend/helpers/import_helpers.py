import pymysql

conn = pymysql.connect(host='localhost',
                       user='user',
                       password='pricosha',
                       db='pricosha')


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


def response(success, msg):
    return {
        'success': success,
        'response': msg
    }

from helpers.comments import *