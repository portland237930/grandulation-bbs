'''
1. 加密的数据   uid
2. 算法     python模块
3. 秘钥     flask_app SECRET_KEY
'''

from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app,request
from flask_shop.models import User
from flask_shop.utils.message import to_dict_msg
import functools

def generate_auth_token(uid,expiration):
    # 创建加密对象
    s = Serializer(current_app.config['SECRET_KEY'],expires_in = expiration)
    # 生成token
    return s.dumps({'id':uid}).decode()

def verify_auth_token(token_str):
    # 创建解密对象
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token_str)
    except Exception:
        return None
    usr = User.query.filter_by(id = data['id']).first()
    return usr


def login_required(view_func):
    functools.wraps(view_func)
    def verify_token(*arg,**kwargs):
        try:
            token = request.headers['token']
        except Exception:
            return to_dict_msg(10016)
            # 创建解密对象
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except Exception as  e:
            print(e)
            return to_dict_msg(10017)
        return view_func(*arg,**kwargs)
    return verify_token