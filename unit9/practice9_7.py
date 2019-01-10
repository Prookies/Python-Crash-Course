class User:
    def __init__(self, first_name, last_name, **user_info):
        self.first_name = first_name
        self.last_name = last_name
        self.user_info = user_info
        self.login_attempts = 0

    def describe_user(self):
        print("The name of user is " + self.first_name.title() + " "
              + self.last_name.title() + ".")
        if self.user_info:
            print("The information about user as follow:")
            for key, value in self.user_info.items():
                print(key + ": " + str(value))
        print("His login attempt number is " + str(self.login_attempts))

    def greet_user(self):
        print("Hello " + self.first_name + " " + self.last_name)

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


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


privileges = ['can add post', 'can delete post', 'can ban user']
admin_1 = Admin('xu', 'hua', Privileges(privileges), age=23, local='Guangzhou')
admin_1.privileges.show_privileges()
