from user_0 import User

class Privileges():
    """特权的简单尝试"""

    def __init__(self, privileges=['can add post', 'can delet post', 'can ban user']):
        """初始化特权属性"""
        self.privileges = privileges

    def show_privileges(self):
        """显示管理员的权限"""
        for privilege in self.privileges:
            print(f"Every administrator {privilege}.")


class Admin(User):
    """管理员用户的一次简单尝试"""

    def __init__(self, first_name, last_name, location, field):
        """初始化父类属性和管理员用户的特有属性"""
        super().__init__(first_name, last_name, location, field)
        self.three_privileges = Privileges()