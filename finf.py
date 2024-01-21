def square(x):
    return x*x

cube=lambda a:a**3

def result(square,cube,n):
    print(square,cube,n)

n=2
result(square(n),cube(n),n)