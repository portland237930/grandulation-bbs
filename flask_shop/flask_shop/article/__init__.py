from flask import Blueprint
from flask_restful import Api
article=Blueprint('article',__name__)
article_api=Api(article)
from flask_shop.article import view