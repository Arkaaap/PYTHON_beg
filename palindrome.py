def Num_Pal(n):
    s = str(n)
    return s[::-1]
if __name__ == '__main__':
    n = int(input("Enter the n :"))
    store = n #151
    if (Num_Pal(n) == store):
        print ("Palindrome")
    else:
        print ("Not Palindrome")