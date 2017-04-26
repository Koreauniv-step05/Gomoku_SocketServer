from flask_socketio import Namespace
from game.controller.GameController import GameController


class MyCustomNamespace(Namespace):
    def __init__(self, namespace=None):
        super().__init__(namespace)
        self.mGameController = GameController()

    def on_game_command(self, cmd):
        print("MyCustomNamespace : on_game_command")
        print("game_command : " + cmd)
        if (cmd == "join"):
            your_role = self.mGameController.allocate_role()
            self.emit('game_broadcast', data={
                    "message": 'Youre ' + your_role,
                    "command": "set_player",
                    "content": your_role
                })

    def on_game_status(self, data):
        print("MyCustomNamespace : game_status " + data)
        pass

    def on_new_stone(self, data):
        print("MyCustomNamespace : on_new_stone "  + data)
        pass

    def on_my_event(self, data):
        self.emit('my_response', data)
