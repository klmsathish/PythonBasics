a = int(input("ENTER A NUMBER = "))
b = int (input("ENTER A  NUMBER = "))
PI = 3.14
select = int(input("chose any one \n 1.square 2. rectangle \n 3. circle "))
if(select == 1 ):
    print("Area Of Square = ",a**2)
if(select == 2):
    print("AREA OF RECTANGLE = ",a*b)
if(select == 3):
    print("AREA OF CIRCLE = ",PI*a*a)
else:
    print("SORRY INVALID INPUT")

