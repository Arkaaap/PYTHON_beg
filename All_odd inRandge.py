def Odd(l,r):
    if (l>r):
        return 
    if (r%2 == 1):
        Odd(l,r-2)
    else:
        Odd(l,r-1)
    if (r%2 == 1):
        print (f"The Number is odd {r}")


if __name__ == '__main__':

    l = 5 
    r = 10 
    Odd(l,r)
