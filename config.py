

#开发环境
class Developconfig:
    DEBUG = True  #调试模式
    HOST = "0.0.0.0"
    


#产品环境
class Productionconfig:
    DEBUG = False  #调试模式 
    HOST = "0.0.0.0"


flask_config = {
    "Developconfig" :Developconfig,
    "Productionconfig":Productionconfig
}    
# flask_config["Developconfig"]  # 环境调用