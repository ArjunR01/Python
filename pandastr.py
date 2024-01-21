import pandas as p

data = [{'Name': 'Alice', 'Age': 25, 'City': 'New York'},
        {'Name': 'Bob', 'Age': 30, 'City': 'San Francisco'},
        {'Name': 'Bob', 'Age': 35, 'City': 'Los Angeles'}]

d=p.DataFrame(data)

a=d.groupby(["Age","City"])

print(a.first())
