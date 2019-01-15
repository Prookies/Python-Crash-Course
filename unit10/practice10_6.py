while True:
    first_number = input("Please input the first number: ")
    if first_number == 'q':
        break
    second_number = input("Please input the second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        msg = "You can't input charter!"
        print(msg)
    else:
        print(str(first_number)+" + "+str(second_number)+" = "+str(answer))
