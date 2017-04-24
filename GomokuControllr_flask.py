from flask import Flask, request, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)

app.config['SECRET_KEY'] = "mysecret"
socket_io = SocketIO(app)

@app.route('/')
def hello_world(name="Yangyi"):
    name = request.args.get('name', name)
    return 'Gomoku server {}!'.format(name)

@app.route('/newgame')
def newgame(name="Yangyi"):
    name = request.args.get('name', name)
    return render_template('newgame.html')

@socket_io.on("message")
def req(msg):
    print("message : "+msg)

    send(msg, broadcast=True)

if __name__ == '__main__':
    socket_io.run(app)
    app.run(debug=True, port=8001, host='0.0.0.0')
