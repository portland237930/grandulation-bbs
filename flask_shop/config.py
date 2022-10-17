import os

class Config:
    # 配置MySQL参数
    MYSQL_DIALECT = 'mysql'
    MYSQL_DIRVER = 'pymysql'
    MYSQL_NAME = 'root'
    MYSQL_PWD = '123456'
    MYSQL_HOST = 'localhost'
    MYSQL_PORT = 3306
    MYSQL_DB = 'flaskbbs'
    MYSQL_CHARSET ='utf8mb4'
    RESTFUL_API_DOC_EXCLUDE=[]
    SQLALCHEMY_DATABASE_URI = f'{MYSQL_DIALECT}+{MYSQL_DIRVER}://{MYSQL_NAME}:{MYSQL_PWD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}?charset={MYSQL_CHARSET}'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = os.urandom(16)
    API_DOC_MEMBER=['user']
    # 使用 CDN
    API_DOC_CDN = True
    API_DOC_METHODS_LIST = ["GET", "POST", "PUT", "DELETE", "PATCH"]
    ALLOWED_IMGS = set(['bmp','png','jpg','jpeg','gif'])
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    SERVER_IMG_UPLOADS = os.path.join(BASE_DIR,'flask_shop','static','img') 
# 生产环境和开发环境
class DevelopmentConfig(Config):
    DEBUG = True
class ProductionConfig(Config):
    pass

config_map={
    'develop':DevelopmentConfig,
    'product':ProductionConfig
}