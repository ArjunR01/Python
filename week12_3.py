from tkinter import *


root=Tk()

c=Canvas(root)

line=c.create_line(200,200,300,300,width=4)
oval=c.create_oval(175,100,100,175,width=4)
arc=c.create_arc(200,200,300,300,width=4)
poly=c.create_polygon(50,50,100,80,120,120,100,190,width=3)

c.pack()







root.mainloop()