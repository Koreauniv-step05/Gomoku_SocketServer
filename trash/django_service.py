import json

import numpy


def get_status_from_django():
    arr = numpy.zeros([3, 3])
    arr_list = arr.tolist()

    arr_json = json.dumps(arr_list)

    return arr_json