from abc import ABCMeta, abstractmethod


class PlayerMessenger(metaclass=ABCMeta):
    @abstractmethod
    def setBlackOrWhite(self):
        pass

    @abstractmethod
    def noticeWin(self):
        pass

    @abstractmethod
    def noticeDefeat(self):
        pass

    @abstractmethod
    def sendWasValidStone(self):
        pass
