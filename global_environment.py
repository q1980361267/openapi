import os


def workdir():
    dir = os.path.dirname(os.path.abspath(__file__))
    return dir


def configFilePath(file_name='test_config.json'):
    return workdir() + "\\" + file_name


def assistFilePath(file_name='assist_config.yaml'):
    return workdir() + "\\" + file_name
