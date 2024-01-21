'''list=(1,2,3,4)
print(sum(list))

x=int(input())
y=int(input())
z=int(input())
n=int(input())

if(x>y and x>z):
    temp=x
elif(y>x and y>z):
    temp=y
else:
    temp=z

for i in range(0,temp) :
    for j in range(0,temp):
        for k in range(0,temp):
            if((i+j+k)!=n):
               list=[i,j,k]
               print(list,end='')'''
'''x = int(input())
y = int(input())
z = int(input())
n = int(input())
print(list([i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)  if i+j+k !=n))'''

x=2
y=7
print(list([i,j] for i in range(x+1) for j in range(y+1)))

