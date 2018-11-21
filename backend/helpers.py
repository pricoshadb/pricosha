import hashlib
import pymysql

conn = pymysql.connect(host='localhost',
                        user='user',
                        password='haha',
                        db='pricosha')


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