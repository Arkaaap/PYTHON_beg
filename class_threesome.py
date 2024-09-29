class threesome:
    def __init__(self,l,t):
        self.l = l
        self.t = t  
    def threesum(self):
        ans = self.l[0] +self.l[1] +self.l[2]

        for i in range (len(self.l)-2):
            if (self.l[i] == self.l[i-1]):
                continue

            le = i+1 
            ri = len(self.l)-1 
        
        while (le < ri):
            sum =  self.l[i] +self.l[le] +self.l[ri]

            if (sum  == self.t):
                break
            if (abs(sum - self.t)<abs(ans - self.t)):
                ans = sum 
            if (sum < self.t):
                le = le+1 
            else:
                ri = ri-1
        
        return ans 
    
l = [-1,2,1,-4]
t = 1
obj = threesome(l,t)
print (obj.threesum())