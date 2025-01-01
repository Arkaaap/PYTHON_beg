#Inheritance 
#Inheritance means inherit the attributes and properties to the child class or the sub class from the parent class or the superclass 1.Single Inheritance 2.Multilevel Inheritance 3.Multiple Inheritance 


class a:
    def __init__(self,a,b):
        self.a = a 
        self.b = b 
    def PrintA(self):
        s = 0 
        a = self.a 
        b = self.b 
        s = a+b 
        print (s)
class b(a):# Single Inheritance because b inherits only from a 
    pass
class c(b):# Multilevel inheritance beacus c is inherits from (b) and b inherits from (a) so it's like grand parent-> parent-> child 
    pass


obj= a(10,20)
obj.PrintA()
#there I haven't initialised any properties in class b but since b inherits (a) it has al the properties of a so i don't need to define them again 
obj = b(10,20)
obj.PrintA()
obj = c(10,20)
obj.PrintA()


