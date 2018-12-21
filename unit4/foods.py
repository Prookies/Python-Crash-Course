my_foods=['pizza','falafel','carrot cake']
friend_foods=my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

print("\nThe first three items in the list are:")
print(my_foods[0:3])

print("\nTwo items from the middle of the list are:")
print(my_foods[1:3])

print("\nThe last three items in the list are:")
print(my_foods[-3:])

my_pizzas=['one','two','three','four']
friend_pizzas=my_pizzas[:]
friend_pizzas.append('five')
print("\nMy favorite pizzas are:")
print(my_pizzas)
print("\nMy friend's favorite pizzas are:")
print(friend_pizzas)

print("\n")
for food in my_foods:
    print(food)

print("\n")
for food in friend_foods:
    print(food)