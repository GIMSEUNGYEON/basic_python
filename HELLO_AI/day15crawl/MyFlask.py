from flask import Flask, redirect, jsonify
import pymysql
from day11_crawl2.dao_bus_path import DaoBusPath

app = Flask(__name__)

@app.route('/')
def index():
    return redirect("static/bus_daejeon.html")

@app.route('/bp_list', methods=['GET'])
def bp_list():
    dbp = DaoBusPath()
    list = dbp.selectList()
    return jsonify(list=list)

if __name__ =='__main__' :
    app.run(debug=True)
    