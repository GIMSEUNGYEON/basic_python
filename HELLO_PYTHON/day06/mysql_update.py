import pymysql

conn = pymysql.connect(host='localhost',
                        user='root',
                        password='python',
                        db='python',
                        port=3305,
                        charset='utf8')

e_id = '6';
e_name = '7';
gen = '7';
addr = '7';

sql = f"""
      update emp 
      set 
          e_name = '{e_name}',
          gen = '{gen}',
          addr = '{addr}'
      where 
          e_id = {e_id}
      """
print(sql)
curs = conn.cursor()

cnt = curs.execute(sql)
print(cnt) # 영향을 받은 행의 개수 리턴
# print(curs.rowcount) # 마찬가지로 영향을 받은 행의 개수
conn.commit()

curs.close()
conn.close()

