'''PRINT THE FACTORIAL OF NUMBERS AND ADD THEM 1/1!+1/2!+1/3!+..+1/(n-1)!'''

def fact (n):
    f = 1 
    for i in range (2,n+1):
        f = f*i 
    
    return 1/f 

n = int (input("ENTER THE n :"))

sum = 0 

for i in range (1,n+1):
    sum = sum+fact(i)

print ("The factorials of numbers divided by one is ",n,sum)