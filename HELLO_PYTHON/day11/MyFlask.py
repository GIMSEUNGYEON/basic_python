from flask import Flask, jsonify, request
from day11.DaoMem import DaoMem

app = Flask(__name__)
de = DaoMem()

@app.route('/mem', methods=['POST'])
def mem_list(): 
    list = de.selectList()
    print(list)
    return jsonify(list)

@app.route('/mem_one', methods=['POST'])
def mem_one(): 
    req = request.get_json()
    # print(req)
    mem = de.select(req['m_id'])
    # print(mem)
    return jsonify(mem)

@app.route('/mem_add', methods=['POST'])
def mem_add(): 
    req = request.get_json()
    m_id = req['m_id']
    m_name = req['m_name']
    mobile = req['mobile']
    email = req['email']
    
    cnt = de.insert(m_id, m_name, mobile, email)
    return jsonify(cnt)

@app.route('/mem_mod', methods=['POST'])
def mem_mod():
    req = request.get_json()
    m_id = req['m_id']
    m_name = req['m_name']
    mobile = req['mobile']
    email = req['email']
    cnt = de.update(m_id, m_name, mobile, email)
    
    return jsonify(cnt)

@app.route('/mem_del', methods=['POST'])
def mem_del():
    req = request.get_json()
    m_id = req['m_id']
    
    cnt = de.delete(m_id)

    return jsonify(cnt)
    
if __name__ =='__main__' :
    app.run(debug=True)
    