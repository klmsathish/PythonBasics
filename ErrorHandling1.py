def ask_for_int():
    while True:
        try:
            result = int(input("please enter a number = "))
        except:
            print("whoops,This is not a number")
            continue
        else:
            print("yes,thank you")
            break
        finally:
            print("end of try/except/finally")
            print("i will always run at last")
ask_for_int()