from flask import Flask, request, render_template
import pymysql
from day08.daoemp import DaoEmp

app = Flask(__name__)
de = DaoEmp()

@app.route('/')
def index() :
    return 'flask'

if __name__ =='__main__' :
    app.run(debug=True)
    