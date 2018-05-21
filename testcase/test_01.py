import unittest
from selenium import webdriver #导入selenium中的webdriver包
import time #导入时间包
class TestDemo(unittest.TestCase):# 定义TesDemo类，继承unittest.TestCase
    '''第一个测试模块'''
    @classmethod
    def setUpClass(cls):#准备测试环境
        cls.driver = webdriver.Chrome(executable_path="./drivers/chromedriver.exe")#调起谷歌浏览器
        cls.driver.get("https://www.baidu.com/")#打开百度网页
        print("开始测试！")
    @classmethod
    def tearDownClass(cls):#测试用例全部执行完成之后清理测试环境
        cls.driver.quit()#退出浏览器
        print("结束测试！")
    def test_01(self):#定义第一个测试用例
        '''第1个测试用例'''
        print("正在执行第1个测试用例")
        # 使用selenium的xpath方法定位百度输入框xpath值，并在输入框中输入“浪晋的测试小讲堂”
        self.driver.find_element_by_xpath("//*[@id=\"kw\"]").send_keys("浪晋的测试小讲堂")                                                                                        
        self.driver.find_element_by_xpath("//*[@id=\"su\"]").click #点击[百度一下] 
        time.sleep(5)  #时间延迟5秒         
        # self.assertEqual(1*2,1,"1*1是否等于1")
    def test_02(self):
        '''第2个测试用例'''
        print("正在执行第2个测试用例")
        self.driver.find_element_by_xpath("//*[@id=\"kw\"]").clear() #清空搜索框
        self.driver.find_element_by_xpath("//*[@id=\"kw\"]").send_keys("selenium")#在搜索框中输入selenium
        self.driver.find_element_by_xpath("//*[@id=\"su\"]").click#点击[百度一下]
        time.sleep(5)     
        # self.assertEqual(1+3,3,"1+2是否等于3")
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


    # unittest.main()        
    # with open('UnittestTextReport.txt', 'a') as h:
    #     runner = unittest.TextTestRunner(stream=h, verbosity=2)
    # runner.run(suite)        
              

     
       
        
       





