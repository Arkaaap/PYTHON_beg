class Sum:
    def __init__(self,n):
        self.n = n 
    def Sum_(self):
        sum = 0 
        for num in range (1,self.n+1):
            sum +=num 
        return sum 

if __name__ == '__main__':
    n = int(input("Enter the Number :"))
    obj = Sum(n)
    print (obj.Sum_())
