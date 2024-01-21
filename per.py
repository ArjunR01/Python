n=int(input())
for i in range (0,n):
    name=input()
    marks1=int(input())
    marks2=int(input())
    marks3=int(input())
    name=[marks1,marks2,marks3]

name2=input("Enter the name you want to search =")
if(name2==name):
    for i in range(0,n):
       sum+=name[i]
    average=sum//3
print(average)       

    