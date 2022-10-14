status_msg={
    200:'成功',
    10000:'数据不完整',
    10011:'用户名不合法',
    10012:'密码不合法',
    10013:'二次密码不一致',
    10014:'手机号不合法',
    10015:'邮箱不合法',
    10016:'请登录后使用',
    10017:'token不可使用',
    10018:'修改用户错误',
    10019:'删除错误',
    10020:'修改的角色不存在',
    10021:'没有此权限可删除',
    10022:'没有此数据',
    10023:'没有上传文件',
    10024:'文件格式不符合规范',
    20000:'异常错误'
}

def to_dict_msg(status=200,data=None,msg=None):
    return {
        'status':status,
        'data':data,
        'msg':msg if msg else status_msg.get(status)
    }

if __name__ == "__main__":
    print(to_dict_msg(10000))