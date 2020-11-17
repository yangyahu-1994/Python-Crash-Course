# 定义函数user_profile.py
def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

# 调用函数
user_profile = build_profile('yahu', 'yang',
                            location = 'Harbin Institute of Technology, Harbin, Heilongjiang Province',
                            field = 'navigation',
                            grade = 'PhD first year')
print(user_profile)