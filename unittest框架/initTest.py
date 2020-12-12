#!/usr/bin/env python
# coding: utf-8


import unittest

class InitTest(unittest.TestCase):
    """
     序列化.测试固件每次执行
    setUp()、tearDown()
    先执行setUp()，再执行具体测试用例，最后执行tearDown()
    """
    def setUp(self):
        print('开始执行')

    def tearDown(self):
        print('结束')

class InitTest2(unittest.TestCase):
    """
        2.测试固件支2执行一次
        setUpClass()、tearDownClass()
        该方法为类方法。使用该测试固件，无论有多少个测试用例，测试固件只执行一次
        """

    @classmethod
    def setUpClass(cls):
        print('start')

    @classmethod
    def tearDownClass(cls):
        print('end')

