def ask_for_int():

    while True:
        try:
            age = int(input("enter your age = "))
        except(ValueError):
            print("Entered input is not a number")
            continue
        else:
            if(age >= 18):
                print("eligible to vote")
                break
            else:
                print("not eligible to vote")
                break
ask_for_int()