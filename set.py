s1={1,2,3,4,5}
s2={3,4,6,7,8}

print(s1.symmetric_difference(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
s1.remove(5)
print(s1)
s1.update(s2)
print(s1)
s1.add(10)
print(s1)