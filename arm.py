class arm:
    def __init__(self,n):
        self.n  = n 
    def arm_(self):
        r = 0 
        n = self.n 
        a = 0 
        while (n>0):
            r = n%10 
            a = (r*r*r)+a 
            n= n//10 
        return a 

if __name__ == '__main__':
    n = int(input("Enter the N :"))
    obj = arm(n)
    store = n 
    if (obj.arm_() == store):
        print (f"The number  {n}is an Armstrong")
    else:
        print (f"The number {n}is Not an ArmStrong Number ")
