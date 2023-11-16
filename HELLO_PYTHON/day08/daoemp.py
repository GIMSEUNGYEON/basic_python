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
    
    def select(self, e_id):
        sql = f'''
            select * from emp
            where 
                e_id = {e_id}'''
        self.cursor.execute(sql)
        vo = self.cursor.fetchone()
        
        return vo
         
    def insert(self, e_id, e_name, gen, addr):
        sql = f'''
            insert into emp
            values({e_id}, {e_name}, {gen}, {addr})
            '''
        cnt = self.cursor.execute(sql)
        self.conn.commit() 

        return cnt
    
    def update(self, e_id, e_name, gen, addr):
        sql = f'''
            update emp 
            set 
                e_name = {e_name}, 
                gen = {gen}, 
                addr = {addr} 
            where 
                e_id = {e_id}
            '''
        cnt = self.cursor.execute(sql)
        self.conn.commit()
        
        return cnt
    
    def delete (self, e_id):
        sql = f'''
            delete from emp
            where
                e_id = {e_id}
            '''
        cnt = self.cursor.execute(sql)
        self.conn.commit()
        
        return cnt
    
    def __del__(self):
        self.conn.close()
        self.cursor.close()
        
if __name__ == '__main__':
    de = DaoEmp()
    # list = de.selectList()
    # print(list)
    # for i in list :
    #     print(i)
    # e_id = input('아이디 입력 : ')
    # e_id = 3
    # vo = de.select(e_id)
    # print(vo)

    # cnt = de.insert('6','6','6','6')    
    # print(cnt)
    
    # cnt = de.update('6','7','7','8')
    # print(cnt)
    
    # cnt = de.delete(9)
    # print(cnt)