import re
s=input()
s1=re.findall("[0-9][0-9]$",s)
s2=re.findall("[a-zA-Z]",s)
s3=re.findall("^[0-9][0-9]",s)

if(len(s2)==3 and len(s)==10 and s3 and s1):
    print("valid")
    print("section is ",s2[2])
    x=s3[0][0]
    y=s3[0][1]
    print(f"Year is 20{x}{y}")


else:
    print("Invalid")


