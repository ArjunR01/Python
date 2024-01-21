n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
o=list(student_marks[query_name])
sum=sum(o)/len(o)
print(sum)