n1=int(input("ENter two numbers"))
n2=int(input("ENter two numbers"))
n3=input("Enter the operation")

if(n3=='+'):
    ans= lambda n1,n2:n1+n2


elif(n3=='-'):
    ans= lambda n1,n2:n1-n2

elif(n3=='*'):
    ans= lambda n1,n2:n1*n2

elif(n3=='/'):
    ans= lambda n1,n2:n1/n2

print(ans(n1,n2))