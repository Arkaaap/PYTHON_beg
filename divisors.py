'''Python Program to find all the didvisors of an integer '''
import math as m 
def Find(n):
    c = 0 
    for i in range (1,int(m.sqrt(n))):
        if (n%i== 0):
            c = c+1
            print(i) 
            print ()
            print (f"The Count of divisors {n} of the  {c}")



if __name__ == '__main__':
    n = int(input("Enter the N :"))
    Find(n)