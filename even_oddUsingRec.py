''''BASE CASE WILL BE CHECKING FOR IF THE LEFT NUMBER IS GREATER THAN RIGHT IF IT'S GREATER THAN RIGHT THE FUNCTIUON WILL BE RETURNED EXAMPLE : (5,10) L = 5 , R = 10 IF 5>10 NEVER HAPPENS 


    SO IF 10-2 = 8 ANS SO ON TILL SOMENUMNER COMES LIKE 4 OR 3 WHICH WILL SATISFY THE CONDITION LIKE 5>4 THE FUNCTION RETURNS 
    AND EVERY TIME IT;S CHECKING WHETHER THE CURRENT NUMBER IS EVEN IF IT'S EVEN THEN WE CALL THE SAME FUNCTION AND THIS TIME SUBTRACT 2 FROM THE RIGHT SIDE OF NUMBER LET'S SAY (5,10) -> (5,8)->(5,6)->(5,4) 'RETURNS'''

def Even(l,r):
    if (l>r):
        return 
    if (r%2 == 0):
        Even(l,r-2)
    else:
        Even(l,r-1)

    if (r%2 == 0 ):
        print (r,end = '')


def Odd(l,r):
    if (l>r):
        return 
    if (r%2 == 1):
        Odd(l,r-2)
    else:
        Odd(l,r-1)
    
    if (r%2 == 1):
        print (r,end = '')

l = 1
r = 5
print ("Even Numbers")
Even(l,r)
print ()
print ("Odd Numbers")
Odd(l,r)
