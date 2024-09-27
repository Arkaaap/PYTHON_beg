s = str(input("Enter the string :"))
l = list(s.split())
c = 0 
m = len(l)

for i in range (m):
    if (l[i] == ''.join(sorted(l[i])))==True:
        c = c+1 
print (c)