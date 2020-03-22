print("                                                          WELCOME TO ABC MART                        ")


name = []
price = []
number=int(input("enter number of products = "))
for i in range(number):
    name.append(input("enter product name = "))
    price = int(input("enter product price = "))

    if(price >= 1000):
        print("discount offered to you is 15%")
        new_price = price - (price*0.15)
        print("total amount = ",new_price)
    elif(price > 500):
        print("discount offered to you is 10%")
        new_price_1 = price - (price*0.10)
        print("total amount = ",new_price_1)
    else:
        print("no dicount offered for you ")
        print("total amount = ",price)
print("                                                                               THANK YOU                                                     ")
print("                                                                               COME AGAIN                                                    ")



