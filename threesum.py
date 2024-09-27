list = [-1,2,1,-4]
t = 1
ans = list[0] + list[1] + list[2]
for i in range (len(list)-2):
    if (i>0 and list[i] == list[i-1]):
        continue

    l = i+1 
    r = len(list ) -1

    while (l != r):
        sum  = list[i] + list[l] + list[r]

        if (sum == t):
            break
        if (abs(sum-t )<abs(ans -t)):
            ans = sum
        if (sum< t):
            l= l+1 
        else:
            r = r-1

print (ans)        