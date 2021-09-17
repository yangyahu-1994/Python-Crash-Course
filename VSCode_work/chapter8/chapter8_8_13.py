# 定义函数user_profile.py
def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

# 调用函数
user_profile = build_profile('yahu', 'yang',
                            location = 'Harbin Institute of Technology, Harbin, Heilongjiang Province',
                            field = 'navigation',
                            grade = 'PhD first year')
print(user_profile)