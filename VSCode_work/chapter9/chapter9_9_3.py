# 创建类
class User():
    """11"""
    def __init__(self, first_name, last_name, location, field):
        """初始化一个用户的属性"""
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.field = field

    def describe_user(self):
        """打印用户信息摘要"""
        print("First name: " + self.first_name.title() + "!")
        print("Last name: " + self.last_name.title() + "!")
        print("Location: " + self.location.title() + "!")
        print("Field: " + self.field.title() + "!")

    def greet_user(self):
        """向用户发出个性化的问候"""
        print(self.first_name + self.last_name + ",how are you? have you eaten? are you healthy now?")

# 创建实例
user_0 = User('yang', 'yahu', 'haerbin', 'navigation')
user_1 = User('gao', 'xiangzhou', 'beijing', 'navigation')

# 调用方法
user_0.describe_user()
user_0.greet_user()
user_1.describe_user()
user_1.greet_user()