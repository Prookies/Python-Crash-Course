def print_names(filename):
    try:
        with open(filename) as file_object:
            content = file_object.read()
    except FileNotFoundError:
        # msg = "I can't find " + filename
        # print(msg)
        pass
    else:
        print(content.strip())


file_cat = "cat"
file_dog = "dog"
print_names(file_cat)
print_names(file_dog)