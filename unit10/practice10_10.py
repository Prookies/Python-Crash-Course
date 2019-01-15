filename='green'
with open(filename) as file_object:
    contents=file_object.read()

numbers_the=contents.lower().count('the')
print("The text has about "+str(numbers_the)+" the.")
