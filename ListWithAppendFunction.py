check=[]
num = int(input("enter the range = "))
for i in range(num):
    check.append(input("enter the value = "))
print(check)
for j in check:
    if (j%2==0):
        print("even no = )
    else:
        print(f'odd no {j}')
