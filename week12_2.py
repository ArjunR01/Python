from tkinter import *

root=Tk()

root.geometry("700x600")


a=root.title("Registration form")

l1=Label(text="name",font="bold")
l1.place(x=13,y=15)

l2=Label(text="Roll",font="bold")
l2.place(x=13,y=95)

l3=Label(text="branch",font=("bold"))
l3.place(x=13,y=195)

l4=Label(text="section",font="bold")
l4.place(x=13,y=295)

l5=Label(text="adress",font="bold")
l5.place(x=13,y=395)

e=Entry(root)
e.place(x=80,y=18)

e1=Entry(root)
e1.place(x=80,y=100)

e2=Entry(root)
e2.place(x=80,y=200)

e3=Entry(root)
e3.place(x=80,y=300)

e4=Entry(root)
e4.place(x=80,y=395)

# l=[e.get(),e1.get(),e2.get(),e3.get()]


def button():
    new=Tk()
    new.geometry("400x200")
    new.title("Details")
    l=Label(new,text=f"Name : {e.get()}\n Roll : {e1.get()}\n Branch : {e2.get()}\n Section : {e3.get()}\n Adress : {e4.get()}",font=("bold,25"))
    l.pack()

b=Button(text="Submit",command=button,bg="orange")
b.place(x=120,y=500)










root.mainloop()


