from flask import Blueprint
from flask_restful import Api

wxuser = Blueprint('wxuser',__name__,url_prefix='/wxuser')
wxuser_api = Api(wxuser)
from flask_shop.wxuser import view