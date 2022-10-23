from flask_shop import app,db
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
from flask import Flask
from flask_shop import models
from flask_admin import Admin, BaseView, expose
manager = Manager(app)
Migrate(app,db)
manager.add_command('db',MigrateCommand)
'''
# python manager.py db init   执行一次

python manager.py db migrate 生成表结构

python manager.py db upgrade 映射数据库

注意： main 一定写是manager.run()
'''

if __name__ == "__main__":
    # app.run() 
    manager.run()