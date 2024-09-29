'''Form a function which will find a unique outta three different nums'''
class unique:
    def __init__(self,n,n1,n2):
        self.n = n 
        self.n1 = n1 
        self.n1 = n2 
    def unique_num(self):
        n = int (input(" "))
        n1 = int (input("  "))
        n2 = int (input("   "))
        s = str(n)
        s1 = str(n1)
        s2 =str(n2)

        for i in range (0,4):
            print (max(s[i],s1[i],s2[i]))


n = int (input(" "))
n1 = int (input("  "))
n2 = int (input("   "))
obj = unique(n,n1,n2)
print (obj.unique_num())
