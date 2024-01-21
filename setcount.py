n=int(input())
l=[]
#name=list(map(int,input().spilt))
for i in range(n):
    name=input()
    l.append(name)
k=set(l) 
print(len((k)))
