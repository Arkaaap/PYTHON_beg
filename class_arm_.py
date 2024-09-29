'''Checking armstrong in class'''

class arm:
    def __init__(self,n):
        self.n= n 
    def arm_strong(self):
        rem = 0 
        arm = 0 
        while (self.n>0):
            rem =self.n%10
            arm = (rem*rem*rem) +arm 
            self.n = self.n//10 
        
        return arm 
    

n = int (input("Enter the n : "))
store = n 
obj = arm(n)

if (obj.arm_strong() == store):
    print ("1")
else:
    print ("0")
