class Valuetoolarge(Exception):
    def display(self):
        print("input value is too large")
class Valuetoosmall(Exception):
    def display(self):
        print("input value is too small")
max = 100
while 1:
    try:
        num = int(input("enter the  number = "))
        if num == max:
            print("great you won the game ")
            break
        elif num > max:
            raise Valuetoolarge
        elif num < max:
            raise Valuetoosmall
    except Valuetoosmall as s:
        s.display()
    except Valuetoolarge as l:
        l.display()
        
        
        
        
        
        
        
        
        