import pandas as p


marks={"Maths":[20,25,26,18],"Physics":[35,34,23,34],"Chemistry":[34,56,54,34]}

# table=p.DataFrame(marks,index=["Sai Deep,Sai Rohan,Harsha,Kush"])
a=p.DataFrame(marks,index=["Sai Deep","Harsha","Sai Rohan","Tejesh"])


marks={"Maths":[24],"Physics":[45],"Chemistry":[34]}

new=p.DataFrame(marks,index=["Naga"])
# new=a._append(p.DataFrame(marks))
a=a._append(new)
# print(a.head())
# print(a.describe())
# print(a.info())
# print(a[["Maths","Chemistry"]])
# print(a["Maths"]>30)
# print(a.sort_values(by="Maths"))
# a.drop("Chemistry",axis=1,inplace=True)
print(a["Maths"].mean())
# print(a)