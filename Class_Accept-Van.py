'''Find the greatest ascending alphabetical order from a string'''

class find:
    def __init__(self,s):
        self.s = s
    def method(self):
        string =  list(self.s.split())
        print (string)
        c = 0 
        for i in range (len(string)):
            if (string[i]== ''.join.sorted(string[i])) == True:
                c = c+1 
            return c 
        

s = str(input("Enter the string :")) 
obj = find(s)
print (obj.method())