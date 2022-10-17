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
    avatar_url=db.Column(db.String(255),default='') # 头像路径
    personal_info=db.Column(db.String(255)) #用户简介 
    rid=db.Column(db.Integer,db.ForeignKey('t_role.id')) # 角色id
    aid=db.relationship("Article",backref="user")
    @property
    def password(self):
        return self.pwd
    # 密码加密
    @password.setter
    def password(self, t_pwd):
        self.pwd = generate_password_hash(t_pwd)
    # 密码解密
    def check_password(self, t_pwd):
        return check_password_hash(self.pwd, t_pwd)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'nick_name': self.nick_name,
            'phone': self.phone,
            'email': self.email,
            # 'roles':self.rid if self.rid else '',
            'personal_info':self.personal_info if self.personal_info else '',
            'avatar_url':self.avatar_url if self.avatar_url else '',
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
	def to_dict(self):
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

class Article(db.Model,BaseModel):
    __tablename__ = 't_article'
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(255),nullable=False) # 文章标题
    viewed=db.Column(db.Integer,default=0) # 浏览次数
    thumb=db.Column(db.Integer,default=0) # 点赞数量
    content=db.Column(db.String(2000)) # 文章内容 
    pid=db.Column(db.Integer,db.ForeignKey('t_user.id'))
    cid=db.relationship("Comment",backref="article")
    def to_dict(self):
        return {
            'title':self.title if self.title else '',
            'viewed':self.viewed if self.viewed else '',
            'thumb':self.thumb if self.thumb else '',
            'content':self.thumb if self.thumb else ''
        }

# 评论表
class Comment(db.Model,BaseModel):
    __tablename__ = 'comments'
    id=db.Column(db.Integer,primary_key=True)
    content=db.Column(db.String(255))
    viewed=db.Column(db.Integer,default=0)
    thumb=db.Column(db.Integer,default=0)
    aid=db.Column(db.Integer,db.ForeignKey("t_article.id"))
    def to_dict(self):
        return {
            'content': self.content if self.content else '',
            'viewed':self.viewed if self.viewed else '',
            'thumb':self.thumb if self.thumb else ''
        }