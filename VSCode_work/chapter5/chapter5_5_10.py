# 创建用户名列表
current_users = ['Admin', 'yang yahu', 'gao xiangzhou', 'eric', 'yang yuhang']
# 创建另一个用户名列表
new_users = ['admin', 'Yang yahu', 'li jianfeng', 'yuan lishan', 'wang hao']

# 遍历列表
for new_user in new_users:
    if new_user.lower() and new_user.upper() and new_user.title() in [current_user.lower() and 
    current_user.upper() and current_user.title() for current_user in current_users]:     # 列表解析
        print(f"{new_user} has been used, you need to input another user name!")
    else:
        print(f"{new_user} has not been used, you kan use it!")

