from app import bp
from flask import request,jsonify
import base64


@bp.route("/",methods =['get','post'])
def index():
    return "hello world!"
@bp.route("/userLogin",methods=['post'])
def user_login():
    #接收json格式的数据，不限于username,password和captcha
    user_imfo = request.get_json()
    username = user_imfo.get("username")
    password = user_imfo.get("password")
    captcha = user_imfo.get("captcha")
    print("username is ={}".format(username))
    print("password is ={}".format(password))
    print("captcha is ={}".format(captcha))
    return "successful"
@bp.route("/Registered",methods=["post"])
def user_Registered():
    user_regi = request.get_json()
    username = user_regi.get("username")
    password = user_regi.get("password")
    avatar = user_regi.get("avatar")
    nickname = user_regi.get("nickname")
    if username == "" or password == "":        
        return "账号或密码不能为空,注册失败"
    elif username == "cc" and password =="cc":
        if avatar == '':
            return jsonify({'username':username,'password':password,'avatar':"串串",'nickname':nickname})
        else:
            return jsonify({'username':username,'password':password,'avatar':avatar,'nickname':nickname})
    else:
        return "账号或密码输入错误，注册失败"
        
        

    

        


