from flask_shop.user import user,user_api
from flask_shop import models,db
from flask import request,current_app
from flask_restful import Resource,reqparse
import re
from flask_shop.utils.md5 import md5_file
from flask_shop.utils.message import to_dict_msg
from flask_shop.utils.tokens import generate_auth_token,verify_auth_token,login_required
@user.route('/')
def index():
    return "User Hello!!!"
# 用户接口
class User(Resource):
    """用户功能"""
    def get(self):
        """获取用户信息

        @@@
        ### description
        > 获取用户信息

        ### args
        |  args | nullable | request type | type |  remarks |
        |-------|----------|--------------|------|----------|
        |  id   |  false   |    body      | int  | user id  |

        ### request
        ```json
        {"id": "xxx"}
        ```

        ### 用户获取成功返回
        ```json
        {"status": 200, "msg": "获取成功", "data": {}}
        ```
        ### 找不到用户返回
        ```json
        {"status": 200, "msg": "没有此用户"}
        ```      
        ### 错误返回
        ```json
        {"status": 20000, "msg": "异常错误"}}
        ```   
        @@@
        """
        try:
            id = int(request.args.get('id').strip())
            usr = models.User.query.filter_by(id = id).first()
            # res=usr.to_dict()
            # res.role=role
            if usr:
                return to_dict_msg(200,usr.to_dict(),'获取用户成功！')
            else:
                return to_dict_msg(200,[],'没有此用户！')
        except Exception as e:
            print(e)
            return to_dict_msg(20000)

    def post(self):
        """用户注册

        @@@
        ### description
        > 获取用户信息

        ### args
        |  args | nullable | request type | type |  remarks |
        |-------|----------|--------------|------|----------|
        |isadmin|  true    |    query     | str |  isadmin  |
        |  name   |  false   |    query      | str  | 用户名 |
        |  pwd   |  false   |    query      | str  | 密码  |
        |  real_pwd   |  false   |    query      | str  | 重复密码  |
        |  nick_name   |  false   |    query      | str  | 昵称  |
        |  phone   |  false   |    query      | str  | 电话号码  |
        |  email   |  false   |    query      | int  | 用户邮箱  |

        ### request
        ```json
        {
            "name": "xxx",
            'pwd':'xxx',
            'real_pwd':'xxx',
            'nick_name':"xxx",
            'phone':'xxx'
            'email':'xxx'
        }

        ### 用户获取成功返回
        ```json
        {"status": 200, "msg": "注册成功"}
        ```
        ### 用户名不合法返回
        ```json
        {"status": 10011, "msg": "用户名不合法"}
        ```      
        ### 密码不合法返回
        ```json
        {"status": 10012, "msg": "密码不合法"}
        ```
        ### 二次密码不一致返回
        ```json
        {"status": 10013, "msg": "二次密码不一致"}
        ```
        ### 手机号不合法返回
        ```json
        {"status": 10014, "msg": "手机号不合法"}
        ```
        ### 二次密码不一致返回
        ```json
        {"status": 10013, "msg": "二次密码不一致"}
        ```
        ### 错误返回
        ```json
        {"status": 10015, "msg": "邮箱不合法"}}
        ```   
        @@@
        """
        isadmin=request.form.get('isadmin') if request.form.get('isadmin') else ''
        name = request.form.get('name') 
        # 用户名唯一
        isnameexist=models.User.query.filter_by(name=name).first()
        if isnameexist:
            return to_dict_msg(10034)
        pwd = request.form.get('pwd')
        real_pwd = request.form.get('real_pwd')
        nick_name = request.form.get('nick_name')
        phone = request.form.get('phone')
        email = request.form.get('email')
        try:
            # 如果是后台管理添加用户
            if isadmin=='1':
                usr = models.User(name = name,password = pwd ,nick_name =nick_name,phone =phone,email = email,rid=1)
                db.session.add(usr)
                db.session.commit()
                return {'status':200,'msg':'成功！'} 
            else:
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
                usr = models.User(name = name,password = pwd ,nick_name =nick_name,phone =phone,email = email)
                db.session.add(usr)
                db.session.commit()
                return {'status':200,'msg':'注册成功！'}
        except Exception as e:
            return to_dict_msg(20000)
    def put(self):
        """用户注册

        @@@
        ### description
        > 获取用户信息

        ### args
        |  args | nullable | request type | type |  remarks |
        |-------|----------|--------------|------|----------|
        |isadmin|  true    |    query     | str |  isadmin  |
        |  name   |  false   |    query      | str  | 用户名 |
        |  pwd   |  false   |    query      | str  | 密码  |
        |  real_pwd   |  false   |    query      | str  | 重复密码  |
        |  nick_name   |  false   |    query      | str  | 昵称  |
        |  phone   |  false   |    query      | str  | 电话号码  |
        |  email   |  false   |    query      | int  | 用户邮箱  |

        ### request
        ```json
        {
            "name": "xxx",
            'pwd':'xxx',
            'real_pwd':'xxx',
            'nick_name':"xxx",
            'phone':'xxx'
            'email':'xxx'
        }
        ```

        ### 用户获取成功返回
        ```json
        {"status": 200, "msg": "修改数据成功！"}
        ```
        ### 指定用户不存在返回
        ```json
        {"status": 10018, "msg": "修改用户错误"}
        ```      
        ### 数据不完整返回
        ```json
        {"status": 10000, "msg": "数据不完整"}
        ```   
        @@@
        """
        try:
            # 获取参数
            id  = int(request.form.get('id')) if request.form.get("id") else 0
            name=request.form.get("name") if request.form.get("name") else ''
            nick_name=request.form.get('nick_name') if request.form.get("nick_name") else ''
            email = request.form.get('email') if request.form.get("email") else ''
            phone = request.form.get('phone') if request.form.get("phone") else ''
            personal_info=request.form.get("personal_info") if request.form.get("personal_info") else ''
            avatar_url=request.form.get('avatar_url') if request.form.get("avatar_url") else ''
            # 根据id获取用户
            usr = models.User.query.get(id)
            if usr:
                # 更改信息
                usr.name=name
                usr.nick_name=nick_name 
                usr.email = email
                usr.phone = phone
                usr.personal_info=personal_info 
                usr.avatar_url=avatar_url
                db.session.commit()
                return to_dict_msg(200,msg='修改数据成功！')
            else:
                return to_dict_msg(10018)
        except Exception as e:
            print(e)
            return to_dict_msg(20000)
    def delete(self):
        """删除用户信息

        @@@
        ### description
        > 获取用户信息

        ### args
        |  args | nullable | request type | type |  remarks |
        |-------|----------|--------------|------|----------|
        |  id   |  false   |    body      | int  | user id  |

        ### request
        ```json
        {"id": "xxx"}
        ```

        ### 用户获取成功返回
        ```json
        {"status": 200, "msg": "删除成功"}
        ```
        ### 删除错误返回
        ```json
        {"status": 10019, "msg": "删除错误"}
        ```      
        ### 错误返回
        ```json
        {"status": 20000, "msg": "异常错误"}}
        ```   
        @@@
        """
        try:
            id  = request.args.get('id')
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
        """根据用户名模糊查询用户列表

        @@@
        ### description
        > 根据用户名模糊查询用户列表

        ### args
        |  args | nullable | request type | type |  remarks |
        |-------|----------|--------------|------|----------|
        |  name   |  false   |    body      | int  | 用户名  |
        |  pnum   |  false   |    body      | int  | 页数  |
        |  psize   |  false   |    body      | int  | 每页显示的页数  |

        ### request
        ```json
        {"id": "xxx"}
        ```

        ### 用户获取成功返回
        ```json
        {"status": 200, "msg": "删除成功"}
        ```   
        ### 错误返回
        ```json
        {"status": 20000, "msg": "异常错误"}}
        ```   
        @@@
        """
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
    """用户登录

    @@@
    ### description
    > 用户登录

    ### args
    |  args | nullable | request type | type |  remarks |
    |-------|----------|--------------|------|----------|
    |  name   |  false   |    query      | str  | 用户名  |
    |  pwd   |  false   |    query      | str  | 密码  |

    ### request
    ```json
    {
        "name": "xxx"
        "pwd": "xxx"
    }
    ```

    ### 用户获取成功返回
    ```json
    {"status": 200, "msg": "登录成功"}
    ``` 
    ### 错误返回
    ```json
    {"status": 20000, "msg": "异常错误"}}
    ```   
    @@@
    """
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
                current_app.logger.info("user: "+name+" Login")
                return to_dict_msg(200,data={'token':token,'uid':usr.id},msg="登录成功")
    return  {'status':10001,'msg':'用户名或密码错误'}

@user.route('/reset',methods=['GET'])
# 重置密码接口
def reset():
    """重置密码接口

    @@@
    ### description
    > 重置密码接口

    ### args
    |  args | nullable | request type | type |  remarks |
    |-------|----------|--------------|------|----------|
    |  id   |  false   |    body      | str  | 用户id  |

    ### request
    ```json
    {
        "id": "xxx"
    }
    ```

    ### 重置密码成功返回
    ```json
    {"status": 200, "msg": "重置密码成功！"}
    ``` 
    ### 错误返回
    ```json
    {"status": 20000, "msg": "异常错误"}}
    ```   
    @@@
    """
    try:
        id = int(request.args.get('id'))
        usr = models.User.query.get(id)
        usr.password = '123'
        db.session.commit()
        return to_dict_msg(200,msg = '重置密码成功！')
    except Exception as e:
        return to_dict_msg(20000)

# 上传头像接口
@user.route('/upload_img', methods=['POST'])
def upload_img():
    """上传图片接口

    @@@
    ### description
    > 上传图片接口

    ### args
    |  args | nullable | request type | type |  remarks |
    |-------|----------|--------------|------|----------|
    |  img_file   |  false   |    body      | file  | 头像图片  |

    ### request
    ```json
    {
        "id": "xxx"
    }
    ```

    ### 重置密码成功返回
    ```json
    {"status": 200, "msg": "重置密码成功！"}
    ``` 
    ### 没有上传文件返回
    ```json
    {"status": 10023, "msg": "没有上传文件"}}
    ```   
    ### 错误返回
    ```json
    {"status": 10024, "msg": "文件格式不符合规范"}}
    ```  
    ### 错误返回
    ```json
    {"status": 20000, "msg": "异常错误"}}
    ```  
    @@@
    """
    try:
        # 获取字段
        img_file = request.files.get('file')
        # 数据查询
        if not img_file and not usr:
            return to_dict_msg(10023)
        if allowed_img(img_file.filename):
            # 上传配置
            floder = current_app.config.get('SERVER_IMG_UPLOADS')
            # 分割字段
            end_prefix = img_file.filename.rsplit('.', 1)[1]
            # 名称加密
            file_name = md5_file()
            img_file.save(f'{floder}/{file_name}.{end_prefix}')
            url=f'http://127.0.0.1:5000/static/img/{file_name}.{end_prefix}'
            path= f'/static/img/{file_name}.{end_prefix}'
            data = {
                'path':path,
                'url': url
            }
            current_app.logger.info("upload: "+img_file+" Success")
            return to_dict_msg(200, data, '上传图片成功！！')
        else:
            current_app.logger.warning("upload: "+img_file+" Failed")
            return to_dict_msg(10024)
    except Exception as e:
        print(e)
        return to_dict_msg(20000)
    
def allowed_img(filname):
    return '.' in filname and filname.rsplit('.', 1)[1] in current_app.config['ALLOWED_IMGS']

@user.route("/avatar_url", methods=["PUT"])
def avatar_url():
    """更改头像接口

    @@@
    ### description
    > 更改头像接口

    ### args
    |  args | nullable | request type | type |  remarks |
    |-------|----------|--------------|------|----------|
    |  id   |  false   |    body      | str  | 用户id  |
    |  url   |  false   |    body      | str  | 用户头像地址  |

    ### request
    ```json
    {
        "id": "xxx",
        'url':'http:/example.com/xxxx.jpg'
    }
    ```

    ### 重置密码成功返回
    ```json
    {"status": 200, "msg": "重置密码成功！"}
    ``` 
    ### 没有此数据返回
    ```json
    {"status": 10022, "msg": "没有此数据"}}
    ```     
    ### 错误返回
    ```json
    {"status": 20000, "msg": "异常错误"}}
    ```  
    @@@
    """
    try:
        id=int(request.form.get('id').strip())
        url=request.form.get('url')
        usr=models.User.query.get(id)
        if usr and url:
            usr.avatar_url=url
            db.session.commit()
            current_app.logger.info("添加头像: "+url+" Success")
            return to_dict_msg(200,msg='上传头像成功')
        else:
            current_app.logger.warning("添加头像: "+url+" Fail")
            return to_dict_msg(10022)
    except Exception as e:
        print(e)
        return to_dict_msg(20000)
@user.route("/alluser",methods=['GET'])
def alluser():
    """更改头像接口

    @@@
    ### description
    > 更改头像接口

    ### 重置密码成功返回
    ```json
    {"status": 200, "msg": "获取用户成功！"}
    ``` 
    ### 没有此数据返回
    ```json
    {"status": 200, "msg": "没有此用户！"}}
    ```     
    ### 错误返回
    ```json
    {"status": 20000, "msg": "异常错误"}}
    ```  
    @@@
    """
    try:
        usr = models.User.query.all()
        # res=usr.to_dict()            # res.role=role
        if usr:
            ulist=[u.to_dict() for u in usr]
            return to_dict_msg(200,ulist,'获取用户成功！')
        else:
            return to_dict_msg(200,[],'没有此用户！')
    except Exception as e:
        print(e)
        return to_dict_msg(20000)

@user.route("/wx_login", methods=['GET'])
def wx_login():
    code=request.args.get("code")
    return code

# 测试用
@user.route('/test')
@login_required
def test_login_req():
    return to_dict_msg(200)

