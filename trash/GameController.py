import numpy
from flask_socketio import emit

class GameController():
    """
    1. 전송방법 모름 but 받아옴
    2. 할당받은 플레이어에게 status전송
    3. 플레이어에게 newstone받아옴
    """

    def __init__(self) -> None:
        super().__init__()
        self.black = Player()
        self.status = numpy.zeros([5,5])

    def send_status(self):
        self.black.send_status_to_player(self.status)
        # white.send_status(self.status)

class Player():
    def send_status_to_player(self, status):
        emit('game_status',status)