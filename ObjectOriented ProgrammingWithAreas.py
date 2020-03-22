class rectangle:
    def __init__(self):
        pass
    def getarea(self,l,b):
        area = l*b
        print("area of rectangle is " ,area)
class circle :
    def __init__(self):
        pass
    def getarea(self,r):
        area = 3.14*(r**2)
        print("area of circle is ",area )
obj = rectangle()
obj1 = circle()
obj.getarea(2,7)
obj1.getarea(3)