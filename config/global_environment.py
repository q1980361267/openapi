import os
import random

def workdir():
    dir = os.path.abspath(os.path.dirname(__file__))
    return dir


def configFilePath(file_name='zhaoshang_test_config.json'):
    return os.path.join(workdir(), file_name)


def assistFilePath(file_name='assist_config.yaml'):
    # return workdir() + "\\" + file_name
    return os.path.join(workdir(), file_name)


if __name__ == '__main__':
    print(workdir())


# import os
#
#
# def workdir():
#     file_dir = os.path.dirname(__file__)
#     dir = os.path.abspath(os.path.dirname(file_dir))
#     return dir
#
#
# def configFilePath():
#     env_dist = os.environ
#     config_file_env = env_dist.get("CONFIGFILE")
#     config_file = os.path.join(workdir(), config_file_env)
#     return config_file
#
#
# def assistFilePath(file_name='assist_config.yaml'):
#     # return workdir() + "\\" + file_name
#     env_dist = os.environ
#     assist_file_env = env_dist.get("ASSISTFILE")
#     assist_file = os.path.join(workdir(), assist_file_env)
#     return os.path.join(workdir(), assist_file)
#
#
# def routerDestination():
#     destination = {
#         "name": "mysql_" + ''.join(random.sample('abcde12345', 5)),
#         "type": 4,
#         "env": 1,
#         "host": "100.78.28.27",
#         "port": 3306,
#         "username": "root",
#         "password": "Iot!@10086",
#         "database": "edgetester",
#         "table": "test"
#     }
#     return destination
#
#
# if __name__ == '__main__':
#     print(configFilePath())
#     print(assistFilePath())