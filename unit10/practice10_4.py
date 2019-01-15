filename = 'guest_book'
with open(filename, 'w') as file_object:
    file_object.write('')

# name = ''
# while name != 'q':
#     name = input("Please input your name: ")
#     if name != 'q':
#         print("Hello " + name)
#         with open(filename, 'a') as file_object:
#             file_object.write(name + '\n')


name = input("Please input your name: ")
while name != 'q':
    print("Hello " + name)
    with open(filename, 'a') as file_object:
        file_object.write(name + "\n")
    name = input("Please input your name: ")
