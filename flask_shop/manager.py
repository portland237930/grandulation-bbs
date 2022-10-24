from flask_shop import app,db
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager,Shell
from flask_mail import Mail, Message
from threading import Thread
from flask_shop import models
from flask import request
from flask_shop.utils.message import to_dict_msg
import random
import copy
manager = Manager(app)
Migrate(app,db)
manager.add_command('db',MigrateCommand)
mail = Mail(app)
str=""

message='发送邮件成功'
str_copy=""
code=200
'''
# python manager.py db init   执行一次

python manager.py db migrate 生成表结构

python manager.py db upgrade 映射数据库

注意： main 一定写是manager.run()
'''
# 异步发送邮件
def send_async_email(app, msg):
    try:
        with app.app_context():
            global str
            global message
            global code
            mail.send(msg)
            code=200
            str=str_copy
            message="发送邮件成功"
    except Exception as e:
        print(e) 
        str=""
        message="邮箱不存在"
        code=500
        
@app.route('/send_email',methods=['GET'])
def index():
    email=request.args.get("email")
    global str
    global message
    global str_copy
    str=""
    for i in range(6):
        ch = chr(random.randrange(ord('0'), ord('9') + 1))
        str += ch
    str_copy=str
    msg = Message(subject='邮箱验证码',
                sender="2279789157@qq.com",  # 需要使用默认发送者则不用填
                recipients=[email])
    # 邮件内容会以文本和html两种格式呈现，而你能看到哪种格式取决于你的邮件客户端。
    msg.body = str
    thread = Thread(target=send_async_email, args=[app, msg])
    thread.start()
    thread.join()
    print(message,str)
    return {'msg':message,'code':code,'data':str}

if __name__ == "__main__":
    # app.run() 
    manager.run()