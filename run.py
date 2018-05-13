import unittest
from utils import HTMLTestRunner
suite = unittest.TestSuite()
# tests=[TestDemo("test_01"),TestDemo("test_02"),TestDemo("test_03"),TestDemo("test_04")]
suite = unittest.defaultTestLoader.discover(start_dir='./testcase', pattern='test*.py')
# suite.addTests(tests)
with open('./reports/HTMLReport2.html', 'wb+') as f:
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=f, title='测试报告', description='执行人：罗欢', verbosity=2)
    runner.run(suite) 