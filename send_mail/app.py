from flask import Flask, request
from flask_script import Manager, Shell
from flask_mail import Mail, Message
from threading import Thread
app = Flask(__name__)
mail = Mail(app)
app.config['MAIL_SERVER'] = 'smtp.qq.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = '2279789157@qq.com'
app.config['MAIL_PASSWORD'] = "aekyayjvlbcxeade"
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_DEFAULT_SENDER'] = '2279789157@qq.com'
mail = Mail(app)
# 异步发送邮件
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

@app.route('/')
def index():
    msg = Message(subject='Hello World',
                  sender="2279789157@qq.com",  # 需要使用默认发送者则不用填
                  recipients=[ '2654784149@qq.com'])
    # 邮件内容会以文本和html两种格式呈现，而你能看到哪种格式取决于你的邮件客户端。
    msg.body = 'sended by flask-email'
    msg.html = '<b>测试Flask发送邮件<b>'
    thread = Thread(target=send_async_email, args=[app, msg])
    thread.start()
    return '<h1>邮件发送成功</h1>'


if __name__ == '__main__':
    app.run(debug=True,port=5001)