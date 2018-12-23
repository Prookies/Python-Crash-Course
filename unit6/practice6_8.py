wangwang = {
    'type': 'dog',
    'master': 'hua',
}
luoxiaohei = {
    'type': 'cat',
    'master': 'xiaojun',
}
wangcai = {
    'type': 'dog',
    'master': 'wenlei',
}

pets=[wangwang,luoxiaohei,wangcai]

for pet in pets:
    for key, value in pet.items():
        print(key+" : "+value)
