# from utils import pyselenium
import webconfig
from utils import base
class Login(base.Page):
    '''登陆页面'''
           
    def dlsy(self):
        ''' 打开登陆地址'''
        self.driver.open(webconfig.url+"/Login")
    def srzh(self):
        ''' 输入登陆账号'''
        self.driver.send_keys("name-->UserName","admin")
    def srma(self):
        ''' 输入密码'''
        self.driver.send_keys("name-->Password","admin8118")
    def djdl(self):
        '''点击登陆'''
        self.driver.click("id-->btnLogin")



    
