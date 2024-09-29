class count_num:
    def __init__(self,n):
        self.n = n 
    def count (self):
        c = 0 
        s = str(self.n)
        for i in range (len(s)):
            c = c+1 
        return c 


s = str(input("Enter the Number : "))
obj =count_num(s)
print (obj.count())