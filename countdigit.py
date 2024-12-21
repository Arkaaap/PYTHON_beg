def count(n):
    s = str(n)
    c = 0 
    for i in range (len(s)):
        c = c+1 

    return c 
    

if __name__ == '__main__':
    n = int(input("Enter the n :"))
    result = count(n)
    print (result)