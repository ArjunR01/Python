import matplotlib.pyplot as p
import numpy as np
import csv
c=[]
d=[]
with open('Book1.csv', mode ='r')as arjun:
 text = csv.reader(arjun)
 for i in text:
       c.append(i[0])
       d.append(i[1])
                

c.pop(0)
d.pop(0)

a=np.array(c)
b=np.array(d)     

p.plot(a,b,marker='o')
p.xlabel("x")
p.show()