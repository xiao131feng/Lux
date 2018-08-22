import requests
class RequestUtils:
    def __init__ (self,url="",data={},headers={}):    
        self.url = url
        self.data = data    
        self.headers = headers    
    def get(self):
        '''
        get 方式
        '''
        try:
            respose = requests.get(url=self.url)
        except Exception as e:
            print(e)
        return respose

    def post(self,url="",data={},headers={}):
        '''
        post 方法
        '''
        try:
            response = requests.post(url=self.url,data=self.data,headers = self.headers)
        except Exception as e:
            print (e)
        return response
def get_zhihu_tz():
    requests = []
    url = "https://www.zhihu.com/collection/123354652?page=1"   
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36","Host":"www.zhihu.com","Upgrade-Insecure-Requests":"1","authorization":"oauth c3cef7c66a1843f8b3a9e6a1e3160e20"}
    # 实例化
    req_obj = RequestUtils(url=url,headers=headers)
    res = req_obj.get()
    print(res.text)
if __name__== "__main__":
    # url = "http://www.itblacklist.tip:2333/login"
    # data = {}
    # data["username"] = "admin"
    # data["password"] = "123456"
    # req_obj = RequestUtils.(url=url,data=data)
    # reponse = resp.post()
    # print(reponse.text)

    # # resp = RequestUtils(url="http://www.baidu.com")
    # # reponse = resp.get()
    # # print(reponse.text)
    get_zhihu_tz()


    
