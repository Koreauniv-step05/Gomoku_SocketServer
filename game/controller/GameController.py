from consts.ROLE import ROLES


class GameController():
    def __init__(self) -> None:
        super().__init__()

        self.roles = ROLES # ['BLACK', 'WHITE', 'OBSERVER']
        self.player = []
        self.num_connected_user = 0

    def allocate_role(self, nickname):
        if self.num_connected_user < 2:
            result = self.roles[self.num_connected_user]
            self.player.append(nickname)
            self.num_connected_user += 1
            return result
        else:
            return self.roles[-1]

    def playersJoined(self):
        if self.num_connected_user >= 2:
            return True
        else:
            return False

    def newStonePoint(self, axisX, axisY, isBlack):
        print('GameController/newStonePoint : ({},{},{})'.format(axisX,axisY,isBlack))