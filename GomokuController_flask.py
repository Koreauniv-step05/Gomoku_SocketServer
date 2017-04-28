import time
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

from consts import config
from server.SocketController import MyCustomNamespace

app = Flask(__name__)

app.config['SECRET_KEY'] = "mysecret"
socket_io = SocketIO(app)
mGameController = None

@app.route('/')
def hello_world(name="Yangyi"):
    return render_template("newgame.html")

@app.route('/gui')
def gui(name="Yangyi"):
    return render_template("gui.html")

if __name__ == '__main__':
    socket_io.on_namespace(MyCustomNamespace())
    socket_io.run(app, host='0.0.0.0', port=config.PORT, debug=True)