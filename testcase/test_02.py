
# a = 1
# b =2
# if a == b:
#     print("pass")
# else:
#     print("faile")


import unittest
#from selenium import webdriver
import time
import HTMLTestRunner
class TestDemo(unittest.TestCase):
    '''第一个测试模块'''
    # def setUp(self):
    #     print("\n开始执行用例！！！")

    # def tearDown(self):
    #     print("结束执行用例")

    @classmethod
    def setUpClass(cls):
        # cls.driver = webdriver.Chrome(executable_path="./drivers/chromedriver.exe")
        # cls.driver.get("https://www.baidu.com/")
        print("开始执行用例")

    @classmethod
    def tearDownClass(cls):
        # cls.driver.quit()
        print("结束执行")

    def test_01(self):
        '''第一个测试用例'''
        print("正在执行第一个用例")
        # self.driver.find_element_by_id("kw").send_keys("浪晋的测试小讲堂")
        # self.driver.find_element_by_id("su").click
        # time.sleep(5)
        self.assertEqual(1,3,"判断是否相等")

    def test_02(self):
        '''第2个测试用例'''
        print("正在执行第2个用例")
        # self.driver.find_element_by_id("kw").clear()
        # self.driver.find_element_by_id("kw").send_keys("slenium test")
        # self.driver.find_element_by_id("su").click
        # time.sleep(5)
        self.assertEqual(1,1)

    def test_03(self):
        '''第3个测试用例'''
        print("正在执行第3个用例")
        # self.driver.find_element_by_id("kw").clear()
        # self.driver.find_element_by_id("kw").send_keys("自动化测试")
        # self.driver.find_element_by_id("su").click
        # time.sleep(5)
        self.assertEqual(1,2,"判断是否相等")
        


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestDemo))

    tests = [TestDemo("test_01"), TestDemo("test_02"),TestDemo("test_03")]
    suite.addTests(tests)
    # suite = unittest.defaultTestLoader.discover(start_dir='.', pattern='test*.py')
    # with open('UnittestTextReport.txt', 'w') as h:
    #     runner = unittest.TextTestRunner(stream=h, verbosity=2)
    #     runner.run(suite)

    with open('HTMLReport.html', 'wb+') as f:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=f, title='测试报告', description='执行人：浪晋', verbosity=2)
        runner.run(suite)