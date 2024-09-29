'''Checking Palindrome number in class'''

class Pal:
    def __init__(self,n):
        self.n= n 
    def Palindrome(self):
        rem = 0 
        p = 0 
        while (self.n>0):
            rem =self.n%10
            p = p*10+rem
            self.n = self.n//10 
        
        return p 
    

n = int (input("Enter the n : "))
store = n 
obj = Pal(n)

if (obj.Palindrome() == store):
    print ("1")
else:
    print ("0")
