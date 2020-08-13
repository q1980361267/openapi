# import logging
# import os
# import time
#
# path = './file/'
# if not os.path.exists(path):
#     os.mkdir(path)
#
# file = path + time.strftime('%H_%M_%S') + '_log.txt'
#
# print(file)
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename=file)
#
# logging.info('info')
# logging.debug('debug')
# logging.error('error')
# logging.critical('critical')
#
