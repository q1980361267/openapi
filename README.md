# OPENAPI自动化测试使用说明
现有的OPENAPI分为DMP和ECP两大类，对应的做成了DMP和ECP的套件。通过调用runner时指定套件名称达到对应的全量OPENAPI的回归
## 使用方法
- 步骤一：配置好配置文件config.json
```
{
    "baseURL": "https://test.api.heclouds.com/oes/api/v1",
    "accessKeyId": "ex6GiYQvEOXk1umz",
    "secret": "cnIE4lhLuXVxs0exXYnmfOyInKLFAOYKgJIP"

}
baseURL: OPENAPI的url地址
accessKeyId： 用户的accessKeyId
secret： 用户的accessSecret
这个文件的名称自定义，但是后缀名必须为.josn文件。
```
- 步骤二： 配置好global_environment文件
```
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

以上中有两个地方需要修改配置：
1、def configFilePath(file_name='zhaoshang_pro_config.json'):
    return workdir() + "/" + file_name
其中file_name的名称配置成步骤一中json文件定义的名称，注意：后缀名必须为json

2、def routerDestination():
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

这个方法中，destination配置为要测试的时候真实能够访问成功的外部mysql地址。
host:mysql的ip地址
port：mysql的端口
username： mysql接入用户名
password： mysql接入密码
database： mysql中的某个数据库
table： mysql中对应数据库中的表
该方法中只需要配置好上述几个参数，其他参数都不动
```
- 步骤三：
```
命令行运行cmd中运行runner：
runner -s dmp -m report
-s: 套件名称，可选值：dmp、ecp_new
-m: 运行模式， 可选值：report, noReport
```

- 说明：
```
- 注意点1：
运行模式分report、noReport：
report模式会在result文件下自动生成一个html的报告文件
普通模式也都会在result文件下自动生成一个log文件夹，名称以当前时间名称为
准

- 注意点2：
runner -h 可以查看需要输入参数的帮助提示信息
可以在python环境下或者非python环境下运行本套代码
python环境：
1、安装好对应的依赖包：pip install -r requirements.txt
2、配置好前面步骤的信息
3、命令行运行runner.py文件：python runner.py -s dmp -m report即可
非python环境： 命令行cmd模式下： runner -s dmp -m report 即可

- 注意点3：
套件中的接口部分有强关联性，以数据路由为例，如果global_environment.py
文件中配置的mysql不正确或者访问不到，会导致后续的rule（规则引擎）等接口
报错，因为是关联到一起的，报告中这个时候后续的大面积报错其实仅仅是因为这
一个配置信息导致的某一个接口错误导致。

```
