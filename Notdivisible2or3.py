def NotDivisible(n):
    if (n%2 != 0 and n%3 != 0):
        print (f"The numbers aren't divisible by 2 either 3 : {n}")
    else:
        print ("Divisible")


if __name__ == '__main__':
    n = int(input("Enter the n :"))
    NotDivisible(n)