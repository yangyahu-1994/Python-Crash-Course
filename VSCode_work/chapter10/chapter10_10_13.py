# 导入必要的模块
import json

# 定义获取已存储用户的函数
def get_stored_username():
    """如果存储了用户名，就获取它"""
    filename = 'username.json'
    try:
        with open(filename) as file_object:
            username = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return username
    
# 定义获取新用户用户名的函数
def get_new_username():
    """提示用户输入名户名"""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as file_object:
        json.dump(username, file_object)
    return username

# 向新用户和老用户问候
def greet_user():
    """询问用户用户名是不是正确，正确则欢迎，错误则重新输入用户名"""
    username = get_stored_username()
    if username:
        ask = input(username + " is your name?(y/n)")
        if ask == 'y':
            print("Welcome back, " + username + "!")
        else:
            username = get_new_username()
            print("We'll remember you when you come back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")
        
# 调用问候函数
greet_user()