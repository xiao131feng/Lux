import allure
from selenium import webdriver
import time
import requests
@allure.feature('testsuite1')
@allure.story('testcass1')
def test_minor():
    # allure.enviroment(country = 'contrys')
    with allure.step("打开百度"):
        @allure.attach("说明这个步骤"，"??")
        driver = webdriver.Chrome(executable_path='./drivers/chromedriver.exe')
        driver.get("http://www.baidu.com")
        allure True
    with allure.step("步骤二","搜索selenium"):
        @allure.attach("说明这个步骤"，"??")
        driver.find_elements_by_id('kw').send_keys("selenium")
        driver.find_element_by_id('su').click()
        time.sleep(10)
        allure True
    with allure.step("步骤三","退出浏览器"):
        @allure.attach("说明这个步骤"，"??")
        driver.quit()
        allure True  
@allure.title("测试报告")
@allure.severity("critical") # 优先级，包含blocker,critical,normal,minor,trivial 几个不同的等级
@allure.feature('testsuite2')
@allure.story('testcass2','testcass3')
@allure.story('testcass4')
class TestBar:
    def test_bar(self):
        @allure.attach("接口测试")
        assert True
    def test_bar2(self):
        with allure.step("步骤一"):
            @allure.attach("用户登陆")
            self.url = "http://183.239.209.132:8081/Login"
            self.data{}
            self.data["UserName"] = "admin"
            self.data["Password"] = "admin8118"
            self.res = requests.post(url,data)
            assert.True    
        with allure.step("步骤二"):
            @allure.attach("判断是否登陆成功")
            res_obj = eval(self.res.text)
            if res_obj["code"] == 200:
                print("登陆成功")
            elif:
                print("登陆成功")      
            assert.True           





    
