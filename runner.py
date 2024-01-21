n=int(input())
arr=[]
for i in range(0,n):
    #l=int(input())
    arr.append(int(input()))

arr.sort()    

while(arr[n-1]==arr[n-2]):
    n=n-1

print(arr[n-2])    


'''print("Array elemnts are:")
for i in range(n):
    print(arr[i])    '''