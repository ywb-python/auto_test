#!/usr/bin/env python
# coding: utf-8


import unittest
from initTest import InitTest, InitTest2


class Test1(InitTest):
    def test_one(self):
        print('具体的测试用例')


class Test2(InitTest2):

    def test_one(self):
        print('第一个测试用例')

    def test_two(self):
        print('第二个测试用例')


if __name__ == '__main__':
    # main使用unittest.TestLoader类来查找和加载模块内的测试用例
    # verbosity:默认值为1，代表执行的测试总数和全局结果，2代表显示详细的信息
    unittest.main(verbosity=2)
