''''Python Program to check whether a number is PRIME OR Not prime '''
 
def PRIME(n): 
    flag = 0 
    for i in range (2,n+1):
        if (n%i == 0):
            flag = 1 
            break
        if (flag == 1):
            return 0
        else:
            return 1

if __name__ == '__main__':
    n = int(input("Enter the n :"))
    if (PRIME(n) == 1):
        print (f"The number {n} is Prime")
    else:
        print (f"The number {n} is Not Prime")