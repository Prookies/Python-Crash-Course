filename = "cause"

cause = input("Why do you like programming?\n")
while cause != 'q':
    with open(filename, 'a') as file_object:
        file_object.write(cause+'\n')
    cause = input("Why do you like programming?\n")
