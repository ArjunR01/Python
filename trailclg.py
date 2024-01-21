def student(roll,*m):
    sum=0
    print(roll,end=' ')
    for i in m:
        print(i,end=' ')
        sum=sum+i
    avg=sum/len(m)
    print(avg,end=' ')
    print()
student(12,34,34,34,56,56,34,78,98)
student(15,36,36,36)


print()
# Print Pascal's Triangle in Python
from math import factorial

# input n
n = 5
for i in range(n):
	for j in range(n-i+1):

		# for left spacing
		print(end=" ")

	for j in range(i+1):

		# nCr = n!/((n-r)!*r!)
		print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")

	# for new line
	print()
