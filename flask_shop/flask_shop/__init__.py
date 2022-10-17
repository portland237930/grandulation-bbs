from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config_map
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

    from flask_shop.user import user
    app.register_blueprint(user)
    from flask_shop.role import role
    app.register_blueprint(role)
    from flask_shop.permission import permission
    app.register_blueprint(permission)
    return app


if __name__ == "__main__":
    app.run()
