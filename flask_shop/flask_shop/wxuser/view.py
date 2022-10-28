from flask_shop.wxuser import wxuser,wxuser_api
from flask_shop import models,db
from flask import request,current_app
from flask_restful import Resource,reqparse
import re
from flask_shop.utils.md5 import md5_file
from flask_shop.utils.message import to_dict_msg

class WxUser(Resource):
	def get(self):
		try:
			wxid=request.args.get('wxid')
			wxuser=models.WxUser.query.filter_by(wxid=wxid).first()
			if wxuser:
				usr=models.User.query.get(wxuser.user_id)
				return to_dict_msg(200,data=usr.to_dict(),msg="获取成功")
			else:
				return to_dict_msg(10035)
		except Exception as e:
			print(e)
			return to_dict_msg(20000)
	def post(self):
		try:
			user_id=request.form.get('user_id')
			nick_name=request.form.get('nick_name')
			avatar_url=request.form.get('avatar_url')
			wxid=request.form.get('wxid')
			usr=models.User.query.get(user_id)
			if usr:				
				wxuser=models.WxUser(nick_name=nick_name,avatar_url=avatar_url,user_id=user_id,wxid=wxid)
				db.session.add(wxuser)
				db.session.commit()
				return to_dict_msg(200,msg="绑定成功")
			else:
				return to_dict_msg(10011)
		except Exception as e:
			print(e)
			return to_dict_msg(20000)
	def delete(self):
		try:
			wxid=request.form.get("wxid")
			uid=int(request.form.get("uid"))
			wxuser=models.WxUser.query.filter_by(wxid=wxid,user_id=uid).first()
			if wxuser:
				db.session.delete(wxuser)
				db.session.commit()
				return to_dict_msg(200,msg="解绑成功")
			else:
				return to_dict_msg(10035)
		except Exception as e:
			print(e)
			return to_dict_msg(20000)
wxuser_api.add_resource(WxUser,"/wxuser")
