#!/usr/bin/env python
# coding: utf-8


import unittest
from initTest import InitTest2

class Load_Test_2(InitTest2):

    def test_luo(self):
        print('三国演义')

    def test_cao(self):
        print('1111')

    def test_wu(self):
        print('2222')

    def test_shi(self):
        print('333')

class test_other(InitTest2):

    def test_case_1(self):
        print('qqqqqqqqqqqqqqqqq')


if __name__ == '__main__':

    # makeSuite:按测试类执行
    suite = unittest.TestSuite(unittest.makeSuite(Load_Test_2))
    unittest.TextTestRunner(verbosity=2).run(suite)
