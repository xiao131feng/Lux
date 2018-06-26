from utils import base
class Area(base.Page):
    '''首页'''
    def ljcookie(self):
        '''获取cookie'''
        ck = self.driver.get_cookie()
        name = ck[0]["name"]
        value = ck[0]["value"]
        lhcookie = name + "=" + value
        return lhcookie
    def hqsy(self):
        self.driver.

    