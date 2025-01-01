'''Module IV Creating a class '''

class a:
    def __init__(self):
        pass
    
    def Print (self):
        a = 'In the Print Function'
        print (a)

obj = a()

obj.Print() #accessing attributes using '.' notaion 

'''Built In Class Attributes '''
#This is are used for fetching a properties of the class and show the extended information about a particular class whenever the class is being created .
print (a.__name__) # it prints the name of the class name 
print (a.__module__)#It prints the module name where the class is inherited or derived ...
print (a.__doc__)# it will assist to print the document string into a class unfortunately I haven't declared any so it's saying 'None'
print (a.__dict__) #It will print all the namesapces into a class 
print (a.__bases__) #it will print the base class of the class I haven't decalred 



#Destroying object in python we can achieve it's functionality using 'del' keyword in python 
del obj
obj.Print () # it has been deleted using the del keyord so it will give you an error 
