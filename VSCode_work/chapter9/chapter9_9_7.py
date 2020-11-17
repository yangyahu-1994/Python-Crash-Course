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

class Admin(User):
    """管理员用户的一次简单尝试"""

    def __init__(self, first_name, last_name, location, field):
        """初始化父类属性和管理员用户的特有属性"""
        super().__init__(first_name, last_name, location, field)
        self.privileges = ['can add post', 'can delet post', 'can ban user']

    def show_privileges(self):
        """显示管理员的权限"""
        for privilege in self.privileges:
            print("Every administrator " + privilege + ".")

# 创建实例
admin_0 = Admin('yang', 'yahu', 'haerbin', 'navigation')


# 调用方法
admin_0.show_privileges()