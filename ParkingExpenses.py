select = int(input("1.car \n2. bike \n3.truck"))
hour = int(input("enter time = "))
if(select == 1 ):
    cost = 20*hour
    print("Hi, you have to pay RS.",cost)
    print(cost)
elif(select == 2):
    cost = 10*hour
    print("Hi,you have to pay RS.",cost)
elif(select == 3):
    cost = 30*hour
    print("Hi, you have to pay RS.",cost)
else :
    print("ENTER VALID INPUT")