'''PRINT THE FACTORIAL OF NUMBERS AND ADD THEM 1!+2!+3!+..+(n-1)!'''

def fact (n):
    f = 1 
    for i in range (2,n+1):
        f = f*i 
    return f 

n = int(input("Enter the number : "))

sum = 0 

for i in range (1,n+1):
    sum+=fact(i)

print ("The sum of fcatorials are ",n,sum)