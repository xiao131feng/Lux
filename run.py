import unittest #调用utittest包
from utils import HTMLTestRunner #从utils中调用HTMLTestRunner包
suite = unittest.TestSuite() #构建测试用例集
# tests=[TestDemo("test_01"),TestDemo("test_02"),TestDemo("test_03"),TestDemo("test_04")]
#执行testcase中以test开头的用例
suite = unittest.defaultTestLoader.discover(start_dir='./testcase', pattern='test*.py') 
# suite.addTests(tests)
# 生成测试报告
with open('./reports/HTMLReport2.html', 'wb+') as f:
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=f, title='测试报告', description='执行人：罗欢', verbosity=2)
    # 执行测试
    runner.run(suite) 
