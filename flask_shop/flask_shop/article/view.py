from flask_shop.article import article,article_api
from flask_shop import models,db
from flask import request	
from flask_restful import Resource
import re
from flask_shop.utils.message import to_dict_msg
import datetime

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
			uid=int(request.form.get('uid').strip()) if request.form.get('uid') else 0
			aid=int(request.form.get('aid').strip()) if request.form.get('aid') else 0
			usr=models.User.query.get(uid)
			art=models.Article.query.get(aid)
			type=request.form.get("type")
			if usr and art:
				# 如果是浏览
				if type=='thumb':
					thumb=models.Thumb.query.filter_by(uid=uid,aid=aid).first()
					# 第一次点赞
					if thumb is None:
						thumb=models.Thumb(uid=uid,aid=aid,isthumb=True)
						db.session.add(thumb)
						art.thumb+=1
						db.session.commit()
						return to_dict_msg(200,data=thumb.isthumb,msg="点赞成功")
					elif thumb.isthumb ==False:
						thumb.isthumb=True
						art.thumb+=1
						db.session.commit()
						return to_dict_msg(200,data=thumb.isthumb,msg="点赞成功")
					elif thumb.isthumb==True:
						thumb.isthumb=False
						art.thumb-=1 if art.thumb else 0
						db.session.commit()
						return to_dict_msg(200,data=thumb.isthumb,msg='取消点赞成功')
					else:
						return to_dict_msg(10028)
				elif type=='viewed':
					viewed=models.Viewed.query.filter_by(uid=uid,aid=aid).first()
					# 第一次点赞
					if viewed is None:
						viewed=models.Viewed(uid=uid,aid=aid,isviewed=True)
						db.session.add(viewed)
						art.viewed+=1
						db.session.commit()
						return to_dict_msg(200,data=viewed.isviewed,msg="浏览成功")
					else:
						return to_dict_msg(10028)					
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
			pnum=int(request.args.get('pnum'))
			psize=int(request.args.get("psize"))
			art=models.Article.query.paginate(pnum,psize)
			alist=[a.to_dict() for a in art.items]
		return to_dict_msg(200,data=alist,msg="获取成功")
	except Exception as e:
		print(e)
		return to_dict_msg(20000)

# 根据标题模糊查询
@article.route('/search',methods=['GET'])
def search():
	try:
		title=request.form.get('title') if request.form.get("title") else request.args.get("title")
		articles=models.Article.query.filter(
			models.Article.title.like("%"+title+"%") if title else ''
			).all()
			# 如果查询成功
		if articles:
			alist=[a.to_dict() for a in articles]
			return to_dict_msg(200,data=alist,msg="查询成功")
		else:
			return to_dict_msg(10036)
	except Exception as e:
		print(e)
		return to_dict_msg(20000)

article_api.add_resource(Article,'/article')
@article.route("/updateArticle",methods=['PUT'])
def updateArticle():
	try:
		id=request.form.get('id')
		content=request.form.get('content')
		title=request.form.get('title')
		cover=request.form.get('cover')
		thumb=int(request.form.get('thumb')) if request.form.get('thumb') else 0
		viewed=int(request.form.get('viewed')) if request.form.get('viewed') else 0
		article=models.Article.query.get(id)
		if article:
			article.content=content
			article.title=title
			article.cover=cover
			article.thumb=thumb
			article.viewed=viewed
			db.session.commit()
			return to_dict_msg(200,msg='修改文章成功')
		else:
			return to_dict_msg(10026)
	except Exception as e:
		print(e)
		return to_dict_msg(20000)

@article.route("/deleteArticle",methods=["DELETE"])
def deleteArticle():
	try:
		id=request.args.get("id")
		article=models.Article.query.get(id)
		if article:
			db.session.delete(article)
			db.session.commit()
			return to_dict_msg(200,msg='删除成功')
		else:
			return to_dict_msg(10026)
	except Exception as e:
		print(e)
		return to_dict_msg(20000)
# 获取文章数量
@article.route("/countArticle",methods=['GET'])
def countArticle():
	try:
		num=models.Article.query.count()
		if num:
			return to_dict_msg(200,data=num,msg="获取成功")
	except Exception as e:
		print(e)
		return to_dict_msg(20000)
# 获取文章数据量
@article.route("/countArticleByDate",methods=['GET'])
def countArticleByDate():
	try:
		type=request.args.get("type") if request.args.get('type') else ''
		init_date = datetime.datetime.today()
		if type=='month':
			restime = datetime.date(year=init_date.year, month=init_date.month, day=1)
		if type=='week':
			restime = init_date - datetime.timedelta(days=init_date.weekday())			
		if type=='quarter':
			restime = init_date.month / 3 if init_date.month % 3 == 0 else init_date.month / 3 + 1
		articles=models.Article.query.filter(models.Article.create_time>restime).count()
		if articles:
			return to_dict_msg(200,data=articles,msg="获取成功")
		else:
			return to_dict_msg(200,msg="当月还没有数据")
	except Exception as e:
		print(e)
		return to_dict_msg(20000)
@article.route("/thumbAndviewedstatus",methods=['GET'])
def thumbstatus():
	try:
		# 收集参数
		uid=int(request.args.get("uid"))
		aid=int(request.args.get("aid"))
		type=request.args.get("type")
		if type=='thumb':
			thumb=models.Thumb.query.filter_by(uid=uid).first()
			# 第一次点赞
			if thumb is None:
				return to_dict_msg(200,data=False,msg="还未浏览过")
			elif thumb.isthumb==False:
				return to_dict_msg(200,data=thumb.isthumb)
			elif thumb.isthumb==True:
				return to_dict_msg(200,data=thumb.isthumb)		
		elif type=='viewed':
			viewed=models.Viewed.query.filter_by(uid=uid).first()
			# 第一次点赞
			if viewed is None:
				return to_dict_msg(200,data=False,msg="还未浏览过")
			elif viewed.isviewed==False:
				return to_dict_msg(200,data=viewed.isviewed)
			elif viewed.isviewed==True:
				return to_dict_msg(200,data=viewed.isviewed)		
	except Exception as e:
		print(e)
		return to_dict_msg(20000)