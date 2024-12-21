# '''Python program to find Numbers which are divisible by 7 and Multiple of 5 in a given range '''


def Checker (l,r):
    for i in range(l,r+1):
        if (i%7 == 0 ):
            print (f"The numbers are : {i}")
             

if __name__ == '__main__':
    l = 5
    r = 50
    print (Checker(l,r))