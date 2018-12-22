users = ['xuhua', 'xiaojun', 'root', 'admin', 'guest']

for user in users:
    if user == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello " + user + ", thank you for logging in again.")

print("\n")
users = []
if users:
    for user in users:
        if user == admin:
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello " + user + ", thank you for logging in again.")
else:
    print("\nWe need to find some users!")

print('\n')
current_users = ['hua', 'jun', 'peng', 'chen', 'admin']
current_users_lower = [item.lower() for item in current_users]
new_users = ['Hua', 'jun', 'jiang', 'lin', 'zheng']

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print("Please input the next user name.")
    else:
        print("The user name isn't used.")
