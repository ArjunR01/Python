n=int(input())
for i in range(n):
    try:
       a,b=map(int,input().split())
       c=a/b
       print(c)
    except Exception as e :
      print("Error Code:",e)
      