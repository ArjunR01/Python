str=input("ENter your string=")
str2="java"
# print(str*str2)
k=len(str)
for i in str[::2]:
    print(i)


str+=str2
# print(str*15,end=' ')
print(str)
print(str2)
