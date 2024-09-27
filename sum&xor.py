''' find a number and sum the even places of this and and xor the odd one's and then find out the diffrence between them and print the difference '''
'''57899''' # 1 = 5  2 = 7  3 = 8  4 = 9  5 = 9  even =  7 + 9 = 16  & xor the odd one's and print the differnece 


n = int (input ("Enter the n "))
s = str(n)
sum = 0 
x = 0 
for i in range (len(s)):
    if (i % 2 == 0):
        sum += int (s[i])
    else:
        x ^= int (s[i])

print (sum-x)