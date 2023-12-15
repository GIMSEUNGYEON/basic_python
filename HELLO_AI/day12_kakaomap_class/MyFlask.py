from flask import Flask, redirect, jsonify
from day12_kakaomap_class.dao_bus_path import DaoBusPath

app = Flask(__name__)

@app.route('/')
def index():
    return redirect("static/bus_here.html")

@app.route('/bp_list', methods=['GET'])
def bp_list():
    dbp = DaoBusPath()
    list = dbp.selectList()
    return jsonify(list)

@app.route('/wa_list', methods=['GET'])
def wa_list():
    list = [
        {'lat':36.32516752,    'lng':127.40874756},
        {'lat':36.32391497,    'lng':127.41018983},
        {'lat':36.3238712,     'lng':127.41020835},
        {'lat':36.32382052,    'lng':127.41021167},
        {'lat':36.32377007,    'lng':127.41020457},
        {'lat':36.32371571,    'lng':127.41018351},
        {'lat':36.32366727,    'lng':127.41015571},
        {'lat':36.32361652,    'lng':127.41013275},
        {'lat':36.32357867,    'lng':127.41009599},
        {'lat':36.32353123,    'lng':127.41007376},
        {'lat':36.32348158,    'lng':127.41006832},
        {'lat':36.32343625,    'lng':127.41006779},
        {'lat':36.3233879,     'lng':127.41005738},
        {'lat':36.32332984,    'lng':127.41004251},
        {'lat':36.32328103,    'lng':127.41003534},
        {'lat':36.3232357,     'lng':127.41005883},
        {'lat':36.32318758,    'lng':127.41008604},
        {'lat':36.32315223,    'lng':127.41012637},
        {'lat':36.32314371,    'lng':127.41019553},
        {'lat':36.32316236,    'lng':127.41025503},
        {'lat':36.32319656,    'lng':127.41030691},
        {'lat':36.32324142,    'lng':127.41035699},
        {'lat':36.32328966,    'lng':127.41040877},
        {'lat':36.32333689,    'lng':127.41045002},
        {'lat':36.32337619,    'lng':127.41048623},
        {'lat':36.32340188,    'lng':127.41053285},
        {'lat':36.32341501,    'lng':127.41047737},
        {'lat':36.32341721,    'lng':127.41041188},
        {'lat':36.32346958,    'lng':127.41034957},
        {'lat':36.32344964,    'lng':127.41025403},
        {'lat':36.32343667,    'lng':127.41014842},
        {'lat':36.32314979,    'lng':127.41019238},
        {'lat':36.32317245,    'lng':127.41013498},
        {'lat':36.32429151,    'lng':127.40961662},
        {'lat':36.32423614,    'lng':127.40961857},
        {'lat':36.32420137,    'lng':127.40966915},
        {'lat':36.32414099,    'lng':127.40974616},
        {'lat':36.32421646,    'lng':127.40984468},
        {'lat':36.32440184,    'lng':127.40976009},
        {'lat':36.32447882,    'lng':127.40980792},
        {'lat':36.32442453,    'lng':127.40972684},
        {'lat':36.32446819,    'lng':127.40971303},
        {'lat':36.32451701,    'lng':127.40971991},
        {'lat':36.32457228,    'lng':127.40968525},
        {'lat':36.32455014,    'lng':127.40962152},
        {'lat':36.32458051,    'lng':127.4095774 },
        {'lat':36.32462743,    'lng':127.40959092},
        {'lat':36.32466528,    'lng':127.40954669},
        {'lat':36.32470886,    'lng':127.40950829},
        {'lat':36.32474106,    'lng':127.40946628},
        {'lat':36.32478325,    'lng':127.40943033},
        {'lat':36.32482597,    'lng':127.40938192},
        {'lat':36.32486434,    'lng':127.40933259},
        {'lat':36.32490868,    'lng':127.40929554},
        {'lat':36.32496502,    'lng':127.40929866},
        {'lat':36.3250049,     'lng':127.40936422},
        {'lat':36.32506719,    'lng':127.40899742},
        {'lat':36.32509844,    'lng':127.40894719},
        {'lat':36.3251309,     'lng':127.40889566},
        {'lat':36.32518139,    'lng':127.40887702},
        {'lat':36.32521911,    'lng':127.40883541},
        {'lat':36.32524815,    'lng':127.40878285},
        {'lat':36.32520277,    'lng':127.40878689},
        {'lat':36.32524647,    'lng':127.40880356},
        {'lat':36.32529232,    'lng':127.40879274}
    ]
    return jsonify(list)

if __name__ =='__main__' :
    app.run(debug=True)
    