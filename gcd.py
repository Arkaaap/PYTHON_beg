def Gcd(n,n1):
    if (n1!=0):
        return Gcd(n1,n%n1)
    else:
        return (n)

n = 366
n1 = 60 
print (f"The {Gcd(n,n1)} ") 
