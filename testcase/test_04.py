from utils.pyrequests import httprequest
import unittest
# from utils.md5 import md5

class Test_O4(unittest.TestCase):
    def test_01(self):
        req = {
            "method": "POST",
            "url": "http://127.0.0.1:2333/login",
            "json": {
                "username": "admin",
                "password": "123456"
            },
            "headers": {
                'Content-Type': "application/json"
            }
        }
        response = httprequest(**req)
        hjson = response.json()
        global token
        token = hjson["data"]
        self.assertEqual(1,1)

    def test_02(self):
        req = {
            "method":"POST",
            "url" : "http://127.0.0.1:2333/chicktoken",
            "json" : {"token":token},
            "headers" : {'Content-Type': "application/json"}
        }
        response = httprequest(**req)
        print(response.text)

    def test_03(self):
        req = {
            "method":"GET",
            "url" : "http://127.0.0.1:2333/test",
            "json" : {
                "AreaId":48,
                "TenantName":"测试条数",
                "IdCardNo":"510902199110186524",
                "TelNo":"166625563638",
                "CardNo":"4294967204",
                "BeginTime":"2018-05-28T01:58:37.943Z",
                "EndTime":"2018-08-08T01:58:37.943Z"
                },
            "headers" : {'Content-Type': "application/json"}
        }
        response = httprequest(**req)
        print(response.text)
# if __name__ == '__main__':
#     unittest.main()