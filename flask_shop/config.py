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
    # SERVER_NAME="txjava.cn:5000"
    SQLALCHEMY_DATABASE_URI = f'{MYSQL_DIALECT}+{MYSQL_DIRVER}://{MYSQL_NAME}:{MYSQL_PWD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}?charset={MYSQL_CHARSET}'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = os.urandom(16)
    MAIL_SERVER='smtp.qq.com'
    MAIL_PORT=465
    MAIL_PASSWORD="aekyayjvlbcxeade"
    MAIL_USE_TLS=False
    MAIL_USE_SSL=True
    MAIL_DEFAULT_SENDER="2279789157@qq.com"
    API_DOC_MEMBER=['user','role','permission','article','comment']
    MAIL_USERNAME='2279789157@qq.com'
    MAIL_SUPPRESS_SEND=False
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
    PORT=11010
    HOST='0.0.0.0'

config_map={
    'develop':DevelopmentConfig,
    'product':ProductionConfig
}