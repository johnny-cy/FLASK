"""
說明：
一個原生Flask的與用SQLAlchemy對Sqlite3的連接、建表、讀寫，含有CORS使用方式，可直接本地啟動，API將透過URL讀入參數。
這範例是app.py跟models寫一起的樣子
套件：
Flask==1.1.2
Flask-Cors==3.0.10
Flask-SQLAlchemy==2.4.4
"""

from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# settings
app = Flask(__name__)
CORS(app, resources={r'/api/*': {"origins": "*"}}) # enable path that matchs the reg exp.
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite3"
db = SQLAlchemy(app) # for inherited by table class


# create a table by creating a class
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    location = db.Column(db.String(50))
    data_created = db.Column(db.DateTime, default=datetime.now)

class UserLevel(db.Model):
    # __tablename__ = 'UserLevelTable'
    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.String(10))
    data_created = db.Column(db.DateTime, default=datetime.now)

# 參考欄位類型 https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/#simple-example
# sqlite3執行檔案下載 https://www.sqlite.org/download.html

@app.route('/api/<name>/<location>', methods=['GET'])
def create_user(name, location): 
    """
    創建使用者存到sqlite3
    """
    user = User(name=name, location=location)
    db.session.add(user)
    db.session.commit()
    return '<H1> Added new user !'

@app.route('/api/<name>', methods=['GET'])
def get_user(name):
    """
    讀取使用者來自sqlite3
    """
    user = User.query.filter_by(name=name).first()
    return f'The user is located in : {user.location}'


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)