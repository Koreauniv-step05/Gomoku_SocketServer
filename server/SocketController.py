from flask_socketio import Namespace
from game.controller.GameController import GameController


class MyCustomNamespace(Namespace):
    def __init__(self, namespace=None):
        super().__init__(namespace)
        self.mGameController = GameController()

    def on_to_server(self, cmd):
        self.emit('to_server', 'on_to_server: reply '+cmd)
        # self.emit('to_server', 'on_to_server: broadcast '+cmd, broadcast=True)
        print("MyCustomNamespace : on_to_server ")
        print("on_to_server : " + cmd)
        # if (cmd == "join"):
        #     your_role = self.mGameController.allocate_role()
        #     self.emit('game_broadcast', data={
        #             "message": 'Youre ' + your_role,
        #             "command": "set_player",
        #             "content": your_role
        #         })

    def on_to_client(self, data):
        self.emit('to_client', 'on_to_client: reply'+data)
        # self.emit('to_client', 'on_to_client: broadcast'+data, broadcast=True)
        print("MyCustomNamespace : on_to_client " + data)
        pass

    def on_new_stone(self, data):
        print("MyCustomNamespace : on_new_stone "  + data)
        pass

    def on_my_event(self, data):
        self.emit('my_response', data)
