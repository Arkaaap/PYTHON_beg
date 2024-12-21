'''Python Program To Print The Binary Equivalent Of An Integer W/o Using Recursion '''


def Binary_Conversion (N):

    for i in range (1,N//2):
        print (N%2,end = "")


if __name__ == '__main__':
    n = int (input("Enter The Number :"))
    print (Binary_Conversion(n))

