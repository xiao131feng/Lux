# Python+Selenium 自动化框架
# 第一章：概述
本框架使用Python+Selenium实现webUI自动化测试，并对其进行二次封装，通过二次封装将测试用例中使用的第三方插件单独保存，在测试用例中直接调用即可，使我们的代码简洁化、灵活化。
# 第二章：环境准备
python语法简洁优美, 功能强大, 标准库跟第三方库灰常强大, 应用领域非常广,入门比较简单非常使用新手使用的语言。
python入门可以参考：https://www.liaoxuefeng.com/
Selenium 通过编写模仿用户操作的 Selenium 测试脚本，可以从终端用户的角度来测试应用程序。通过在不同浏览器中运行测试，更容易发现浏览器的不兼容性
本框架需要安装python3和selenium，选择一个适合自己的IDE编写脚本，我是使用的vscode编写的。  
python和selenium的安装方法可以参考：https://blog.csdn.net/nanalinlinlin/article/details/54692114  
vscode安装地址：https://code.visualstudio.com/
# 第三章：项目结构
1.  testcase       # 用于存放测试用例  
    * test_case_01.py  #第一个测试用例
    * test_case_02.py  #第二个测试用例
2. drivers #用于存放浏览器插件     

    * chromedriver.exe # 谷歌浏览器插件
3. utils #用于存放第三方库  
    * HTMLTestRunner.py #生成网页的测试报告插件
4. reports #用于存放测试报告
5. run.py #作为整个自动化的入口
6. env #虚拟环境
# 第四章：第三方库介绍  
## 第三方库介绍
HTMLtestreport  
生成网页版的测试报告插件    
## 第三方库安装
Python3自带了pip包管理工具，可以让用户方便简单的对第三方的库进行安装管理。只需要在命令行输入pip install 【名字】 就可以安装了。 

安装selenium:   
建议在虚拟环境中安装selenium，在虚拟环境中运行时不会影响我们的正式环境。    
第一步：切换到我们的虚拟环境    










   



