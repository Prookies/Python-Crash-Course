import json


def get_stored_number(filename):
    """读取你喜欢的数"""
    try:
        with open(filename) as f_obj:
            favorite_number = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return favorite_number


def get_new_number(filename):
    """请输入一个你喜欢的数字"""
    favorite_number = input("Please input a your favorite number: ")
    with open(filename, 'w') as f_obj:
        json.dump(favorite_number, f_obj)
    return favorite_number


def favorite_number(filename):
    """获取用户最喜欢的数字"""
    favorite_number = get_stored_number(filename)
    if favorite_number:
        print("Your favorite number is: " + favorite_number)
    else:
        get_new_number(filename)
        print("We'll remember your favorite number when you come back.")


favorite_number('favorite_number.json')