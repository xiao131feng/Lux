# from flask import Flask
from app import create_app
from app.resources import users,admin

app = create_app()


# 声明一个index的接口，这个接口支持get和post请求
# @app.route("/",methods=['get','post'])
# def index():
#     return "hello world!"


if __name__ == '__main__':
    app.run()

