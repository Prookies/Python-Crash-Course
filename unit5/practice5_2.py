str1 = 'I love you'
print("两个字符串是否相等")
print(str1 == 'I love you')
print("转换为小写")
print(str1.title() == 'I love you'.title())

num1=18
print("两个数字是否相等")
print(num1 == 18)
print("两个数字是否不等")
print(num1 != 18)
print("是否大于")
print(num1 > 19)
print("是否小于")
print(num1 < 20)
print("是否大于等于")
print(num1 >= 18)
print("是否小于等于")
print(num1 <= 22)

print("数字是否大于9小于20")
print((num1 > 9) and (num1 < 20))

num2 = 22
print("数字1大于20或者数字2小于20")
print(num1 > 20 or num2 < 20)

numbers = [18, 20, 22, 24]
print("数字1是否在数字列表中")
print(num1 in numbers)
print("数字2是否不在数字列表中")
print(num2 not in numbers)

