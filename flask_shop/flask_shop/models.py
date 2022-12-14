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
    rid=db.Column(db.Integer,db.ForeignKey('t_role.id',ondelete="SET NULL")) # 角色id
    aid=db.relationship("Article",backref="user") # 一对多
    cid=db.relationship("Comment",backref="cuser") # 一对多
    tid=db.relationship("Thumb",backref="tuser",uselist=False) #一对多
    tid=db.relationship("Viewed",backref="vuser",uselist=False) #一对多
    # user=db.relationship("WxUser",uselist=False,backref='User')
    
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
            'role':Role.query.get(self.rid).to_dict() if self.rid else {}
        }

# 角色表
class Role(db.Model,BaseModel):
	__tablename__ ='t_role'
	id=db.Column(db.Integer,primary_key=True)
	name=db.Column(db.String(32),unique=True,nullable=False)# 角色名
	desc=db.Column(db.String(64))
    # 设置用户表的关联字段
	users=db.relationship('User',backref="Role", lazy="dynamic")
	permission=db.relationship('Permission',secondary=trm) # 多对多关联
	def to_dict(self):
		return {
			'id':self.id,
			'name':self.name,
			'desc':self.desc,
            'permission':[p.to_dict() for p in self.permission]
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
    content=db.Column(db.String(20000)) # 文章内容 
    cover=db.Column(db.String(255)) # 文章封面
    pid=db.Column(db.Integer,db.ForeignKey('t_user.id'))
    cid=db.relationship("Comment",backref="article")
    tid=db.relationship("Thumb",backref="thumb_article",uselist=False)
    vid=db.relationship("Viewed",backref="viewed_article",uselist=False)
    def to_dict(self):
        return {
            'id':self.id if self.id else 0,
            'title':self.title if self.title else '',
            'viewed':self.viewed if self.viewed else 0,
            'thumb':self.thumb if self.thumb else 0,
            'content':self.content if self.content else 0,
            'cover':self.cover if self.cover else '',
            'create_time':str(self.create_time) if self.create_time else '',
            'update_time':str(self.update_time) if self.update_time else '',
            'commentlist':[c.to_dict() for c in self.cid] if self.cid else [],
            'user':User.query.get(self.pid).to_dict() if self.pid else {}
        }

# 评论表
class Comment(db.Model,BaseModel):
    __tablename__ = 'comments'
    id=db.Column(db.Integer,primary_key=True)
    content=db.Column(db.String(255))
    thumb=db.Column(db.Integer,default=0)
    aid=db.Column(db.Integer,db.ForeignKey("t_article.id"))
    uid=db.Column(db.Integer,db.ForeignKey("t_user.id"))
    def to_dict(self):
        return {
            'id':int(self.id) if self.id else 0,
            'owner':User.query.get(self.uid).name if User.query.get(self.uid) else '',
            'create_time':str(self.create_time) if self.create_time else '',
            'update_time':str(self.update_time) if self.update_time else '',
            'content': self.content if self.content else '',
            'thumb':self.thumb if self.thumb else 0
        }
# 微信绑定用户表
class WxUser(db.Model,BaseModel):
    __tablename__ = 't_wxuser'
    id=db.Column(db.Integer,primary_key=True)
    wxid=db.Column(db.String(255),nullable=False)
    nick_name=db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey("t_user.id"),unique=True)
    users = db.relationship("User", backref=db.backref("User"), uselist=False)
    avatar_url=db.Column(db.String(255))
    def to_dict(self):
        return {
            'id':int(self.id) if self.id else 0,
            'nick_name':self.nick_name if self.nick_name else '',
            'avatar_url':self.avatar_url if self.avatar_url else ''
        }

# 点赞表
class Thumb(db.Model):
    __tablename__="t_thumb"
    id=db.Column(db.Integer,primary_key=True)
    uid=db.Column(db.Integer,db.ForeignKey('t_user.id'))
    aid=db.Column(db.Integer,db.ForeignKey("t_article.id"))
    isthumb=db.Column(db.Boolean,default=False) # 点赞状态
    def to_dict(self):
        return {
            'uid':int(self.uid) if self.uid else 0,
            'aid':int(self.aid) if self.aid else 0
        }

# 浏览表
class Viewed(db.Model):
    __tablename__="t_viewed"
    id=db.Column(db.Integer,primary_key=True)
    uid=db.Column(db.Integer,db.ForeignKey('t_user.id'))
    aid=db.Column(db.Integer,db.ForeignKey("t_article.id"))
    isviewed=db.Column(db.Boolean,default=False) # 浏览状态
    def to_dict(self):
        return {
            'uid':int(self.uid) if self.uid else 0,
            'aid':int(self.aid) if self.aid else 0
        }