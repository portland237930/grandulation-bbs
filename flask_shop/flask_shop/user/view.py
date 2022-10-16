from flask_shop.user import user,user_api
from flask_shop import models,db
from flask import request
from flask_restful import Resource,reqparse
import re
from flask_shop.utils.message import to_dict_msg
from flask_shop.utils.tokens import generate_auth_token,verify_auth_token,login_required
@user.route('/')
def index():
    return "User Hello!!!"
# 用户接口
class User(Resource):
    def get(self):
        try:
            id = int(request.args.get('id').strip())
            usr = models.User.query.filter_by(id = id).first()
            if usr:
                return to_dict_msg(200,usr.to_dict(),'获取用户成功！')
            else:
                return to_dict_msg(200,[],'没有此用户！')
        except Exception as e:
            print(e)
            return to_dict_msg(20000)

    def post(self):
        name = request.form.get('name')
        pwd = request.form.get('pwd')
        real_pwd = request.form.get('real_pwd')
        nick_name = request.form.get('nick_name')
        phone = request.form.get('phone')
        email = request.form.get('email')

        # 验证数据的正确性
        if not all([name,pwd,real_pwd]):
            return to_dict_msg(10000)
        if len(name) <2:
            return to_dict_msg(10011)
        if len(pwd) <2:
            return to_dict_msg(10012)
        if pwd != real_pwd:
            return to_dict_msg(10013)
        if not re.match(r'1[345678]\d{9}',phone):
            return to_dict_msg(10014)
        if not re.match(r'^\w+((-\w+)|(\.\w+))*\@[A-Za-z0-9]+((\.|-)[A-Za-z0-9]+)*\.[A-Za-z0-9]+$',email):
            return to_dict_msg(10015)
        try:
            usr = models.User(name = name,password = pwd ,nick_name =nick_name,phone =phone,email = email)
            db.session.add(usr)
            db.session.commit()
            return {'status':200,'msg':'成功！'} 
        except Exception:
            return to_dict_msg(20000)
    def put(self):
        try:
            # 获取参数
            id  = int(request.form.get('id').strip())
            name=request.form.get("name").strip() if request.form.get('name') else ''
            nick_name=request.form.get('nick_name').strip() if request.form.get('nick_name') else ''
            email = request.form.get('email').strip() if request.form.get('email') else ''
            phone = request.form.get('phone').strip() if request.form.get('phone') else ''
            personal_info=request.form.get("personal_info").strip() if request.form.get('personal_info') else ''
            # 根据id获取用户
            usr = models.User.query.get(id)
            if usr:
                # 更改信息
                usr.name=name
                usr.nick_name=nick_name
                usr.email = email
                usr.phone = phone
                usr.personal_info=personal_info
                db.session.commit()
                return to_dict_msg(200,msg='修改数据成功！')
            else:
                return to_dict_msg(10018)
        except Exception as e:
            print(e)
            return to_dict_msg(10000)
    def delete(self):
        try:
            id  = request.json.get('id')
            usr = models.User.query.get(id)
            if usr:
                db.session.delete(usr)
                db.session.commit()
                return to_dict_msg(200,msg='删除成功！')
            else:
                return to_dict_msg(10019)
        except Exception as e:
            return to_dict_msg(20000)
# 获取所有用户
class UserList(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name',type=str)
        parser.add_argument('pnum',type=int)
        parser.add_argument('psize',type=int)
        try:
            args = parser.parse_args()
            name = args.get('name')
            pnum = args.get('pnum') if args.get('pnum') else 1
            psize = args.get('psize') if args.get('psize') else 2
            if name:
                users_p = models.User.query.filter(models.User.name.like(f'%{name}%')).paginate(pnum,psize)
            else:
                users_p = models.User.query.paginate(pnum,psize)
            data = {
                'pnum':pnum,
                'totalPage':users_p.total,
                'users':[u.to_dict() for u in  users_p.items]
            }
            return to_dict_msg(200,data,'获取用户列表成功！！')
        except Exception as e:
            print(e)
            return to_dict_msg(10000)
# 绑定URL
user_api.add_resource(UserList,'/user_list')
user_api.add_resource(User,'/user')

# 用户登录接口
@user.route('/login',methods=['POST'])
def login():
    name = request.form.get('name')
    pwd = request.form.get('pwd')
    if not all([name,pwd]):
        return {'status':10000,'msg':'数据不完整'}
    if len(name) >1:
        usr = models.User.query.filter_by(name =name).first()
        print(usr)
        if usr:
            if usr.check_password(pwd):
                token = generate_auth_token(usr.id,5)
                return to_dict_msg(200,data={'token':token,'uid':usr.id})
    return  {'status':10001,'msg':'用户名或密码错误'}

@user.route('/reset',methods=['GET'])
# 重置密码接口
def reset():
    try:
        id = int(request.args.get('id'))
        usr = models.User.query.get(id)
        usr.password = '123'
        db.session.commit()
        return to_dict_msg(200,msg = '重置密码成功！')
    except Exception as e:
        return to_dict_msg(20000)
# 测试用
@user.route('/test')
@login_required
def test_login_req():
    return to_dict_msg(200)