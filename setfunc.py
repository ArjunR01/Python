n=int(input())
l=list(map(int,input().split()))
a=set(l)
m=int(input())
for i in range(0,m):
    op=input().split()
    if(op[0]=='insert'):
       a.add(int(op[1]))  
    elif(op[0]=='discard'):
       a.discard(int(op[1]))  
    elif(op[0]=='remove'):
       a.remove(int(op[1]))  
    elif(op[0]=='pop'):
       a.pop()          
print(a)        