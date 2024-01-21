import numpy as n
a=(n.linspace(1.0,3.0,num=4,endpoint=False))
c=n.linspace(0.0,1.0,num=4,endpoint=False)

b=[True,False,True,False]
arr=a[b]

print(a)
print(arr)


print(n.where(a==2.0))

print(n.concatenate((a,arr)))



# print(n.concatenate(a,arr))

