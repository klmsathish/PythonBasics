list = [1,78,56,45,89,20,100]
print("my original value is ",list)
print("max vaule of the list is",max(list))
print("minimum value of the list is",min(list))
print("sorted list is",sorted(list))
print("removing last element",list.pop())
print("removing element based on index ",list.pop(4))
print("check",45 in list)
print("check not in list", 2001 not in list)
print(list*2)
print("update the list" )
list[0]=1001
print(list)
del list[2]
print("after delete",list)
print(list[ : :-1])