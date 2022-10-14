from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config_map

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    obj = config_map.get(config_name)
    app.config.from_object(obj)
    db.init_app(app)

    from flask_shop.user import user
    app.register_blueprint(user)
    return app


if __name__ == "__main__":
    app.run()
