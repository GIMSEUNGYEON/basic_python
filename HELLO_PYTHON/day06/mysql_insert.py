import pymysql

conn = pymysql.connect(host='localhost',
                        user='root',
                        password='python',
                        db='python',
                        port=3305,
                        charset='utf8')

sql = "insert into emp values(4, '4', '4','4')"

curs = conn.cursor()

curs.execute(sql)


sql2 = 'insert into emp values(%s,%s,%s,%s)'

cnt = curs.execute(sql2, (5,'5','5','5'))
print(cnt)
conn.commit() 

curs.close()
conn.close()

