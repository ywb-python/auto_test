#!/usr/bin/env python
# coding: utf-8


import unittest
import os
import time
import HTMLTestRunner


def allcase():
    """
    获取所有的测试用例
    discover():
    start_dir;测试模块的路径，存放在testCase包中
    pattern:获取模块文件的规则

    :return:
    """
    suite = unittest.TestLoader().discover(start_dir=os.path.dirname(__file__), pattern='test*.py', top_level_dir=None)
    return suite

def get_current_time():
    """
    获取当前时间
    :return:
    """
    return time.strftime("%Y-%m-%d %H_%M_%S", time.localtime(time.time()))


def run():
    file_name = os.path.join(os.path.dirname(__file__),'report',get_current_time() + 'report.html')
    fp = open(file_name, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='UI自动化测试报告',description='UI自动化测试报告详细信息')
    runner.run(allcase())


if __name__ == '__main__':
    run()