from math import factorial

x=int(input('ENter x value='))
n=int(input('ENter no of series='))
sum=0

for i in range(1,n+1):
    sum=sum+((-x)**i/factorial(i))
print(sum)

print((-x)**2/factorial(2))