from admin import Admin, Privileges

privileges = ['can add users', 'can delete post', 'can ban user']
admin_1 = Admin('xu', 'hua', Privileges(privileges), age=23, local='Guangzhou')
admin_1.describe_user()
admin_1.privileges.show_privileges()
