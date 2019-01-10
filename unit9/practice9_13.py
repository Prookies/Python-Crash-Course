from collections import OrderedDict

favorite_words = OrderedDict()
favorite_words['key'] = "关键词"
favorite_words['list'] = "列表"
favorite_words['dictionary'] = "字典"
favorite_words['class'] = "类"
favorite_words['function'] = "函数"
for word, mean in favorite_words.items():
    print(word + "'s mean is: " + mean)
