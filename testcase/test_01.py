import unittest
from selenium import webdriver
import time
class TestDemo(unittest.TestCase):
    '''第一个测试模块'''
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="./drivers/chromedriver.exe")
        cls.driver.get("https://www.baidu.com/")
        print("开始测试！")
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("结束测试！")
    def test_01(self):
        '''第1个测试用例'''
        print("正在执行第1个测试用例")
        self.driver.find_element_by_id("kw").send_keys("浪晋的测试小讲堂")
        self.driver.find_element_by_id("su").click
        time.sleep(5)             
        self.assertEqual(1*2,1,"1*1是否等于1")
    def test_02(self):
        '''第2个测试用例'''
        print("正在执行第2个测试用例")
        self.driver.find_element_by_id("kw").clear()
        self.driver.find_element_by_id("kw").send_keys("slenium test")
        self.driver.find_element_by_id("su").click
        time.sleep(5)     
        self.assertEqual(1+3,3,"1+2是否等于3")
    def test_03(self):
        '''第3个测试用例'''
        print("正在执行第3个测试用例")
        self.driver.find_element_by_id("kw").clear()
        self.driver.find_element_by_id("kw").send_keys("自动化测试")
        self.driver.find_element_by_id("su").click        
        self.assertEqual(3-2,2,"3-2是否等于2")
    def test_04(self):
        '''第4个测试用例'''
        print("正在执行第4个测试用例")
        self.assertEqual(4/1,2,"4/2是否等于2")


    # unittest.main()        
    # with open('UnittestTextReport.txt', 'a') as h:
    #     runner = unittest.TextTestRunner(stream=h, verbosity=2)
    # runner.run(suite)        
              

     
       
        
       





