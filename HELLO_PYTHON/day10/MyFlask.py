from flask import Flask, redirect, jsonify, request
from day10.daoemp import DaoEmp

app = Flask(__name__)
de = DaoEmp()

@app.route('/')
def index():    
    return redirect('static/ajax.html')
    # 최초 페이지 자체를 이동시켜 백엔드 코드에서 작동

    # return '<script>location.href="static/ajax.html"</script>'
    # 웰컴 페이지로 이동 후 브라우저에게 스크립트 코드를 전송시켜 프론트엔드 코드에서 작동

@app.route('/ajax', methods=['POST'])
def ajax(): 
    req = request.get_json()
    print(req['menu'])
    return jsonify(result = 'success')

@app.route('/emp', methods=['POST'])
def emp_list(): 
    list = de.selectList()
    # return render_template("emp_list.html", emps=emps)
    return jsonify(list)

@app.route('/emp_one', methods=['POST'])
def emp_one(): 
    req = request.get_json()
    emp = de.select(req['e_id'])
    print(emp)
    return jsonify(emp)

@app.route('/emp_add', methods=['POST'])
def emp_add(): 
    req = request.get_json()
    e_id = req['e_id']
    e_name = req['e_name']
    gen = req['gen']
    addr = req['addr']
    
    cnt = de.insert(e_id, e_name, gen, addr)
    return jsonify(cnt)

@app.route('/emp_mod', methods=['POST'])
def emp_mod():
    req = request.get_json()
    e_id = req['e_id']
    e_name = req['e_name']
    gen = req['gen']
    addr = req['addr']
    
    cnt = de.update(e_id, e_name, gen, addr)
    
    return jsonify(cnt)

@app.route('/emp_del', methods=['POST'])
def emp_del():
    req = request.get_json()
    e_id = req['e_id']
    
    cnt = de.delete(e_id)

    return jsonify(cnt)
    
if __name__ =='__main__' :
    app.run(debug=True)
    