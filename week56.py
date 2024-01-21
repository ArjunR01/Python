import re
s=input()
x=re.findall("\s",s)
y=re.findall("^[0-9]",s)
z=re.findall("-",s)
if(x or y or z):
    print("invalid")
else:
    print("Valid")
