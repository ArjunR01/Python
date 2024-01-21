import re
user=input()
s=re.sub(r"g\b","gs",user)
print(s)