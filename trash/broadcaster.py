import threading
import time

import numpy
from flask import copy_current_request_context, json
from flask_socketio import emit

def broadcast_thread():
    # @copy_current_request_context
    def send_yourturn():
        while True:
            print('emit game_broadcast')

            arr = numpy.ones([4, 4])
            arr_list = arr.tolist()

            arr_json = json.dumps(arr_list)

            emit('game_state', arr_json)
            time.sleep(10)

    thread = threading.Thread(target=send_yourturn)
    thread.start()
    print("threading : start")