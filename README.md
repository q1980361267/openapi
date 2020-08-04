# OPENAPI自动化测试使用说明
## 套件执行
把每个接口的测试放在了一个case文件夹里面，只需要修改执行runner.py文件就可以直接来控制执行要覆盖测试的接口,修改方法

```
# discover中选中需要执行的测试套件
discover = unittest.defaultTestLoader.discover(start_dir=path, pattern='test_*.py')
# wb方式写入report中
with open(report_file, 'w', encoding='utf-8') as report:
    runner = HTMLTestRunner.HTMLTestRunner(stream=report, title=report_title, description=report_description)
    # 使用runner运行测试套件
    runner.run(discover)
    report.close()
```