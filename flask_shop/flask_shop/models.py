from flask_shop import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

# 基类,使每个表都拥有时间
class BaseModel:
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(
        db.DateTime, default=datetime.now, onupdate=datetime.now)

# 用户登录界面
class User(db.Model, BaseModel):
    __tablename__ = 't_user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True, nullable=False) # 用户名
    pwd = db.Column(db.String(128)) #密码
    nick_name = db.Column(db.String(32)) # 昵称
    phone = db.Column(db.String(11)) # 电话号码
    email = db.Column(db.String(32)) # 电子邮箱
    personal_info=db.Column(db.String(255)) #用户简介 
    role=(db.Column(db.Integer,default=1)) # 1普通用户 2管理员

    @property
    def password(self):
        return self.pwd

    @password.setter
    def password(self, t_pwd):
        self.pwd = generate_password_hash(t_pwd)

    def check_password(self, t_pwd):
        return check_password_hash(self.pwd, t_pwd)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'nick_name': self.nick_name,
            'phone': self.phone,
            'email': self.email,
            'role':self.role
        }
