class two:
    def __init__(self,l,t):
        self.l = l 
        self.t = t 
    def pairsum (self):
        c = 0 
        for i in range (len(self.l)):
            for j in range (i+1,len((self.l))):
                if (self.l[i] +self.l[j] == self.t):
                    c = c+1 
                    
                    return c 

l = [-1,2,3,4,5]
t = 1
obj = two(l,t)
print (obj.pairsum())