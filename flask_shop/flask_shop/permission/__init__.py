from flask import Blueprint
from flask_restful import Api
permission=Blueprint('menu',__name__)
permission_api=Api(permission)
from flask_shop.permission import view