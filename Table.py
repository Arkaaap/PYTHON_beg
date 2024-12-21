'''Python program To Print Table Of A Given Number '''

def Table(N):
    for i in range (1,10+1):
        print (f"The Table Of This {N} is {N }x{ i} = {N*i}")


if __name__ == '__main__':
    n = int (input("Enter the N :"))
    print (Table(n))