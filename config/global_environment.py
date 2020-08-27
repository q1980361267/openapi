import os
import random

def workdir():
    dir = os.path.abspath(os.path.dirname(__file__))
    return dir


def configFilePath(file_name='test_config.json'):
    return os.path.join(workdir(), file_name)




def assistFilePath(file_name='assist_config.yaml'):
    # return workdir() + "\\" + file_name
    return os.path.join(workdir(), file_name)

def routerDestination():
    destination = {
        "name": "mysql_" + ''.join(random.sample('abcde12345', 5)),
        "type": 4,
        "env": 1,
        "host": "100.78.28.27",
        "port": 3306,
        "username": "root",
        "password": "Iot!@10086",
        "database": "edgetester",
        "table": "test"
    }
    return destination