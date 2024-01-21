def s(roll,*m):
    sum=0
    print('\n',roll,end=' ')
    for i in m:
        sum=sum+i
        avg=sum/len(m)
        print(i,end=' ')
    print(round(avg,2))
    print("\n")
s(14,23,24,25)
s(67,56,23,46)