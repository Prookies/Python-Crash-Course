def count_words(filename):
    """计算一个文件大致包含多少个单词"""
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist!"
        print(msg)
    else:
        words = contents.split()
        len_words = len(words)
        print("The file has about " + str(len_words) + " words.")


filename = "alice"
count_words(filename)
filename = "cause"
count_words(filename)
