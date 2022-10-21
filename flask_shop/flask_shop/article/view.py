from flask_shop.article import article,article_api
from flask_shop import models,db
from flask import request	
from flask_restful import Resource
import re
from flask_shop.utils.message import to_dict_msg

# 文章接口
class Article(Resource):
	# 获取指定文章
	def get(self):
		try:
			# 收集参数
			uid=int(request.args.get('uid').strip() if request.args.get('uid') else '')
			# 指定获取类型 list为指定用户所有文章 only 指定用户指定文章
			type=request.args.get('type')
			usr=models.User.query.get(uid)
			if type=='list' and uid:
				# 用户查询
				if usr.id==uid:
					articles=[]
					article=models.Article.query.filter_by(pid=uid).all()
					for a in article:
						articles.append(a.to_dict())
					return to_dict_msg(200,data=articles,msg="获取所有文章成功")
			if type=='only' and uid:
				# 获取文章参数
				aid=int(request.args.get('aid').strip() if request.args.get('aid') else '')
				if aid:
					art=models.Article.query.get(aid)
					if art:
						return to_dict_msg(200,data=art.to_dict(),msg="获取文章成功")
					else:
						return to_dict_msg(10026)
		except Exception as e:
			print(e)
			return to_dict_msg(20000)
	# 指定用户添加文章接口
	def post(self):
		try:
					# 收集参数
			id=int(request.form.get("id").strip())
			title=request.form.get('title').strip()
			content=request.form.get('content').strip()
			cover=request.form.get('cover').strip()
			usr=models.User.query.get(id)
			uid=usr.id
			# 如果用户存在
			if usr:
				# 创建文章
				art=models.Article(title=title,content=content,pid=uid,cover=cover)
				# 用户关联文章
				usr.aid.append(art)
				db.session.add(art)
				db.session.commit()
				return to_dict_msg(200,msg='创建文章成功')
			else:
				return to_dict_msg(200,msg='10025')
		except Exception as e:
			print(e)
			return to_dict_msg(20000)
	# 修改文章接口
	def put(self):
		try:
			# 获取指定参数
			uid=int(request.form.get('uid').strip()) if request.form.get('uid') else 0
			aid=int(request.form.get('aid').strip()) if request.form.get('aid') else 0
			content=request.form.get('content').strip()
			title=request.form.get('title').strip()
			cover=request.form.get('cover').strip()
			# 查询指定用户和指定文章
			usr=models.User.query.get(uid)
			art=models.Article.query.get(aid)
			# 如果用户和文章都存在
			if usr and art:
				art.content=content
				art.title=title
				art.cover=cover
				db.session.commit()
				return to_dict_msg(200,msg="修改文章成功")
			else:
				return to_dict_msg(10027)
		except Exception as e:
			print(e)
			return to_dict_msg(20000)
	def delete(self):
		try:
			uid=int(request.args.get('uid').strip()) if request.args.get('uid') else 0
			aid=int(request.args.get('aid').strip()) if request.args.get('aid') else 0
			usr=models.User.query.get(uid)
			art=models.Article.query.get(aid)
			# 如果查询成功
			if usr and art:
				db.session.delete(art)
				db.session.commit()
				return to_dict_msg(200,msg="删除成功")
			else:
				return to_dict_msg(10026)
		except Exception as e:
			print(e)
			return to_dict_msg(20000)
# 点赞数和评论数增加接口
@article.route("/addart",methods=["POST"])
def addthumb():
		try:
			# 获取用户id和文章id
			uid=int(request.args.get('uid').strip()) if request.args.get('uid') else 0
			aid=int(request.args.get('aid').strip()) if request.args.get('aid') else 0
			usr=models.User.query.get(uid)
			art=models.Article.query.get(aid)
			type=request.args.get('type').strip() if request.args.get('type') else ''
			if usr and art:
				if type=='thumb_add':
					art.thumb+=1
				elif type=='viewed_add':
					art.viewed+=1
				elif type=='thumb_reduce':
					art.thumb-=1 if art.thumb else 0
				elif type=='viewed_reduce':
					art.viewed-=1 if art.viewed else 0
				else:
					return to_dict_msg(10028)
				db.session.commit()
				return to_dict_msg(200,msg='成功')
		except Exception as e:
			print(e)
			return to_dict_msg(20000)
# 获取所有文章
@article.route("/getAllArticle",methods=['GET'])
def getAllArticle():
	try:
		type=request.args.get('type').strip() if request.args.get('type') else ''
		if type=='all':
			art=models.Article.query.all()
			alist=[a.to_dict() for a in art]
		elif type=='reo':
			art=models.Article.query.paginate(1,12)
			alist=[a.to_dict() for a in art.items]
		return to_dict_msg(200,data=alist,msg="获取成功")
	except Exception as e:
		print(e)
		return to_dict_msg(20000)

# 根据标题模糊查询
@article.route('/search',methods=['GET'])
def search():
	try:
		title=request.form.get('title')
		articles=models.Article.query.filter(
			models.Article.title.like("%"+title+"%") if title else ''
			).all()
			# 如果查询成功
		if articles:
			alist=[a.to_dict() for a in articles]
			return to_dict_msg(200,data=alist,msg="查询成功")
	except Exception as e:
		print(e)
		return to_dict_msg(20000)

article_api.add_resource(Article,'/article')