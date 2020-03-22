def ask_for_int():
    result = 0
    while True:
        try:
            result = int(input("please enter a number = "))
            square = result * result
            print("squared value = ", square)
        except:
            print("whoops,This is not a number")
            continue
        else:
            print("thank you")
            break

ask_for_int()