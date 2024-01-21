def average(array):
    s=set(array)
    add=sum(s)
    n=len(s)
    average=add/n
    return average
    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)