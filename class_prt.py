class si:
    def __init__(self):
        print ("I'm in Constructor")
    def simple_interest(self,p,t,r,):
        print (f"Total : ",p*t*r//100)


p = int (input("Enter the principal value : "))
t = int (input("Enter the time / Duration : "))
r = int (input("Enter the rate : "))
obj = si()
obj.simple_interest(p,t,r)

