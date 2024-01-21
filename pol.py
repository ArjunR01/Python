x=int(input())
n=int(input())
sum=0
for i in range(0,n):
    sum=sum+(x**i)
    print(sum)
print(sum)    
if(sum==n):
    print(True)
else:
    print(False)    
  