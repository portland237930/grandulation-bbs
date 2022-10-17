from flask_shop.permission import permission,permission_api
from flask_shop import models,db
from flask import request	
from flask_restful import Resource
import re
from flask_shop.utils.message import to_dict_msg

class Permission(Resource):
	def get(self):
		pass
	# 创建权限
	def post(self):
		name=request.form.get("name")
		try:
			if name:
				permission=models.Permission(name=name)
				db.session.add(permission)
				db.session.commit()
				return to_dict_msg(200,msg="增加权限成功")
			return to_dict_msg(10000)
		except Exception:
			print(e)
			return to_dict_msg(20000)		
		pass

permission_api.add_resource(Permission,'/permission')