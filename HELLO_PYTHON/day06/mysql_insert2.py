import pymysql

conn = pymysql.connect(host='localhost',
                        user='root',
                        password='python',
                        db='python',
                        port=3305,
                        charset='utf8')

e_id = '6';
e_name = '6';
gen = '6';
addr = '6';

sql = f"""
      insert into emp 
      values('{e_id}', '{e_name}', '{gen}', '{addr}')
    """

curs = conn.cursor()

cnt = curs.execute(sql)
print(cnt) # 영향을 받은 행의 개수 리턴
print(curs.rowcount) # 마찬가지로 영향을 받은 행의 개수
conn.commit() 

curs.close()
conn.close()

