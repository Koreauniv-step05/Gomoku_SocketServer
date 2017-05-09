
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template
from server.SocketController import MyCustomNamespace
from flask_socketio import SocketIO

app = Flask(__name__)


# @app.route('/')
# def newgame():
#     return render_template("newgame.html")

@app.route('/gui')
def gui():
    return render_template("gui.html")

@app.route('/')
def visualize():
    return render_template("visualize.html")

# socketio = SocketIO(app)
# socketio.on_namespace(MyCustomNamespace())