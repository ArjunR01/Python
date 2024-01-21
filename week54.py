import re
s=input()
s1=re.findall("^[a-zA-Z].",s)
s2=re.findall("[a-zA-Z]+$",s)
s3=re.findall("^[a-zA-Z]*",s)
s4=re.split("\s",s)


print(s1,s2,s3,s4)