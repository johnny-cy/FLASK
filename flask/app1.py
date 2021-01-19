"""
說明：
使用Flask_API套件，無發現其與原生Flask使用區別，看點是request的使用方式，可獲取headers、post body、query params。
這範例是models放在db.py，使用前先引用進來。包括app跟db及User表
安裝：
Flask==1.1.2
Flask-API==2.0
"""
from flask import request, url_for, jsonify
from db import db, app, User


@app.route('/api/<name>/<location>', methods=['GET'])
def create_user(name, location): 
    """
    創建使用者存到sqlite3
    """
    user = User(name=name, location=location)
    db.session.add(user)
    db.session.commit()
    return '<H1> Added new user !'

@app.route('/', methods=['GET'])
def index():
    return "<H1>Hello Flask</H1>"



@app.route('/table/create', methods=['POST'])
def tableCreate():
    """
    創建資料表
    """
    pass
    return {"status": 200, "result": []}

@app.route('/table/drop', methods=['DELETE'])
def tableDrop():
    """
    刪除資料表
    """
    pass
    return {"status": 200, "result": []}

@app.route('/data/create', methods=["POST"])
def dataCreate():
    
    # print(request.data) # 可獲得post body
    return request.data

@app.route('/data/read', methods=['GET'])
def dataRead():
    # print(request.args.to_dict()) # 可獲得query_parameters
    return {"status": 200, "result": []}

@app.route('/data/update', methods=['UPDATE'])
def dataUpdate():
    pass
    return {"status": 200, "result": []}

@app.route('/data/delete', methods=['DELETE'])
def dataDelete():
    pass
    # request.args.to_dict() # 可獲得query_parameters
    return {"status": 200, "result": ""}


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)

"""sqlite operate
conn = sqlite3.connect('example.db')
cursor = conn.cursor()
res = cursor.execute().fetchall() # return list



"""