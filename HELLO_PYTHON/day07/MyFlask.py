from flask import Flask, request, render_template
import pymysql

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello flask!'

@app.route('/param')
def param():
    menu = request.args.get('menu', type=str)
    return f'param: menu={menu}'

@app.route('/post', methods=['GET','POST'])
def post():
    result = request.form['menu']
    return f"post{result}"
    
@app.route('/forw')
def forw():
    a='홍길동'
    b=['전우치','일지매', '정몽주']
    c=[
        {'e_id':1,'e_name':1,'gen':1,'addr':1},
        {'e_id':2,'e_name':2,'gen':2,'addr':2},
        {'e_id':3,'e_name':3,'gen':3,'addr':3}
    ]
    return render_template("forw.html", name=a, list=b, c=c)

@app.route('/emp')
def emp():
    conn = conn = pymysql.connect(host='localhost',
                       user='root',
                       password='python',
                       db='python',
                       port=3305,
                       charset='utf8')
    
    sql = 'select * from emp'
    
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql)
    result = cursor.fetchall()

    return render_template("emp.html", result=result)

if __name__ =='__main__' :
    app.run(debug=True)
    