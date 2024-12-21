'''python Program to find sum of digits of a number '''


def find(n):
    s = 0 
    for i in range (1,n+1):
        s= s+i 
    
    return s 

if __name__ == '__main__':
    n = int(input("Enter the n :"))
    result = find(n)
    print (f"The sum of digits of {n} is {result}")