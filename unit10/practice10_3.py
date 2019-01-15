filename = "guest"
name = input("Please input your name")
with open(filename, 'w') as file_object:
    file_object.write(name)

with open(filename) as file_object:
    print(file_object.read())
