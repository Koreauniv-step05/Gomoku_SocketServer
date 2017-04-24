import threading

import time
from flask import Flask, request, render_template, copy_current_request_context
from flask_socketio import SocketIO, emit


app = Flask(__name__)

app.config['SECRET_KEY'] = "mysecret"
socket_io = SocketIO(app)

@app.route('/')
def hello_world(name="Yangyi"):
    name = request.args.get('name', name)
    return 'Gomoku server {}!'.format(name)

# @app.route('/newgame')
# def newgame(name="Yangyi"):
#     name = request.args.get('name', name)
#
#     return render_template('newgame.html')

@socket_io.on("game_command")
def game_command(cmd):
    @copy_current_request_context
    def send_yourturn():
        while True:
            print('emit game_broadcast')
            emit('game_broadcast', 'yourturn')
            time.sleep(10)

    if cmd == 'new_game':
        # todo newgame
        print("new_game : ")

        # todo remove
        thread = threading.Thread(target=send_yourturn)
        thread.start()
        print("threading : start")


@socket_io.on("new_stone")
def new_stone(newStonePoint):
    # todo newstone
    print("new_stone : "+newStonePoint)

if __name__ == '__main__':
    socket_io.run(app)
    app.run(debug=True, port=8001, host='0.0.0.0')


