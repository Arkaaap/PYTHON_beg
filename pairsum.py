'''Wap to print pair sum of a number and print the pair idx number '''

list =  [1,2,3,3,4]
t = 6

for i in range (len(list)):
    for j in range (i+1,len(list)):
        if (list[i] + list[j] == t):
            print (i,j)
            break