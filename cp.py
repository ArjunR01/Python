def fact(x):
    if(x==1):
        return 1
    else:
        return x*fact(x-1)

def com(a,b):
    ans=a-b
    print(fact(a)/(fact(ans)*fact(b)))

k=com(3,2)