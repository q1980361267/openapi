import os
from HTMLTestRunner import HTMLTestRunner
import unittest
import time
import logging

time = time.strftime('%Y-%m-%d %H_%M_%S')  # 获取时间
report_title = '测试报告'  # 设置报告标题
report_description = '测试描述'  # 设置报告描述
report_path = './result/'  # 设置测试报告的路径
report_file = report_path + time + '_report.html'  # 获得测试报告
log_file = report_path + time + '_log.txt'  # 获得日志文件
# filename 日志文件路径 level 日志的级别 format 格式
logging.basicConfig(filename=log_file, level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# 如果没有这个路径，就创建路径
if not os.path.exists(report_path):
    os.mkdir(report_path)
else:
    pass
path = './case/'  # 设置路径
# 获得测试集对象
discover = unittest.defaultTestLoader.discover(start_dir=path, pattern='test_*.py')
# wb方式写入report中
with open(report_file, 'wb') as report:
    runner = HTMLTestRunner(stream=report, title=report_title, description=report_description)
    # 使用runner运行测试套件
    runner.run(discover)
    report.close()