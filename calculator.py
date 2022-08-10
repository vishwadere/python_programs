from tkinter import *
root = Tk()
root.title("Simple Calcuator")
e = Entry(root, width=40)
e.grid(row=0, column=0, columnspan=3)

def button_click(number):
    #e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addtion"
    f_num = int(first_number)
    e.delete(0, END)

def button_equal():
    second_number=e.get()
    e.delete(0, END)

    if math == "addtion":
       e.insert(0, f_num + int(second_number))

    if math == "subtraction":
       e.insert(0, f_num - int(second_number))

    if math == "multiplication":
       e.insert(0, f_num * int(second_number))

    if math == "division":
       e.insert(0, f_num / int(second_number))


def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)


button_1 = Button(root, text="1", command=lambda: button_click(1), width=3)
button_2 = Button(root, text="2", command=lambda: button_click(2), width=3)
button_3 = Button(root, text="3", command=lambda: button_click(3), width=3)
button_4 = Button(root, text="4", command=lambda: button_click(4), width=3)
button_5 = Button(root, text="5", command=lambda: button_click(5), width=3)
button_6 = Button(root, text="6", command=lambda: button_click(6), width=3)
button_7 = Button(root, text="7", command=lambda: button_click(7), width=3)
button_8 = Button(root, text="8", command=lambda: button_click(8), width=3)
button_9 = Button(root, text="9", command=lambda: button_click(9), width=3)
button_0 = Button(root, text="0", command=lambda: button_click(0), width=3)
button_add = Button(root, text="+", command=button_add, width=3,fg="red")
button_equal = Button(root, text="=", command=button_equal, fg="white", bg="black", width=3)
button_clear = Button(root, text="clr", command=button_clear, fg="white", bg="black",width=5)

button_subtract = Button(root, text="-", command=button_subtract, width=3,fg="red")
button_multiply = Button(root, text="*", command=button_multiply, width=3,fg="red")
button_divide = Button(root, text="/", command=button_divide, width=3,fg="red")

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=1)
button_clear.grid(row=7, column=1, columnspan=1)
button_add.grid(row=4, column=0)
button_equal.grid(row=4, column=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

root.mainloop()
