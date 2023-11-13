import pymysql

class DaoEmp : 
    def __init__(self):
        self.conn = pymysql.connect(host='localhost',
                       user='root',
                       password='python',
                       db='python',
                       port=3305,
                       charset='utf8')
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)
    
    def selectList(self):
        sql = 'select * from emp'
        self.cursor.execute(sql)
        list = self.cursor.fetchall()
        
        return list
    
    def __del__(self):
        self.conn.close()
        self.cursor.close()
        
if __name__ == '__main__':
        de = DaoEmp()
        list = de.selectList()
        print(list)


