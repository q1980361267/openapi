import os


def workdir():
    dir = os.path.dirname(os.path.abspath(__file__))
    return dir


def configFilePath(file_name='zhaoshang_pro_config.json'):
    return workdir() + "/" + file_name


def assistFilePath(file_name='assist_config.yaml'):
    return workdir() + "\\" + file_name


def routerDestination():
    destination = {
        "name": "mysql",
        "type": 4,
        "env": 1,
        "host": "36.155.103.36",
        "port": 3306,
        "username": "root",
        "password": "Iot!@10086",
        "database": "edgetester",
        "table": "test"
    }
    return destination