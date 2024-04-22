n=int(input("Enter the number :"))
store=n
arm=0
while (n!=0):
    rem=n%10
    arm=rem*rem*rem+arm
    n=n//10


if (arm==store):
        print ("Armstrong ")
else:
        print ("Not")