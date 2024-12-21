'''Python Program to find Binary Equivalent Of an Integer'''

# Function to convert decimal number
# to binary using recursion

def Binary_Integer (n):
    if (n>=1):
        Binary_Integer(n//2)
    print (n%2 ,end = " ")


if __name__ == '__main__':
    n = int (input("Enter the n :"))
    print (Binary_Integer(n))