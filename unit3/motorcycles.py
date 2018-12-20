motorcycles=['honda','yamaha','suzuki']
print(motorcycles)

motorcycles[0]='ducati'
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles=[]

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

motorcycles.insert(0,'ducati')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

del motorcycles[1]
print(motorcycles)

motorcycles.insert(0,'honda')
print(motorcycles)
popped_motorcycle=motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles=['honda','yamaha','suzuki']
last_owned=motorcycles.pop()
print("The last motorcycle I owned was a "+last_owned.title()+".")

motorcycles.insert(2,'suzuki')
first_owned=motorcycles.pop(0)
print('The first motorcycle I owned was a '+first_owned.title()+'.')

motorcycles=['honda','yamada','suzuki','ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

motorcycles.insert(3,'ducati')
print(motorcycles)
too_expensice='ducati'
motorcycles.remove(too_expensice)
print(motorcycles)
print("\nA "+too_expensice.title()+" is too expensive for me.")
