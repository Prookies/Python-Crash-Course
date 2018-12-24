sandwich_orders=['ham','bacon','cheese']
finished_sandwiches=[]
active=True
while sandwich_orders:
    current_sandwiche=sandwich_orders.pop()
    print("I made your "+current_sandwiche+" sandwich")
    finished_sandwiches.append(current_sandwiche)

print("I have finished all sandwiches listed:")
for sandwich in finished_sandwiches:
    print(sandwich)
