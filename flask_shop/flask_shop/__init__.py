from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config_map
from flask_admin import Admin, BaseView, expose
from flask_docs import ApiDoc
db = SQLAlchemy()
# 初始化app
def create_app(config_name):
    app = Flask(__name__)

    obj = config_map.get(config_name)
    app.config.from_object(obj)
    # 自动化创建API文档
    ApiDoc(
    app,
    title="论坛API文档",
    version="1.0.0",
    description="论坛API",
    )
    db.init_app(app)
    # 蓝图注册
    from flask_shop.user import user
    app.register_blueprint(user)
    from flask_shop.role import role
    app.register_blueprint(role)
    from flask_shop.permission import permission
    app.register_blueprint(permission)
    from flask_shop.article import article
    app.register_blueprint(article)
    from flask_shop.comments import comments
    app.register_blueprint(comments)
    return app
app=create_app('develop')


if __name__ == "__main__":
    app.run()
