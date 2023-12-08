from flask import Flask, request, render_template
import pymysql

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/bus')
def dus():
    return render_template("bus.html")

if __name__ =='__main__' :
    app.run(debug=True)
    