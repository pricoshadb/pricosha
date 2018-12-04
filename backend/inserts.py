
import time
import pymysql

conn = pymysql.connect(host='localhost',
                       user='user',
                       password='pricosha',
                       db='pricosha')
c = conn.cursor()
for i in range(100):
    sql = "INSERT INTO ContentItem(email, post_time, item_name, is_pub, file_path) values('AA@nyu.edu', NOW(), %d, True, 'test.png')" %i
    c.execute(sql)
    time.sleep(1)
conn.commit()