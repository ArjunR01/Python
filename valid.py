str=input()
i=0
if '@' in str and '.' in str:
    while(str[i]!='@'):
        print(str[i],end='')
        i=i+1
else:
    print('invalid email')