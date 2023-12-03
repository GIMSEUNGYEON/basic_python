import pymysql

class DaoStock:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost',
                    user='root',
                    password='python',
                    db='python',
                    port=3305,
                    charset='utf8')
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        
    def insert(self, s_name, price, s_code, ymd):
        sql = f"""
                insert into stock (s_name, price, s_code, ymd) 
                values('{s_name}',{price},'{s_code}','{ymd}')
                """
        cnt = self.cursor.execute(sql)
        self.conn.commit()
        
        return cnt
    
if __name__=='__main__':
    dc = DaoStock()
    