class rev:
    def __init__(self,s):
        self.s = s 
    def reverse (self):
        return self.s[::-1]


s = str(input("Enter the string : "))
obj =rev(s)
print (obj.reverse())
