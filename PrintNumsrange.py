'''python Programs to Print numbers in a range without using loops '''

def Print (l,r):
    if (l>r):
        return 0   
    
    Print(l,r-1)
    print ()
    print (r,end = " ")


if __name__ == '__main__':
    l = 1
    r = 10 
    print(Print(l,r))