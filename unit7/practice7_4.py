burdenings = []
msg = "Please input a kind of bordening: "
burdening = ""
active = True
while active:
    burdening = input(msg)
    if burdening != 'quit':
        print("We will add the "+burdening)
        burdenings.append(burdening)
    else:
        break
print("This is your burdenings: ")
for burdening in burdenings:
    print(burdening)
