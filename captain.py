n=int(input())
room=set(map(int,input().spilt()))
l=list(room)
for i in range(0,len(l)):
    if(l.count(i)<n):
        print(l[i])

