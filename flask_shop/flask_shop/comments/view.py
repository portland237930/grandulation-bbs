from flask_shop.comments import comments,comments_api
from flask_shop import models,db
from flask import request	
from flask_restful import Resource
import re
from flask_shop.utils.message import to_dict_msg
from datetime import datetime

# 评论接口
class Comments(Resource):
	# 获取指定评论接口
	def get(self):
		"""获取指定评论接口

    @@@
    ### description
    > 获取指定评论接口

    ### args
    |  args | nullable | request type | type |  remarks |
    |-------|----------|--------------|------|----------|
    |  cid   |  false   |    args      | str  | 评论id |
    |  aid    |  false   |    args       | str  | 文章id |
    |  art   |  false   |    query      | str  | art |
    |  comment    |  false   |    query       | str  | 评论 |
    

    ### request
    ```json
    {
        "cid": "xxx",
        'aid':'xxx'
        "art": "xxx",
        'comment':'xxx'
    }
    ```

    ### 重置密码成功返回
    ```json
    {"status": 200, "msg": "评论成功"}
    ``` 
    ### 没有此数据返回
    ```json
    {"status": 10030, "msg": "指定评论或文章不存在"}}
    ```     
    ### 错误返回
    ```json
    {"status": 20000, "msg": "异常错误"}}
    ```  
    @@@
    """				
		try:
			# 收集参数
			cid=int(request.args.get("cid").strip()) if request.args.get("cid") else 0
			aid=int(request.args.get("aid").strip()) if request.args.get("aid") else 0
			art=models.Article.query.get(aid)
			comment=models.Comment.query.get(cid)
			# 查询成功
			if art and comment:
				usr=models.User.query.get(art.pid)
				if usr:
					return to_dict_msg(200,data={'comments':comment.to_dict(),'user':usr.to_dict()},msg="获取评论成功")
			else:
				return to_dict_msg(10030)
		except Exception as e:
			print(e)
			return to_dict_msg(20000)
	# 创建评论接口
	def post(self):
		"""创建评论接口

    @@@
    ### description
    > 创建评论接口

    ### args
    |  args | nullable | request type | type |  remarks |
    |-------|----------|--------------|------|----------|
    |  aid   |  false   |    args      | str  | 文章id |
    |  content    |  true   |    form       | str  | 内容 |
    |  create_time   |   false   |     form       | str  | 创建时间  |
    |  art   |  false   |     form       | str  | art |
    |  uid    |  false   |     form       | str  | 文章 |
    

    ### request
    ```json
    {
        "aid": "xxx",
        'content':'xxx'
				"create_time": "xxx",
        'art':'xxx'
				"uid": "xxx"
    }
    ```

    ### 重置密码成功返回
    ```json
    {"status": 200, "msg": "评论成功"}
    ``` 
    ### 没有此数据返回
    ```json
    {"status": 10029, "msg": "评论失败"}}
    ```     
    ### 错误返回
    ```json
    {"status": 20000, "msg": "异常错误"}}
    ```  
    @@@
    """		
		try:
			# 收集参数
			aid=int(request.args.get('aid').strip()) if request.args.get('aid') else 0
			content=request.form.get("content").strip() if request.form.get("content") else ''
			create_time=request.form.get("create_time").strip() if request.form.get("create_time") else datetime.now()
			art=models.Article.query.filter_by(id=aid).first()
			uid=art.pid if art.pid else 0
			# 如果参数收集成功
			if art:
				# 创建评论
				comment=models.Comment(content=content,aid=aid,uid=uid,create_time=create_time,update_time=create_time)
				db.session.add(comment)
				db.session.commit()
				return to_dict_msg(200,msg="评论成功")
			else:
				return to_dict_msg(10029)
		except Exception as e:
			print(e)
			return to_dict_msg(20000)
	def put(self):
		"""收集参数

    @@@
    ### description
    > 收集参数

    ### args
    |  args | nullable | request type | type |  remarks |
    |-------|----------|--------------|------|----------|
    |  cid   |  false   |    form      | str  | 评论id |
    |  create_time   |   false   |     form       | str  | 创建时间  |
		|  content    |  true   |    form       | str  | 内容 |
    |  comment   |  false   |     query       | str  | 评论 |
    

    ### request
    ```json
    {
        "cid": "xxx",
				"create_time": "xxx",
        'content':'xxx',				
        'comment':'xxx'
    }
    ```

    ### 重置密码成功返回
    ```json
    {"status": 200, "msg": "评论成功"}
    ``` 
    ### 没有此数据返回
    ```json
    {"status": 10029, "msg": "评论失败"}}
    ```     
    ### 错误返回
    ```json
    {"status": 20000, "msg": "异常错误"}}
    ```  
    @@@
    """				
		try:			
			cid=int(request.form.get("id"))
			create_time=request.form.get("create_time").strip() if request.form.get("create_time") else datetime.now()
			content=request.form.get("content") if request.form.get("content") else ''
			comment=models.Comment.query.get(cid)
			if comment:
				# create_time=datetime.strptime(create_time,"%m/%d/%y %H:%M:%S")
				comment.create_time=create_time
				comment.update_time=create_time
				comment.content=content
				db.session.commit()
				return to_dict_msg(200,msg='修改成功')
			else:
				return to_dict_msg(10033)
		except Exception as e:
			print(e)
			return to_dict_msg(20000)
	def delete(self):
		"""获取指定用户指定文章的所有评论

    @@@
    ### description
    > 获取指定用户指定文章的所有评论

    ### args
    |  args | nullable | request type | type |  remarks |
    |-------|----------|--------------|------|----------|
    |  id   |  false   |    args      | str  | 评论id |
    |  comment   |  false   |     query       | str  | 评论 |
    

    ### request
    ```json
    {
        "id": "xxx",				
        'comment':'xxx'
    }
    ```

    ### 重置密码成功返回
    ```json
    {"status": 200, "msg": "评论成功"}
    ``` 
    ### 没有此数据返回
    ```json
    {"status": 10030, "msg": "指定评论或文章不存在"}}
    ```     
    ### 错误返回
    ```json
    {"status": 20000, "msg": "异常错误"}}
    ```  
    @@@
    """					
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

# 获取指定用户指定文章的所有评论
@comments.route('/GetAllComments',methods=["GET"])
def getcomments():	
	try:

		# # 如果获取指定用户的指定文章的所有评论
		# if type=='all':
		# 	uid=int(request.args.get("uid").strip()) if request.args.get("uid") else 0
		# 	aid=int(request.args.get("aid").strip()) if request.args.get("aid") else 0
		# 	art=models.Article.query.get(aid)
		# 	usr=models.User.query.get(uid)
		# 	comments=models.Comment.query.filter_by(aid=aid,uid=uid).all()
		# 	clist=[c.to_dict() for c in comments]
		# 	return to_dict_msg(200,data=clist,msg="获取用户{0}的文章{1}所有评论成功".format(usr.name,art.title))
		# 如果指定用户的所有评论
		uid=int(request.args.get("uid").strip()) if request.args.get("uid") else 0
		usr=models.User.query.get(uid)
		if usr:
			comments=models.Comment.query.filter_by(uid=uid).all()
			clist=[]
			for c in comments:
				art=models.Article.query.get(c.aid)
				clist.append(
					{
						'comment':c.to_dict(),
						'publisher':art.title
					}
				)
			# 如果用户存在				
			return to_dict_msg(200,data=clist,msg="获取用户{0}所有评论成功".format(usr.name))
			# # 如果指定文章的所有评论
			# elif type=='article':
			# 	aid=int(request.args.get("aid").strip()) if request.args.get("aid") else 0
			# 	art=models.Article.query.get(aid)
			# 	comments=models.Comment.query.filter_by(aid=aid)
			# 	clist=[c.to_dict() for c in comments]
			# 	return to_dict_msg(200,data=clist,msg="获取文章{0}所有评论成功".format(art.title))
		else:
			return to_dict_msg(10026)
	except Exception as e:
		print(e)
		return to_dict_msg(20000)
# 点赞数和评论数增加接口
@comments.route("/addcom",methods=["POST"])
def addthumb():
		"""点赞数和评论数增加接口

    @@@
    ### description
    > 点赞数和评论数增加接口

    ### args
    |  args | nullable | request type | type |  remarks |
    |-------|----------|--------------|------|----------|
    |  cid   |  false   |    args      | str  | 评论id |		
    |  aid   |  false   |    args      | str  | 文章id |
    |  comment   |   false   |     query       | str  | 评论  |
    |  art   |  false   |     query       | str  | art |
    |  type    |  true   |     args       | str  | 文章 |
    

    ### request
    ```json
    {
        "cid": "xxx",
        'aid':'xxx'
				"comment": "xxx",
        'art':'xxx'
				"type": "xxx"
    }
    ```

    ### 重置密码成功返回
    ```json
    {"status": 200, "msg": "评论成功"}
    ``` 
    ### 没有此数据返回
    ```json
    {"status": 10028, "msg": "请指定点赞或浏览"}}
    ```     
    ### 错误返回
    ```json
    {"status": 20000, "msg": "异常错误"}}
    ```  
    @@@
    """			
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
@comments.route("/getArticleToComment",methods=['GET'])
def getArticleToComment():	
	try:		
		id=request.args.get("id")
		comments=models.Comment.query.filter_by(aid=id).all()
		if comments:
			clist=[c.to_dict() for c in comments]
			return to_dict_msg(200,data=clist,msg="获取评论成功")
		else:
			return to_dict_msg(10028)
	except Exception as e:
		print(e)
		return to_dict_msg(20000)

@comments.route("/publishComment",methods=['POST'])
def publishComment():			
	try:	
		id=int(request.form.get('id')) if request.form.get('id') else 0
		content=request.form.get('content')
		art=models.Article.query.get(id)
		if art:
			uid=art.pid if art.pid else 0
			comment=models.Comment(content=content,aid=id,uid=uid)
			db.session.add(comment)
			db.session.commit()
			return to_dict_msg(200,msg="评论成功")
		else:
			return to_dict_msg(10026)
	except Exception as e:
		print(e)
		return to_dict_msg(20000)
comments_api.add_resource(Comments,'/comments')