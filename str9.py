a="HellO Arjun"
for i in a:
    if(i.isupper()):
        print(i," is upper case letter")
    elif(i.islower()):
        print(i," is lower case letter")
    else:
        print(i," is not letter")



x="python"
y="python"
print(x+y)
x+=y
print(x)
print(y*3)
for i in y[::2]:
    print(i,end=' ')
print()
for i in y[::-1]:
    print(i,end=' ')
if 'yty' in x:
    print("True")