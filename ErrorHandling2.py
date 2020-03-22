while True:
    try:
        a = int(input("enter the num = "))
        b = (input("enter the num = "))
        c = a + b
        print(c)
    except(TypeError):
        print("wrong")
    except(ValueError):
        print("bad")
    finally:
        print("thank you")
