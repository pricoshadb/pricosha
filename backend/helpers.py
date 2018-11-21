import hashlib
import pymysql

conn = pymysql.connect(host='localhost',
                        user='user',
                        password='haha',
                        db='pricosha')

def check_pw(password, password_hash):
    return password_hash == hashlib.sha256(password.encode('utf8')).hexdigest()


# Hash password with sha256 and store as hex string
def hash_pw(password):
    return hashlib.sha256(password.encode('utf8')).hexdigest()


def create_content_item(email, post_time, item_name, is_pub, file_path):
    c = conn.cursor()
    sql = '''INSERT INTO 
              ContentItem(email, post_time, item_name, is_pub, file_path)
              VALUES (%s,%s,%s,%s,%s)'''
    c.execute(sql, (email, post_time, item_name, is_pub, file_path))
    