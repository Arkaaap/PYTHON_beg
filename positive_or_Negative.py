def Num_Checker(n):
    if (n  == 0):
        return 
    if (n>0):
        print ("Positive")
    else:
        print ("Negative")

n = int(input("Enetr the Number :"))
print (f"The number is {Num_Checker(n)}")
print ()
Num_Checker(n)
    