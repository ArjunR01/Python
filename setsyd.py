n = int(input())
set1 = list(map(int, input().split()))
a=set(set1)
m = int(input())
set2 = list(map(int, input().split()))
b=set(set2)
k=a.symmetric_difference(b)
m=len(k)
f=list(k)
f.sort
for i in range(m):
    print(f[i])
