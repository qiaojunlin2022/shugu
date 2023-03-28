import os
import json


def readJson(filepath):
    path = os.path.dirname(__file__)
    path = os.path.abspath(path + os.path.sep + '..')
    dict_data = {}
    with open(path + "/" + filepath, 'r', encoding="utf-8") as fp:
        dict_data = json.load(fp)
    return dict_data
