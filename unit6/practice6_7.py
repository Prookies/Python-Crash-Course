acquaintance_0={
    'first_name':'lai',
    'last_name':'shuming',
    'age':24,
    'city':'dongguan',
}
acquaintance_1={
    'first_name':'xu',
    'last_name':'hua',
    'age':22,
    'city':'zhuhai'
}
acquaintance_2={
    'first_name':'peng',
    'last_name':'wen',
    'age':22,
    'city':'zhongshan'
}

acquaintances=[acquaintance_0,acquaintance_1,acquaintance_2]

for acquaintance in acquaintances:
    print("Full name: "+acquaintance['first_name']+acquaintance['last_name'])
    print("age: "+str(acquaintance['age']))
    print("city: "+acquaintance['city'])

