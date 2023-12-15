import pymysql

class DaoBusPath : 
    def __init__(self):
        self.conn = pymysql.connect(host='localhost',
                    user='root',
                    password='python',
                    db='python',
                    port=3305,
                    charset='utf8')
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)
    
    def selectList(self):
        sql = """
            SELECT * FROM bus_path WHERE bp_name in (SELECT bp_name from bus_path where sta_id = '21400')
            """
        self.cursor.execute(sql)
        list = self.cursor.fetchall()
        
        return list
    
    def select(self, sta_id):
        sql = f'''
            select * from bus_path
            where 
                sta_id = {sta_id}'''
        self.cursor.execute(sql)
        vo = self.cursor.fetchone()
        
        return vo
         
    def insert(self, bp_name, bp_seq, sta_id, sta_name, lat, lng):
        sql = f'''
            insert into bus_path
            values('{bp_name}', '{bp_seq}', '{sta_id}', '{sta_name}', '{lat}','{lng}')
            '''
        cnt = self.cursor.execute(sql)
        self.conn.commit() 

        return cnt
    
    def __del__(self):
        self.conn.close()
        self.cursor.close()
        
if __name__ == '__main__':
    de = DaoBusPath()
    print(de.selectList());
    