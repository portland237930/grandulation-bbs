from flask_shop.role import role,role_api
from flask_shop import models,db
from flask import request	
from flask_restful import Resource
import re
from flask_shop.utils.message import to_dict_msg

# 角色列表接口
class Role(Resource):
	def get(self):
		# 获取角色列表接口
		"""获取角色列表接口

    @@@
    ### description
    > 获取角色列表接口

    ### args
    |  args | nullable | request type | type |  remarks |
    |-------|----------|--------------|------|----------|
    |  role_list   |  false   |    query      | str  | 获取所有角色  |
    |  roles   |  false   |    form      | str  | 角色  |

    ### request
    ```json
    {
        "role_list": "xxx",
        'roles':'xxx'
    }
    ```

    ### 重置密码成功返回
    ```json
    {"status": 200, "msg": "增加角色成功"}
    ``` 
    ```     
    ### 错误返回
    ```json
    {"status": 20000, "msg": "异常错误"}}
    ```  
    @@@
    """			
		try:
			role_list=[]
			# 获得所有角色
			roles=models.Role.query.all()
			role_list=[r.to_dict() for r in roles]
			return to_dict_msg(200,role_list,'获取角色列表成功')
		except Exception as e:
			print(e)
			return to_dict_msg(20000)
	# 增加角色接口
	def post(self):
		"""增加角色接口

    @@@
    ### description
    > 增加角色接口

    ### args
    |  args | nullable | request type | type |  remarks |
    |-------|----------|--------------|------|----------|
    |  name   |  false   |    form      | str  | 角色名  |
    |  desc   |  false   |    form      | str  | 角色描述  |

    ### request
    ```json
    {
        "name": "xxx",
        'desc':'xxx'
    }
    ```

    ### 重置密码成功返回
    ```json
    {"status": 200, "msg": "增加角色成功"}
    ``` 
    ### 没有此数据返回
    ```json
    {"status": 10000, "msg": "数据不完整"}}
    ```     
    ### 错误返回
    ```json
    {"status": 20000, "msg": "异常错误"}}
    ```  
    @@@
    """
		# 接收参数
		name=request.form.get('name')
		desc=request.form.get('desc')
		mids=request.form.get("mids")
		try:
			if name:
				role=models.Role(name=name,desc=desc)
				if mids:
					for m in mids.split(','):
							if m:
								# 获取权限
								temp_menu=models.Permission.query.get(int(m))
								if temp_menu:
									role.permission.append(temp_menu)
				db.session.add(role)
				db.session.commit()
				return to_dict_msg(200,msg="增加角色成功")
			return to_dict_msg(10000)
		except Exception:
			print(e)
			return to_dict_msg(20000)
	# 删除角色
	def delete(self):
		"""删除角色

    @@@
    ### description
    > 删除角色

    ### args
    |  args | nullable | request type | type |  remarks |
    |-------|----------|--------------|------|----------|
    |  id   |  false   |    args      | str  | id  |
		|  r   |  false   |    query      | str  | id  |

    ### request
    ```json
    {
        "id": "xxx",
				"r": "xxx"
    }
    ```

    ### 重置密码成功返回
    ```json
    {"status": 200, "msg": "增加角色成功"}
    ``` 
    ### 没有此数据返回
    ```json
    {"status": 10000, "msg": "数据不完整"}}
    ```     
    ### 错误返回
    ```json
    {"status": 20000, "msg": "异常错误"}}
    ```  
    @@@
    """		
		try:
			id=int(request.args.get("id"))
			# 获得用户
			r=models.Role.query.get(id)
			if r:
				db.session.delete(r)
				db.session.commit()
				return to_dict_msg(200,msg="删除角色成功")
			return to_dict_msg(10000)
		except Exception as e:
			print(e)
			return to_dict_msg(20000)
	# 修改角色接口
	def put(self):
		"""修改角色接口

    @@@
    ### description
    > 修改角色接口

    ### args
    |  args | nullable | request type | type |  remarks |
    |-------|----------|--------------|------|----------|
		|  id   |  false   |    form      | str  | id  |
    |  name   |  false   |    form      | str  | 角色名  |
    |  desc   |  false   |    form      | str  | 角色描述  |

    ### request
    ```json
    {
				"id": "xxx",
        "name": "xxx",
        'desc':'xxx'
    }
    ```

    ### 重置密码成功返回
    ```json
    {"status": 200, "msg": "增加角色成功"}
    ``` 
    ### 没有此数据返回
    ```json
    {"status": 10021, "msg": "没有此权限可删除"}}
    ```     
    ### 错误返回
    ```json
    {"status": 20000, "msg": "异常错误"}}
    ```  
    @@@
    """		
		try:
			# 获取参数
			id=int(request.form.get("id"))
			name=request.form.get("name").strip() if request.form.get("name") else ''
			desc=request.form.get("desc").strip() if request.form.get("desc") else ''
			if name:
				r=models.Role.query.get(id)
				if r:
					r.name=name
					r.desc=desc
					db.session.commit()
					return to_dict_msg(200,msg="修改角色成功")
				else:
					return to_dict_msg(10021)
			return to_dict_msg(10000)
		except Exception as e:
			print(e)
			return to_dict_msg(20000)				

role_api.add_resource(Role,'/role')

# 删除角色权限
@role.route("/del_menu/<int:rid>/<int:mid>")
def del_menu(rid,mid):
		"""删除角色权限

    @@@
    ### description
    > 删除角色权限

    ### args
    |  args | nullable | request type | type |  remarks |
    |-------|----------|--------------|------|----------|
    |  r   |  false   |    query      | str  | 角色id  |
    |  m   |  false   |    query      | str  | 权限id  |

    ### request
    ```json
    {
        "name": "xxx",
        'desc':'xxx'
    }
    ```

    ### 重置密码成功返回
    ```json
    {"status": 200, "msg": "增加角色成功"}
    ``` 
    ### 没有此数据返回
    ```json
    {"status": 10022, "msg": "没有此数据"}}
    ```     
    ### 错误返回
    ```json
    {"status": 20000, "msg": "异常错误"}}
    ```  
    @@@
    """	
		try:
			# 查询指定的角色和菜单权限
			r=models.Role.query.get(rid)
			m=models.Menu.query.get(mid)
			# 如果查询数据有效
			if all([r,m]):
				# 如果权限存在
				if m in r.menus:
					# 删除指定角色中的指定权限
					r.menus.remove(m)
					# # 如果删除的是一级菜单
					# if m.level==1:
					# 	# 获得一级菜单的子菜单
					# 	for temp_m in m.children:
					# 		# 删除所有子节点
					# 		if temp_m in r.menus:
					# 			r.menus.remove(temp_m)
					db.session.commit()
					return to_dict_msg(200,data=r.get_menu_dict(),msg="删除权限成功")
				else:
					return to_dict_msg(10022)
			return to_dict_msg(10000)
		except Exception as e:
			print(e)
			return to_dict_msg(20000)

# 分配权限接口
@role.route("/set_permission/<int:rid>/",methods=['POST'])
def set_permission(rid):
	print(1)
	try:
		# 获得角色
		role=models.Role.query.get(rid)
		# 获得权限列表
		mids=request.form.get('mids')
		if role:
			# 清空角色权限
			role.permission=[]
			for m in mids.split(','):
				if m:
					# 获取权限
					temp_menu=models.Permission.query.get(int(m))
					if temp_menu:
						role.permission.append(temp_menu)
			db.session.commit()
			return to_dict_msg(200,msg="分配权限成功")
		return to_dict_msg(10020)
	except Exception as e:
		print(e)
		return to_dict_msg(20000)