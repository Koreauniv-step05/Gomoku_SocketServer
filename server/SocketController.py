import json
import threading

from flask_socketio import Namespace
from game.controller.GameController import GameController
from server.JsonDataMaker import *


class MyCustomNamespace(Namespace):
    def __init__(self, namespace=None):
        super().__init__(namespace)
        self.mGameController = GameController()
        self.startFlag = False

    def on_to_server(self, data):
        self.emit('to_server', data)
        print("on_to_server : " + data)

        parse_data = json.loads(data)
        command = parse_data['command']
        print(parse_data['message'])
        if command == 'Nickname':
            nickname = parse_data['content']
            to_client_data = makeSetroleData(self.mGameController.allocate_role(nickname))
            self.sendDataToClient(to_client_data)

            if self.mGameController.playersJoined():
                if self.startFlag is False:
                    print("Game Start")
                    self.starfFlag = True
                    threading._start_new_thread(self.startGame,())

        elif command == 'NewStonePoint':
            axisX = parse_data['content']['axisX']
            axisY = parse_data['content']['axisY']
            isBlack = parse_data['content']['black']
            self.mGameController.newStonePoint(axisX,axisY,isBlack)

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


    def startGame(self):
        self.turnIsBlack = True
        self.todo = 'Tellonyourturn'
        while(True):
            if self.todo == 'Tellonyourturn':
                self.sendTellOnYourTurn(self.turnIsBlack)
                self.todo = 'Wait'
            elif self.todo == 'Wait':
                continue

    def sendTellOnYourTurn(self, turnIsBlack):
        self.sendDataToClient(makeTellOnYourTurn(turnIsBlack))

    def sendDataToClient(self,data):
        print("MyCustomNamespace/sendDataToClient : {}".format(data))
        self.emit('to_client', data)