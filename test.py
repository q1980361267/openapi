import os
import global_environment

config_path = global_environment.workdir() + '\\' + os.environ['CONFIGFILE']

a = os.path.join(global_environment.workdir(), os.environ['CONFIGFILE'])
print(config_path)
print(a)
