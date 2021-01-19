"""
說明：
Flask + templates/index.html  分別是前後端socketio使用範例
測試方法，打開兩個視窗，一個進到/，另一個進到/push，此時後端會push一條測試訊息給首頁，之後再進到/remove則會清除前面的測試訊息
安裝：
Flask==1.1.2
Flask-SocketIO==5.0.1
"""
# python
import os
# flask
from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect
from flask import flash
# flask-socketio
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(16).hex()

socketio = SocketIO()
socketio.init_app(app, cors_allowed_origins='*')

name_space = '/dcenter'

@app.route('/')
def index():
    # return "ddd"
    return render_template('index.html')

@app.route('/push')
def push_once():
    event_name = 'dcenter' # 有點像是隊列名稱 
    broadcasted_data = {'data': "test message"} # 資料
    socketio.emit(event_name, broadcasted_data, broadcast=False, namespace=name_space) # 發送
    return "done!"

@app.route('/remove')
def remove_last():
    event_name = 'dcenter'
    broadcasted_data = {'data': 'del last'}
    socketio.emit(event_name, broadcasted_data, broadcast=False, namespace=name_space) # 發送)
    return "sent del."

@socketio.on('connect', namespace=name_space)
def connected_msg():
    print('client connected.')
        
@socketio.on('disconnect', namespace=name_space)
def disconnect_msg():
    print('client disconnected.')

@socketio.on('my_event', namespace=name_space)
def test_message(message):
    print(message)
    # emit('my_response', {'data': message['data'],'count': 1})

if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=5000, debug=-True)