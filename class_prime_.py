'''Checking Prime numbers in class'''
class prime:
    def __init__(self,n):
        self.n = n 
    def Isprime(self):
        flag =0 
        
        for i in range (2,n):
            if (self.n%i==0):
                flag = 1 
                break
            if (flag == 0):
                return '1'
            else:
                return '0'
                

n =int (input("Enter the n : "))
obj= prime(n)
n1 = obj.Isprime()
print (n1)