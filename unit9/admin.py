from user import User
class Privileges:
    """描述特权"""

    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print("He has these privileges: ")
        for privilege in self.privileges:
            print(privilege)


class Admin(User):
    """描述一个管理员用户"""

    def __init__(self, first_name, last_name, privileges, **user_info):
        super().__init__(first_name, last_name, **user_info)
        self.privileges = privileges