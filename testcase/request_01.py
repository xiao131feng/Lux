import reports


def get(self):
        '''
        get 方式
        '''
        try:
            respose = requests.get(url=url)
        except Exception as e:
            print(e)
        return respose

def post(url="",data={},headers={}，json={}):
        '''
        post 方法
        '''
        response = None
        try:
            response = requests.post(url=url,data=data,headers = headers,json = json)
        except Exception as e:
            print (e)
        return response
def testcase_addcases():
    url_index = "http://www.itblacklist.top:5000/"
    res_obj = get(url=url_index)
    print(res_obj.text)
    url_case = " http://www.itblacklist.top:5000/addtcass"
    datas = """
            {
            "request": "{\"url\": \"http://127.0.0.1:2333/test\", \"json\": {\"aaa\": \"bbb\"}, \"method\": \"POST\", \"headers\": {\"Content-Type\": \"application/json\"}, \"timeout\": 10}",
            "testname": "testcase99",
            "testtype": "testcass",
            "validate": "[{\"Equal\": [\"r.json()\",\"request[\\\\\"json\\\\\"]\"]},{\"Equal\": [\"r.status_code\",\"200\"]}]"
            }
          """
    headers = {"Content-Type":"application/json"}
    res_obj = post（url=url_case,data=datas,headers=headers)
    print(res_obj.text)
    url_querycass = "http://www.itblacklist.top:5000/querytcass"
    data = {"idlist":"1,2,3"}
    headers = {"Content-Type":"application/json"}
    res_ob = post(url=url_querycass,data=data,headers= headers)
    
    if res_obj.status_code == 200:
        print("添加测试用例成功！")    

if __name__ == '__main__':
    testcase_addcases()
