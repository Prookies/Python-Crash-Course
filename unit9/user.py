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
