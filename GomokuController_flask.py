import time
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

from server.SocketController import MyCustomNamespace

app = Flask(__name__)

app.config['SECRET_KEY'] = "mysecret"
socket_io = SocketIO(app)
mGameController = None

@app.route('/')
def hello_world(name="Yangyi"):
    # name = request.args.get('name', name)
    return render_template("newgame.html")

@app.route('/gui')
def gui(name="Yangyi"):
    # name = request.args.get('name', name)
    return render_template("gui.html")
#
# @socket_io.on("connect")
# def on_connect():
#     print('connect')
#     emit('user_connect', 'user_connect: reply')
#     emit('user_connect', 'user_connect: broadcast', broadcast=True)
#
# @socket_io.on("disconnect")
# def on_disconnect():
#     print('disconnect')
#     emit('user_disconnect', 'user_disconnect: reply')
#     emit('user_disconnect', 'user_disconnect: broadcast', broadcast=True)
#
# @socket_io.on("reconnect")
# def on_reconnect():
#     print('reconnect')
#     emit('user_reconnect', 'user_reconnect: reply')
#     emit('user_reconnect', 'user_reconnect: broadcast', broadcast=True)

if __name__ == '__main__':
    socket_io.on_namespace(MyCustomNamespace())
    socket_io.run(app)

    app.run(debug=True, port=8002, host='0.0.0.0')