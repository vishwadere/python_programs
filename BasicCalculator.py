from tkinter import *
parent=Tk()
parent.title("Basic calculator")
#f=Frame(parent,height=200,width=200)
#canvas1=Canvas(parent, width=300, height=300).pack()

l1=Label(parent,text="Enter first no.:")
l1.grid(row=1,column=0)
en=Entry(parent,width=8)
en.grid(row=1,column=1)

l2=Label(parent,text="Enter second no.:")
l2.grid(row=3,column=0)
en2=Entry(parent,width=8)
en2.grid(row=3,column=1)

l=Label(parent, text="Result : ")
l.grid(row=5,column=0)
res=Entry(parent,width=15)
res.grid(row=5,column=1)
ans=0

def add():
    one=int(en.get())
    two=int(en2.get())
    #ans=one+two
    ans=res.insert(0,str(one+two))

def sub():
    one=int(en.get())
    two=int(en2.get())
    #ans=one-two
    ans=res.insert(0,str(one-two))

def product():
    one=int(en.get())
    two=int(en2.get())
    #ans=one*two
    ans=res.insert(0,str(one*two))

def div():
    one=int(en.get())
    two=int(en2.get())
    #ans=one/two
    ans=res.insert(0,str(one/two))


b1=Button(parent, text="    +   ",command=add, fg="white", bg="black", width=2)
b2=Button(parent, text="     -    ",command=sub, fg="white", bg="black", width=2)
b3=Button(parent, text="     x    ",command=product, fg="white", bg="black", width=2)
b4=Button(parent, text="     /    ", command=div, fg="white", bg="black",width=2)

b1.grid(row=1,column=3)
b2.grid(row=2,column=3)
b3.grid(row=3,column=3)
b4.grid(row=4,column=3)



mainloop()
