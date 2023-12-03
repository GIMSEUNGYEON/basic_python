import pymysql
import numpy as np

class DaoStock:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost',
                    user='root',
                    password='python',
                    db='python',
                    port=3305,
                    charset='utf8')
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)
    
    def select(self, s_name):
        sql = f"""
                select price from stock
                where s_name='{s_name}'
                """
        self.cursor.execute(sql)
        list = self.cursor.fetchall()
        
        price = []
        for i in list :
            price.append(i["price"])
            
        return price
    
    def selectArrN(self, s_name):
        sql = f"""
                select price from stock
                where s_name='{s_name}'
                """
        self.cursor.execute(sql)
        list = self.cursor.fetchall()
        
        price = []
        for i in list :
            price.append(i["price"])
            
        return np.array(price)
    
    def select_name(self):
        sql  = """
                SELECT 
                    s_name 
                FROM 
                    stock 
                GROUP BY 
                    s_name 
                HAVING COUNT(s_name) = 10
            """
        
        self.cursor.execute(sql)
        name_list = self.cursor.fetchall()
        names = []
        for i in name_list : 
            names.append(i["s_name"])
            
        return names

if __name__=='__main__':
    ds = DaoStock()
    print(ds.select_name())
