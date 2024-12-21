'''Python program to print all the numbers divisible by the given number in a range.'''
def Check(n):
    c = 0 
    for i in range (1,n+1):
        if (n%i == 0):
            c = c+1 
            print ("The count of numbers are divisible by the ",n,i,c)


if __name__ == '__main__':
    n = int(input("Enter the n : "))
    result = Check(n)
    print (result)