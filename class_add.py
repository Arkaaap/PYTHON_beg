##SUM OF TWO NUMBERS BY CLASSES AND OBJS

class add :
    def __init__(self):
        print ("I'm in constructor Self")
        
    def sum (self,a,b):
        print(f"Total : ",a,'+',b,{a+b})



a = int(input("Enter the a :"))
b = int(input ("Enter the b : "))
obj = add()
obj.sum(a,b)

