'''print the Sum Of Numbers 1/n^2 +1/n^3 +1/n^4 + 1/(n-1)^n'''


def sum (n):
    s = 0 
    for i in range (1,n+1):
        s = s+(1/n**(i+1))
    
    return s 

n = int(input())
result = sum(n)
print ("tHE SUMMATION OF Numbers are : ",result)