from flask_socketio import SocketIO, emit

from trash.GameController import GameController

socket_io = SocketIO()



@socket_io.on("game_command")
def game_command(cmd):
    print("game_command : ")
    if cmd == 'new_game':
        # todo newgame
        print("new_game : ")

        newgame = GameController()

        emit('game_command_reply', cmd)

@socket_io.on("game_command_reply")
def game_command_reply(cmd):
    print('game_command_reply : '+cmd)
    pass

@socket_io.on("new_stone")
def new_stone(newStonePoint):
    # todo newstone
    print("new_stone : "+newStonePoint)

    emit('new_stone_reply', newStonePoint)

@socket_io.on("new_stone_reply")
def new_stone_reply(cmd):
    print('new_stone_reply : '+cmd)
    pass

@socket_io.on("game_status")
def game_status(cmd):
    print("game_status(from server) : "+cmd)
    # todo remove

def game_status_sender(cmd):
    emit('game_status', cmd)

# if __name__ == '__main__':
#     server = create_server()
#     server.run(debug=True, port=8001, host='0.0.0.0')
#     # socket_io.run(app)

