# for i in range(int(input())):
#     try:
#         a, b = map(int, input().split())
#         print(int(a//b))
#     except Exception as e:
#         print("Error Code:",e)

i = 5

def f(arg=i):
    print(arg)

i = 6
f()