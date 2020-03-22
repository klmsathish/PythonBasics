list1=[]
num = int(input("enter the no. of elements = "))
for i in range(num):
    list1.append(int(input("enter the elements = ")))
odd =[]
even =[]
for j in list1:
    if(j%2==0):
        even.append(j)
    else:
        odd.append(j)
print(even,"are even")
print(odd,"are odd")
