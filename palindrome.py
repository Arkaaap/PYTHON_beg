#101 is a plaindrome 
n=int(input("Enter the n : "))
p=0
rem=0
store=n
while (n>0):
    rem=n%10
    p=p*10+rem
    n=n//10


if (p==store):
        print ("Palindrome")
else:
        print ("Not")