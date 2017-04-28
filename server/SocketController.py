from flask_socketio import Namespace
from game.controller.GameController import GameController


class MyCustomNamespace(Namespace):
    def __init__(self, namespace=None):
        super().__init__(namespace)
        self.mGameController = GameController()

    def on_to_server(self, data):
        self.emit('to_server', 'on_to_server: reply '+data)
        # self.emit('to_server', 'on_to_server: broadcast '+cmd, broadcast=True)
        print("on_to_server : " + data)
        # if (cmd == "join"):
        #     your_role = self.mGameController.allocate_role()
        #     self.emit('game_broadcast', data={
        #             "message": 'Youre ' + your_role,
        #             "command": "set_player",
        #             "content": your_role
        #         })

    def on_to_client(self, data):
        self.emit('to_client', 'on_to_client: reply '+data)
        # self.emit('to_client', 'on_to_client: broadcast'+data, broadcast=True)
        print("on_to_client : " + data)
        pass

    def on_connect(self):
        print("MyCustomNamespace : on_connect")

    def on_disconnect(self):
        print("MyCustomNamespace : on_disconnect")

    def on_reconnect(self):
        print("MyCustomNamespace : on_reconnect")

    def on_message(self, msg):
        self.send('on_message: reply ' + msg)
        print("on_message "+msg)