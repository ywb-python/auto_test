#!/usr/bin/env python
# coding: utf-8


import unittest
from selenium import webdriver
from ddt import data,unpack,ddt


def getData():
    """
    数据分离出来放到列表中
    :return:
    """
    return [
        ['123456789','122','手机格式不正确'],
        ['18721706546','12','输入的密码不正确']
    ]
@ddt
class DoubanLogin(unittest.TestCase):

    def setUp(self):
        print('开始登陆')
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://www.douban.com/')
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()
        print('结束登陆')



    @data(*getData())
    @unpack
    def test_login(self,tel,password,result):
        pwd_login = self.driver.find_element_by_class_name('account-tab-account')
        pwd_login.click()
        self.driver.find_element_by_id('username').send_keys(tel)
        self.driver.find_element_by_id('password').send_keys(password)
        login_button = self.driver.find_element_by_class_name('btn btn-account')
        login_button.click()
        actual_result = self.driver.find_element_by_class_name('fatal-msg hide').text
        self.assertEqual(actual_result,result)


if __name__ == '__main__':
    unittest.main(verbosity=2)
