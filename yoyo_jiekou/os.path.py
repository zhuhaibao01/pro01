#coding=utf-8
import os
import time
import logging

# 1.os.path.abspath返回path规范下的绝对路径
print os.path.abspath('logger.py')
#  C:\Users\test\Desktop\yoyo_jiekou\logger.py
print os.path.abspath(__file__)
#  C:\Users\test\Desktop\yoyo_jiekou\os.path.py

# 2.os.patj.split(path) 把path分割成目录和文件名二元组返回。
print os.path.split('logger.py')

# 3.os.path.dirname(path)返回path的目录

# 返回当前文件的真实路径
print os.path.realpath('logger.py')
print os.path.realpath(__file__)
# 去掉文件，光返回目录
print os.path.dirname(os.path.realpath(__file__))
#目录加字符串名，合成目录
print os.path.join(os.path.dirname(os.path.realpath(__file__)),'logs')
#exists 内容为真返回True
if not os.path.exists(os.path.join(os.path.dirname(os.path.realpath(__file__)),'logs')):os.mkdir(os.path.join(os.path.dirname(os.path.realpath(__file__)),'logs'))
class Log():
    def __init__(self):
        #文件的命名
        self.logname=os.path.join(os.path.dirname(os.path.realpath(__file__)),'logs'),'%s.log'%time.strftime('%Y_%m_%d')
        self.log