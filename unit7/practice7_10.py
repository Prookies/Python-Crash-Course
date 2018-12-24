dream_resorts={}
msg="If you could visit one place in the world, where would you go?" \
    " (yes/no) "
active=True
while active:
    result=input(msg)
    if result == 'yes':
        name=input("Please your name: ")
        place=input("Please your drem resort: ")
        dream_resorts[name]=place
    else:
        active=False

print("\n --- Poll Results ---")
for name, place in dream_resorts.items():
    print(name+", his/her dream resort is "+place)
