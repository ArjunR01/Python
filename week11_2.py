import pandas as p

a=p.read_csv("Book1.csv")

a=p.DataFrame(a)
print(a)

new=a.groupby("x")

print(a["x"]>2)

print(new.first())