'''Checking pal str in class '''
class pal():
    def __init__(self,s):
        self.s = s 
    def Ispal(self):
        return self.s[::-1]
    


s = str(input("Enter the string :"))
store = s 
obj = pal(s)
if (obj.Ispal() == store):
    print ("1")
else:
    print ("0")
