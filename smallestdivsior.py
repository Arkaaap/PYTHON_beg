'''Python Program to Find the smallest divisor of an integer'''

import math 
from math import *
def Find_Check(n):
    if n == 1:
        return 1  # 1 is divisible only by itself
    
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return i  # The first divisor greater than 1
    
    return n  # If no divisor is found, n is prime

if __name__ == '__main__':
    n = int(input("Enter the number: "))
    print(f"The smallest divisor of {n} is: {Find_Check(n)}")
