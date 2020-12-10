#!/usr/bin/env python
# coding: utf-8


import unittest
from initTest import InitTest

class Load_Test_1(InitTest):

    def test_luo(self):
        print('三国演义')

    def test_cao(self):
        print('红楼梦')

    def test_wu(self):
        print('西游记')

    def test_shi(self):
        print('水浒传')


if __name__ == '__main__':
    suite = unittest.TestSuite()
    # addTest:按顺序添加，添加的顺序来执行
    suite.addTest(Load_Test_1('test_three'))
    suite.addTest(Load_Test_1('test_two'))
    suite.addTest(Load_Test_1('test_one'))
    unittest.TextTestRunner(verbosity=2).run(suite)
    # # makeSuite:按测试类执行
    # # suite = unittest.TestSuite(unittest.makeSuite(Test1))
    # # unittest.TextTestRunner(verbosity=2).run(suite)
    # # TestLoader():加载测试类
    # suite = unittest.TestLoader().loadTestsFromTestCase(Test1)
    # unittest.TextTestRunner(verbosity=2).run(suite)