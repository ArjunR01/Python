list=[]
a=[]
li=[]
def acces(n):
    name=input('Enter the name =')
    score=float(input("ENter the score ="))
    list.append([name,score])


n=int(input())
for i in range(0,n):
    acces(i)  
print(list)

for i in range(0,n-1):
    for j in range(i+1,n):
        if(list[i][1]>list[j][1]):
            temp=list[i]
            list[i]=list[j]
            list[j]=temp
        
print(list)  
k=0
for i in range(1,n-1):
    if(list[0][1]==list[i][1]):
        a.append(list[i])
        k=k+1  
        
    


l=k+1

m=k

for i in range(l,n):
    if(list[l][1]==list[i][1]):
        a.append(list[i])
        m+=1
print(a)
#print(list[l][0])
#print("After sorting the list of a is given as below =",a)
#a.sort()
for i in range(k,m):
    if(a[i]==None):
        continue
    else:
        li.append(a[i])
li.sort()
#print(li)
for i in range(0,len(li)):
    print(li[i][0])

