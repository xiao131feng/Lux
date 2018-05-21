import unittest
from utils.pyselenium import Pyselenium
from utils import webconfig
import time
@classmethod
def setUpclass(cls):
    driver = Pyselenium(webconfig.browser) #在pyselenium类中调用webconfig的browser值并赋值给driver
    driver.openurl("https://www.baidu.com") #调用openurl函数
    time.sleep(5)
    print("开始测试！")
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("结束测试！")
    def test_01(self):
        '''第1个测试用例'''
        print("正在执行第1个测试用例")
        self.driver.find_element_by_xpath("//*[@id=\"kw\"]").send_keys("浪晋的测试小讲堂")
        self.driver.find_element_by_xpath("//*[@id=\"su\"]").click
        time.sleep(5)             
        self.assertEqual(1*2,1,"1*1是否等于1")
    def test_02(self):
        '''第2个测试用例'''
        print("正在执行第2个测试用例")
        self.driver.find_element_by_xpath("//*[@id=\"kw\"]").clear()
        self.driver.find_element_by_xpath("//*[@id=\"kw\"]").send_keys("selenium")
        self.driver.find_element_by_xpath("//*[@id=\"su\"]").click
        time.sleep(5)     
        self.assertEqual(1+3,3,"1+2是否等于3")
    def test_03(self):
        '''第3个测试用例'''
        print("正在执行第3个测试用例")
        self.driver.find_element_by_xpath("//*[@id=\"kw\"]").clear()
        self.driver.find_element_by_xpath("//*[@id=\"kw\"]").send_keys("自动化")
        self.driver.find_element_by_xpath("//*[@id=\"su\"]").click      
        self.assertEqual(3-2,2,"3-2是否等于2")
    def test_04(self):
        '''第4个测试用例'''
        print("正在执行第4个测试用例")
        self.assertEqual(4/1,2,"4/2是否等于2")