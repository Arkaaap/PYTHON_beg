# PYTHON_beg



#list

list = [1,2,3,4,5,6,8,-8]
#print(dir(list))
#list.append(90)
#list.insert(0,'String')
#list.sort ()
#list.reverse()
#list.clear()
print (list)


\n 



Tuple
list = (1,2,3,4,5,6,8,-8)
print (type(list))
#print (dir(list))
#print (list.count(-8))
print (list.index(-8))


\n



Set 
list = {1,2,3,4,5,6,8,-8}
print (type(list))
print (dir(list))
list.add(-80)
set = list.copy()
set.pop()
set.remove(-8)
print (set)
print (set)


\n


Dictionary:
dict = {
    1:'A',
    2:'B',
    3:'C'
}
#print(type(dict))
print (dir(dict))
dict2 = dict.copy()
dict.pop(3)
print (dict)
print(dict2)
print (dict.get(1))
print (dict.values())


string :


string= "203808399"
print (dir(string))
print ()
print (string.upper())
print (string.lower())
print (string.isalnum())#true if alphabet or number 
print (string.isalpha())#true if only alphabet  
print (string.find('S'))#find an iteam 
print (string.split())#list 
print (string.capitalize())
print (string.replace ('T','t'))#old ->new 
print (string.islower())
print (string.count('T'))
print (string)
print (string.isdigit())#true if only numbers 
print (string.isnumeric())#true if only numbers 
print (string.isspace())#true if only space 
