from flask import Blueprint
from flask_restful import Api
comments=Blueprint('comments',__name__)
comments_api=Api(comments)
from flask_shop.comments import view