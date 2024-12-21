'''python Program to find sum of digits of a number using recursion'''

def Find(n):
    if (n <=0):
        return 0 
    #print(f"tHE SUM OF {n} is {n} itself")
    return n+Find(n-1)


if __name__ == '__main__':
    n = int(input("enter the n :"))
    result = Find(n)
    print (f"The sum of {n} is {result}")
    

