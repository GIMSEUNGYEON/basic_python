import pymysql

conn = pymysql.connect(host='localhost',
                       user='root',
                       password='python',
                       db='python',
                       port=3305,
                       charset='utf8')

sql = 'select * from emp'


cursor = conn.cursor(pymysql.cursors.DictCursor)
cursor.execute(sql)
result = cursor.fetchall()
for data in result :
    print(data)

cursor.close()
conn.close()
