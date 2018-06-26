import unittest
import time
import requests
from pageobject.login import Login
from selenium import webdriver
from utils import pyselenium
import webconfig
class Test_login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver =  pyselenium.Pyselenium(webconfig.browser)
        login = Login(cls.driver)
        login.dlsy()
        login.srzh()
        login.srma()
        login.djdl()
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()      
    def test_01_login(self):
        ck=self.driver.get_cookies()
        print(ck)
        name=ck[0]["name"]
        value=ck[0]["value"]
        global lhcookie
        lhcookie = name+"="+value
        sy=self.driver.find_element_by_xpath("//*[@id=\"app_sidebar\"]/div/nav/ul/li[2]/a/span").text
        self.assertEqual(sy,"首页")
    def test_02_help(self):
        self.driver.find_element_by_xpath("//*[@id=\"app_header\"]/header/nav/div[2]/ul[3]/li[3]/a").click()
        time.sleep(10)
        hp=self.driver.find_element_by_xpath("/html/body/div/div/div[1]/div/div/div/div").text
        self.assertEqual(hp,"帮助中心")
    def test_03_find(self):
        self.driver.get("http://183.239.209.132:8081/Card")
        self.driver.find_element_by_xpath("//*[@id=\"Type\"]/option[2]").click()
        self.driver.find_element_by_xpath("//*[@id=\"page\"]/div/div[2]/div[2]/div/div[1]/form/div[3]/button[2]").click()
        time.sleep(10)
        lsum=self.driver.find_element_by_xpath("//*[@id=\"page\"]/div/div[2]/div[2]/div/div[2]/div/div/div/ul/span").text
        url = "http://183.239.209.132:8081/Card/DoorCardQuery"

        querystring = {"pageIndex":"1","pageSize":"10"}

        payload = "{\"AreaId\":1,\"HouseId\":\"\",\"CardNo\":\"\",\"IdCardNo\":\"\",\"TenantName\":\"\",\"Status\":\"\",\"Type\":\"0\",\"IsPrivilige\":\"\",\"BeginTime\":\"\",\"EndTime\":\"\",\"SortFieldName\":\"\",\"SortType\":\"\"}"
        headers = {
            'Content-Type': "application/json",
            'Cookie': lhcookie
             }

        response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
        lheate=response.json()
        Total="总共"+str(lheate["PageInfo"]["Total"])+"条"
        self.assertEqual(lsum,Total)

    
# if __name__ == '__main__':
#     unittest.main()
       


