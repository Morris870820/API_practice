from flask import Flask, jsonify

# 基本上，把下行的語法當做一個約定俗成的用法，就是這樣，沒有其它的用意，如此flask才會知道你的root在何處
app = Flask(__name__)

# flask利用裝飾器@app.route來定義路由，其表達式為@app.route(我的url)
# @app.route(我的url)的後面所接的，也一定是一個要執行的function
# 透過這樣子的設置，當連接到’/'的時候，路由就知道要執行後面的function了
# 定義路由 '/'，並指定接受 GET 請求的處理函式
@app.route('/', methods=['GET'])
def get_users():
    # 模擬的使用者資訊
    users = [
        {'id': 1, 'name': 'John'},
        {'id': 2, 'name': 'Jane'},
        {'id': 3, 'name': 'Bob'},
        {'id': 4, 'name': 'Mia'},
        {'id': 5, 'name': 'Nina'}
    ]
    return jsonify(users)

# 啟動 Flask 應用程式的伺服器
if __name__ == '__main__':
    app.debug = True
    app.run()
