# 创建类
class User():
    """11"""
    
    def __init__(self, first_name, last_name, location, field):
        """初始化一个用户的属性"""
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.field = field
        self.login_attempts = 0

    def describe_user(self):
        """打印用户信息摘要"""
        print("First name: " + self.first_name.title() + "!")
        print("Last name: " + self.last_name.title() + "!")
        print("Location: " + self.location.title() + "!")
        print("Field: " + self.field.title() + "!")
        print("Number of logins: " + str(self.login_attempts) + "!" )

    def greet_user(self):
        """向用户发出个性化的问候"""
        print(self.first_name + self.last_name + ",how are you? have you eaten? are you healthy now?")

    def increment_login_attempts(self):
        """将属性login_attempts的值加1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """将属性login_attempts的值重置为0"""
        self.login_attempts = 0

# 创建实例
user = User('yang', 'yahu', 'haerbin', 'navigation')


# 调用方法
user.increment_login_attempts()
user.describe_user()


user.increment_login_attempts()
user.describe_user()

user.increment_login_attempts()
user.describe_user()

user.reset_login_attempts()
user.describe_user()