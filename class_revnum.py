class rev:
    def __init__(self,n):
        self.n = n 
    def reverse (self):
        s = str(self.n)
        return s[::-1]


s = int(input("Enter the Number  : "))
obj =rev(s)
print (obj.reverse())