n = int(input())
list=[]
for i in range(0,n):
    a=str(input())
    if(a=='insert'):
        e1=int(input())
        e2=int(input())
        list.insert(e1,e2)
    elif(a=='print'): 
        print(list)
    elif(a=='remove'):
        e1=int(input())
        list.remove(e1)  
    elif(a=='append'):
        e1=int(input())
        list.append(e1) 
    elif(a=='sort'):
        list.sort()
    elif(a=='pop'):
        list.pop()
    else:
        list.reverse()  