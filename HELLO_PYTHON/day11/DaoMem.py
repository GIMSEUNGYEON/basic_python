import pymysql

class DaoMem : 
    def __init__(self):
        self.conn = pymysql.connect(host='localhost',
                    user='root',
                    password='python',
                    db='python',
                    port=3305,
                    charset='utf8')
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)
    
    def selectList(self):
        sql = 'select * from mem'
        self.cursor.execute(sql)
        list = self.cursor.fetchall()
        
        return list
    
    def select(self, m_id):
        sql = f'''
            select * from mem
            where 
                m_id = {m_id}'''
        self.cursor.execute(sql)
        vo = self.cursor.fetchone()
        
        return vo
         
    def insert(self, m_id, m_name, mobile, email):
        sql = f'''
            insert into mem
            values({m_id}, {m_name}, {mobile}, {email})
            '''
        cnt = self.cursor.execute(sql)
        self.conn.commit() 

        return cnt
    
    def update(self, m_id, m_name, mobile, email):
        sql = f'''
            update mem
            set 
                m_name = {m_name}, 
                mobile = {mobile}, 
                email = {email} 
            where 
            m_id = {m_id}
            '''
        cnt = self.cursor.execute(sql)
        self.conn.commit()
        
        return cnt
    
    def delete (self, m_id):
        sql = f'''
            delete from mem
            where
                m_id = {m_id}
            '''
        cnt = self.cursor.execute(sql)
        self.conn.commit()
        
        return cnt
    
    def __del__(self):
        self.conn.close()
        self.cursor.close()
        
if __name__ == '__main__':
    de = DaoMem()
    list = de.selectList()
    print(list)
    for i in list :
        print(i)
    