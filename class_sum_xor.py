'''Take a number as an input and find the sum of the even places of that number 
and xor of the odd places '''

class sum_xor:
    def __init__(self,n):
        self.n = n 
    def method(self):
        s = str(self.n)
        sum = 0 
        x = 0 

        for i in range (len(s)):
            if (i%2 == 0):
                sum = sum+int(s[i])
            else:
                x = x^int (s[i])
        return (sum-x)
    

n = int (input("Enter the number : "))
obj = sum_xor(n)
print (obj.method())

