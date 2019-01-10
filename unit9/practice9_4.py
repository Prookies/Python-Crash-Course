from practice9_2 import User

user_1 = User('li', 'ming', age=25, local='Guangzhou')
user_1.describe_user()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.describe_user()
