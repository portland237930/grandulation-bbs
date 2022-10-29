from flask_shop.permission import permission,permission_api
from flask_shop import models,db
from flask import request	
from flask_restful import Resource
import re
from flask_shop.utils.message import to_dict_msg

class Permission(Resource):
	def get(self):
		"""点赞数和评论数增加接口

    @@@
    ### description
    > 点赞数和评论数增加接口

    

    ### 重置密码成功返回
    ```json
    {"status": 200, "msg": "点赞成功"}
    ```     
    ### 错误返回
    ```json
    {"status": 20000, "msg": "异常错误"}}
    ```  
    @@@
    """			
		try:
			rlist=[r.to_dict() for r in models.Permission.query.all()]
			if rlist:
				return to_dict_msg(200,data=rlist,msg="获取权限成功")
		except Exception as e:
			print(e)
			return to_dict_msg(20000)
	# 创建权限
	def post(self):
		"""点赞数和评论数增加接口

    @@@
    ### description
    > 点赞数和评论数增加接口
    ### args
    |  args | nullable | request type | type |  remarks |
    |-------|----------|--------------|------|----------|
    |  name    |  true   |    form       | str  | 姓名 |
    

    ### request
    ```json
    {
				"name": "xxx"
    }
    ```
    

  
   	### 重置密码成功返回
    ```json
    {"status": 200, "msg": "点赞成功"}
    ```
		### 重置密码成功返回
    ```json
    {"status": 10000, "msg": "数据不完整"}
    ```    
    ### 错误返回
    ```json
    {"status": 20000, "msg": "异常错误"}}
    ```  
    @@@
    """		
		name=request.form.get("name")
		try:
			if name:
				permission=models.Permission(name=name)
				db.session.add(permission)
				db.session.commit()
				return to_dict_msg(200,data=permission.to_dict(),msg="增加权限成功")
			return to_dict_msg(10000)
		except Exception:
			print(e)
			return to_dict_msg(20000)		
	def put(self):
		"""点赞数和评论数增加接口

    @@@
    ### description
    > 点赞数和评论数增加接口

    ### args
    |  args | nullable | request type | type |  remarks |
    |-------|----------|--------------|------|----------|
    |  id   |  false   |    form      | str  | id |
    |  name    |  true   |    form       | str  | 姓名 |
		|  permission   |  false   |    form      | str  | 权限  |
    

    ### request
    ```json
    {
        "id": "xxx",
				"name": "xxx",
				"permission": "xxx"
    }
    ```

    ### 重置密码成功返回
    ```json
    {"status": 200, "msg": "点赞成功"}
    ``` 
   	### 重置密码成功返回
    ```json
    {"status": 10031, "msg": "评论不存在"}
    ```     
    ### 错误返回
    ```json
    {"status": 20000, "msg": "异常错误"}}
    ```  
    @@@
    """		
		try:
			id=request.form.get("id") if request.form.get("id") else 0
			name=request.form.get('name') if request.form.get('name') else ''
			permission=models.Permission.query.get(id)
			if permission:
				permission.name=name
				db.session.commit()
				return to_dict_msg(200,msg="修改成功")
			else:
				return to_dict_msg(10031)
		except Exception as e:
			print(e)
			return to_dict_msg(20000)
	def delete(self):
		"""点赞数和评论数增加接口

    @@@
    ### description
    > 点赞数和评论数增加接口

    ### args
    |  args | nullable | request type | type |  remarks |
    |-------|----------|--------------|------|----------|
    |  id   |  false   |    args      | str  | id |
    |  permission    |  false   |    query       | str  | 权限 |
    

    ### request
    ```json
    {
        "id": "xxx",
				"permission": "xxx"
    }
    ```

    ### 重置密码成功返回
    ```json
    {"status": 200, "msg": "点赞成功"}
    ``` 
   	### 重置密码成功返回
    ```json
    {"status": 10032, "msg": "指定角色不存在"}
    ```   
    ### 错误返回
    ```json
    {"status": 20000, "msg": "异常错误"}}
    ```  
    @@@
    """		
		try:
			id=request.args.get("id") if request.args.get("id") else 0
			permission=models.Permission.query.get(id)
			if permission:
				db.session.delete(permission)
				db.session.commit()
				return to_dict_msg(200,msg="删除成功")
			else:
				return to_dict_msg(10032)
		except Exception as e:
			print(e)
			return to_dict_msg(20000)
		
@permission.route('/GetPermissionlist',methods=['GET'])
def GetPermissionlist():		
	"""点赞数和评论数增加接口

    @@@
    ### description
    > 点赞数和评论数增加接口

    ### args
    |  args | nullable | request type | type |  remarks |
    |-------|----------|--------------|------|----------|
    |  rid   |  false   |    args      | str  | 权限id |
    |  role    |  false   |    query       | str  | 角色 |
    

    ### request
    ```json
    {
        "rid": "xxx",
				"role": "xxx"
    }
    ```

    ### 重置密码成功返回
    ```json
    {"status": 200, "msg": "点赞成功"}
    ``` 
   	### 重置密码成功返回
    ```json
    {"status": 10032, "msg": "指定角色不存在"}
    ```   
    ### 错误返回
    ```json
    {"status": 20000, "msg": "异常错误"}}
    ```  
    @@@
    """
	try:
		rid=int(request.args.get('rid').strip()) if request.args.get('rid') else 0
		role=models.Role.query.get(rid)
		if role:
			plist=[p.to_dict() for p in role.permission]
			return to_dict_msg(200,data=plist,msg="获取成功")
		else:
			return to_dict_msg(10032)
	except Exception as e:
		print(e)
		return to_dict_msg(20000)


permission_api.add_resource(Permission,'/permission')
