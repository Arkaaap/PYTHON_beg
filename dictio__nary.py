## make 1 lists of different domain and 1 for suitable language 

domain = ['Software Enginner','system administrator','game dev','web dev','android dev','ios dev','Ethical hacker']
## this is domain list 
language = ['C,C++,JAVA','UNIX,C','C++,C#,UNITY','NODEJS,REACH,JS,HTML,CSS','ANDROIDSTUDIO,JAVA,KOTLIN','SWIFT,C','C,C++,LINUX,UNIX']
## this is language list 

# print(domain)
# print ()
# print(language)

# print("After merging them >>>>")

dic_domain_language = dict(zip(domain,language))

## this  is where merge two lists and make them a dictionary 

print (dic_domain_language)
## printing dictionray 
print ()
##giving a \n

print(dic_domain_language['Ethical hacker'])
## fethching language section of language list for domain 'Ethical hacking '
del dic_domain_language ['web dev']
## DELETING WEB DEV AS I'M NOT A FAN OF WEB DEV 
print (dic_domain_language)
## PRINTING AGAIN THE DICTIONARY WITHOUT WEB DEV THIS TIME :0

dic_domain_language.clear()
## Clearing the dictionary ;)
print (dic_domain_language)
## printing to be sure the dictionary is cleared or not 

