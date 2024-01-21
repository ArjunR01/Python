n=int(input("ENter number="))
ans=0
for i in range(2,n):
    if(n%i==0):
        ans=ans+1
if(ans>=1):
    print("Not")
else:
    print("prime")