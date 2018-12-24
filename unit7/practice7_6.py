msg = "Please input a kind of ingredient you like: "
ingredients = []
active = True
while active:
    ingredient = input(msg)
    if ingredient != 'quit':
        ingredients.append(ingredient)
        print("We will add " + ingredient + "in your pizza")
    else:
        active = False
        break
print("This is your ingredients: ")
for ingredient in ingredients:
    print(ingredient)