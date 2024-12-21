''''Python Program To Find Prime Numbers In A Given Range'''
#l-->r = 1-->5
import math

def is_prime(n):
    flag = 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            flag = 1 
        if (flag == 0):
            return True
        else:
            return False

def Prime(l, r):
    if l > r:
        return -1
    for i in range(l, r + 1):
        if is_prime(i):
            print(f"{i} is Prime")
        else:
            print(f"{i} is Not Prime")

if __name__ == "__main__":
    l = 1  # Starting number of range
    r = 10 # Ending number of range
    Prime(l, r)



































# Function to find prime numbers in a given range
def prime_numbers_in_range(l, r):
    primes = []
    
    # Loop through each number in the range
    for num in range(l, r + 1):
        if num > 1:  # Prime numbers are greater than 1
            is_prime = True
            
            # Check divisibility by numbers from 2 to num-1
            for i in range(2, num):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
    
    return primes

# Driver code
if __name__ == "__main__":
    # Input: range l and r
    l = int(input("Enter the start of the range: "))
    r = int(input("Enter the end of the range: "))
    
    # Call function to find prime numbers in the given range
    prime_numbers = prime_numbers_in_range(l, r)
    
    if prime_numbers:
        print(f"Prime numbers between {l} and {r} are: {prime_numbers}")
    else:
        print(f"There are no prime numbers between {l} and {r}.")
