n=int(input("no of series="))
a=0
b=1
sum=0

while(a<=n):
    sum=a+b
    if(a==n):
        print("fib")
    a,b=b,sum

# for i in range(0,n):
#     if(i==0):
#         a=i
#         print(i)
#     elif(i==1):
#         b=i
#         print(i)
#     else:
#         sum=a+b
#         a,b=b,sum
#         print(sum,end=' ')