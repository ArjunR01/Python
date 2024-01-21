import matplotlib.pyplot as p
import numpy as np
import csv
l=[]
with open('Book1.csv', mode ='r')as arjun:
 text = csv.reader(arjun)
 for i in text:
		l.append(i)
                
l.pop(0)
print(l)



a=np.array(None)
b=np.array(None)
c=[]
d=[]

for i in l:
        c.append(i[0])

for i in l:
        d.append(i[1])

a=np.array(c)
b=np.array(d)

print(a)

print(b)        



p.plot(a,b,marker='o')

p.xlabel("x axis")
p.ylabel("y axis")
p.show()