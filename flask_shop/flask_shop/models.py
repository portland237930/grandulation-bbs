from flask_shop import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

# 基类,使每个表都拥有时间
class BaseModel:
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(
        db.DateTime, default=datetime.now, onupdate=datetime.now)

# 创建权限和角色的关联表
trm=db.Table('t_role_permission',
	db.Column('rid',db.Integer,db.ForeignKey('t_role.id')),
	db.Column('pid',db.Integer,db.ForeignKey('t_permission.id'))
)

# 用户
class User(db.Model, BaseModel):
    __tablename__ = 't_user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True, nullable=False) # 用户名
    pwd = db.Column(db.String(128)) #密码
    nick_name = db.Column(db.String(32)) # 昵称
    phone = db.Column(db.String(11)) # 电话号码
    email = db.Column(db.String(32)) # 电子邮箱
    personal_info=db.Column(db.String(255)) #用户简介 
    rid=db.Column(db.Integer,db.ForeignKey('t_role.id')) # 角色id

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
            'role_name':self.rid.name if self.rid else '',
            'permission':self.rid.permission if self.rid else '',
            'personal_info':self.personal_info if self.personal_info else ''
        }

# 角色表
class Role(db.Model,BaseModel):
	__tablename__ ='t_role'
	id=db.Column(db.Integer,primary_key=True)
	name=db.Column(db.String(32),unique=True,nullable=False)# 角色名
	desc=db.Column(db.String(64))
    # 设置用户表的关联字段
	users=db.relationship('User',backref="role")
	permission=db.relationship('Permission',secondary=trm) # 多对多关联
	def to_dict():
		return {
			'id':self.id,
			'name':self.name,
			'desc':self.desc,
		}
# 用户权限表
class Permission(db.Model,BaseModel):
	__tablename__ = 't_permission'
	id=db.Column(db.Integer,primary_key=True)
	name=db.Column(db.String(32)) # 权限名
	roles=db.relationship('Role',secondary=trm)
	def to_dict(self):
		return{
			'id':self.id,
			'name':self.name,
		}
