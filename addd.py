AD = [1,2,3,3,4]
DD = [5,7,7,7,5]
l = [0,0,0,0,0,0,0]

for i in range (5):
    for j in range (AD[i] , DD[i]+1):
        l [j-1] += 1

m = max(l)

for x in range (len(l)):
    if l [i] == m:
        print (i+1,'Day')

