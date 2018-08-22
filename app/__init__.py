from flask import Flask,Blueprint
from config import flask_config
#声明蓝本bp，作用是将users.py和admin.py分层开发
bp = Blueprint("bp",__name__)
#web操作对象
def create_app(config_name = "Developconfig"):
    '''
    创建APP对象方法
    '''
    # 初始化flask对象
    app = Flask(__name__)
    #从config文件夹加载flask配置
    config = flask_config[config_name]
    app.config.from_object(config)
    
    #注册蓝本
    app.register_blueprint(bp)


    return app