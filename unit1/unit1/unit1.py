#hello_world.py
"""
message="Hello Python world!"
print(message)

message="Hello Python Crash Course world!"
print(message)
"""

#simple_message.py
"""
message="How are you?"
print(message)
message="I am fine"
print(message)
"""

#name.py
"""
name="ada lovelace"
print(name.title())
first_name="ada"
last_name="lovelace"
full_name=first_name+" "+last_name
print(full_name)

print("Hello, "+full_name.title()+"!")

message="Hello, "+full_name.title()+"!"
print(message)
"""

#apostrophe.py
"""
message="One of Python's strengths is its diverse community."
print(message)
"""

#name_cases.py
"""
name="Eric"
print("Hello "+name+", would you like to learn some Python today?")
print(name.lower())
print(name.upper())
print(name.title())
celebrity_name="Albert Einstein"
print(celebrity_name+' once said, "A person who never made a mistake never tried anything new."')
name=" Eric "
print('\t'+name)
print('\t'+name.rstrip())
print('\t'+name.lstrip())
print('\t'+name.strip())
"""

#birthday.py
"""
age=23
message="Happy "+str(age)+"rd Birthday!"
print(message)
"""

#number_cases.py
print(4+4)#打印4+4的结果
print(4*2)#打印4*2的结果
print(9-1)#打印9-1的结果
print(int(16/2))#打印16/2的结果
favorite_number=2#定义最喜欢数字的变量
favorite_number_msg="my favorite number is"+str(favorite_number)#将数字与字符串结合并赋值给新的变量，使用str方法把数字转换为字符串
print(favorite_number_msg)#打印消息