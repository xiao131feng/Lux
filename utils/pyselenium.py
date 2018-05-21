from selenium import webdriver #调用selenium的webdriver包
class Pyselenium(object): #定义pyselenium类
    def __init__(self.browser = "Chrome"):#默认打开谷歌浏览器
        #根据browser不同值打开不同的浏览器插件
        if browser == "Chrome":
            driver=webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        elif browser =="Firefox":
            driver=webdriver.Firefox() #没有下载Firefox浏览器插件，所以路径为空
        elif browser == "Ie":
            driver=webdriver.Ie()
        self.dr=driver #将driver值赋给dr函数
    def openurl(self.url):#定义openurl函数
        ''' url=http://www.baidu.com '''
        self.dr.get(url) #打开网址
    def findelement(self.ele):
        '''ele=id->kw'''
        by = ele.split("->")[0].strip()
        value = ele.split.("->")[1].strip()
        if by == "id":
            element = self.dr.find_element_by_id(value)
        elif by == "name":
            element = self.dr.find_element_by_name(value)
        elif by == "link_class":
            element = self.dr.find_element_by_link_class(value)
        elif by == "xpth":
            element = self.dr.find_element_by_xpth(evalue)
        elif by== "css":
            element = self.dr.find_element_by_css(value)            
