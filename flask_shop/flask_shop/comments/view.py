from flask_shop.comments import comments,comments_api
from flask_shop import models,db
from flask import request	
from flask_restful import Resource
import re
from flask_shop.utils.message import to_dict_msg

# 评论接口
class Comments(Resource):
	# 获取指定评论接口
	def get(self):
		try:
			# 收集参数
			cid=int(request.args.get("cid").strip()) if request.args.get("cid") else 0
			aid=int(request.args.get("aid").strip()) if request.args.get("aid") else 0
			art=models.Article.query.get(aid)
			comment=models.Comment.query.get(cid)
			# 查询成功
			if art and comment:
				return to_dict_msg(200,data=comment.to_dict(),msg="获取评论成功")
			else:
				return to_dict_msg(10030)
		except Exception as e:
			print(e)
			return to_dict_msg(20000)
	# 创建评论接口
	def post(self):
		try:
			# 收集参数
			aid=int(request.args.get('aid').strip()) if request.args.get('aid') else 0
			content=request.form.get("content").strip() if request.form.get("content") else ''
			art=models.Article.query.filter_by(id=aid)
			# 如果参数收集成功
			if art and content:
				comment=models.Comment(content=content,aid=aid)
				db.session.add(comment)
				db.session.commit()
				return to_dict_msg(200,msg="评论成功")
			else:
				return to_dict_msg(10029)
		except Exception as e:
			print(e)
			return to_dict_msg(20000)
	def delete(self):
		try:
			id=int(request.args.get("id").strip()) if request.args.get("id") else 0
			comment=models.Comment.query.get(id)
			if comment:
				db.session.delete(comment)
				db.session.commit()
				return to_dict_msg(200,msg="删除评论成功")
			else:
				return to_dict_msg(10030)
		except Exception as e:
			print(e)
			return to_dict_msg(20000)

# 获取所有接口
@comments.route('/GetAllComments',methods=["GET"])
def getcomments():
	try:
		id=int(request.args.get("id").strip()) if request.args.get("id") else 0
		art=models.Article.query.get(id)
		if art:
			comments=models.Comment.query.filter_by(aid=id).all()
			clist=[c.to_dict() for c in comments]
			return to_dict_msg(200,data=clist,msg="获取所有评论成功")
		else:
			return to_dict_msg(10026)
	except Exception as e:
		print(e)
		return to_dict_msg(20000)
# 点赞数和评论数增加接口
@comments.route("/addcom",methods=["POST"])
def addthumb():
		try:
			# 获取用户id和文章id
			cid=int(request.args.get('cid').strip()) if request.args.get('cid') else 0
			aid=int(request.args.get('aid').strip()) if request.args.get('aid') else 0
			comment=models.Comment.query.get(cid)
			art=models.Article.query.get(aid)
			type=request.args.get('type').strip() if request.args.get('type') else ''
			if comment and art:
				if type=='add':
					comment.thumb+=1
				elif type=='reduce':
					comment.thumb-=1 if comment.thumb else 0
				else:
					return to_dict_msg(10028)
				db.session.commit()
				return to_dict_msg(200,msg='成功')
		except Exception as e:
			print(e)
			return to_dict_msg(20000)
comments_api.add_resource(Comments,'/comments')