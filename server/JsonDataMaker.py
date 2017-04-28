import json
from json import JSONEncoder

from consts.ROLE import ROLES
from server.domain.Data import Data


def makeSetroleData(role):
    command = "Setrole"
    message = "You're {}".format(role)
    data = role

    jsondata = json.dumps(Data(command, message, data).__dict__)
    print('JsonDataMaker/makeRole : {}'.format(jsondata))
    return jsondata

def makeTellOnYourTurn(isBlack):
    command = "Onyourturn"
    if isBlack:
        turn = ROLES[0]
    else:
        turn = ROLES[1]

    message = "On {}'s turn".format(turn)
    data = turn

    jsondata = json.dumps(Data(command, message, data).__dict__)
    print('JsonDataMaker/makeRole : {}'.format(jsondata))
    return jsondata
