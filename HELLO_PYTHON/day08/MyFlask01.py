from flask import Flask, request, render_template
import pymysql

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello flask!'

@app.route('/emp_list')
def emp_list():

    return render_template("emp_list.html")

if __name__ =='__main__' :
    app.run(debug=True)
    