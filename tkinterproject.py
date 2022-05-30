from tkinter import *

root = Tk()
root.geometry("200x250+300+200")
root.title("calculator")
root.configure(bg="orange")


def enter_number(number):
    str_number = entry1.get() + str(number)
    entry1.delete(0, END)
    entry1.insert(0, str(str_number))


def operation(sign):
    value = entry1.get()
    if value[-1] in "+-*/":
        value = value[:-1]
    entry1.delete(0, END)
    entry1.insert(0, value + sign)

def calc():
    value=entry1.get()
    if value[-1] in '+-*/':
        value=value+value[:-1]
    entry1.delete(0, END)
    entry1.insert(0,eval(value))

entry1 = Entry(root, justify=RIGHT, font=(20), width=15)

but1 = Button(root, text='1', bd=7, command=lambda: enter_number(1))
but2 = Button(root, text='2', bd=7, command=lambda: enter_number(2))
but3 = Button(root, text='3', bd=7, command=lambda: enter_number(3))
but4 = Button(root, text='4', bd=7, command=lambda: enter_number(4))
but5 = Button(root, text='5', bd=7, command=lambda: enter_number(5))
but6 = Button(root, text='6', bd=7, command=lambda: enter_number(6))
but7 = Button(root, text='7', bd=7, command=lambda: enter_number(7))
but8 = Button(root, text='8', bd=7, command=lambda: enter_number(8))
but9 = Button(root, text='9', bd=7, command=lambda: enter_number(9))
but0 = Button(root, text='0', bd=7, command=lambda: enter_number(0))

entry1.grid(row=0, column=0, columnspan=4, stick=EW, padx=3)
but1.grid(row=1, column=0, stick=NSEW, padx=3, pady=3)
but2.grid(row=1, column=1, stick=NSEW, padx=3, pady=3)
but3.grid(row=1, column=2, stick=NSEW, padx=3, pady=3)
but4.grid(row=2, column=0, stick=NSEW, padx=3, pady=3)
but5.grid(row=2, column=1, stick=NSEW, padx=3, pady=3)
but6.grid(row=2, column=2, stick=NSEW, padx=3, pady=3)
but7.grid(row=3, column=0, stick=NSEW, padx=3, pady=3)
but8.grid(row=3, column=1, stick=NSEW, padx=3, pady=3)
but9.grid(row=3, column=2, stick=NSEW, padx=3, pady=3)
but0.grid(row=4, column=0, stick=NSEW, padx=3, pady=3)

root.grid_columnconfigure(0, minsize=50)
root.grid_columnconfigure(1, minsize=50)
root.grid_columnconfigure(2, minsize=50)
root.grid_columnconfigure(3, minsize=50)

root.grid_rowconfigure(0, minsize=50)
root.grid_rowconfigure(1, minsize=50)
root.grid_rowconfigure(2, minsize=50)
root.grid_rowconfigure(3, minsize=50)
root.grid_rowconfigure(4, minsize=50)

but11 = Button(root, text='+', bd=7, command=lambda: operation('+'))
but12 = Button(root, text='-', bd=7, command=lambda: operation('-'))
but13 = Button(root, text='*', bd=7, command=lambda: operation('*'))
but14 = Button(root, text='/', bd=7, command=lambda: operation('/'))
but15 = Button(root, text='=', bd=7, command=calc)
but16 = Button(root, text='с', bd=7, command=lambda: operation('='))

but11.grid(row=1, column=3, padx=3, pady=3, stick=NSEW)
but12.grid(row=2, column=3, padx=3, pady=3, stick=NSEW)
but13.grid(row=3, column=3, padx=3, pady=3, stick=NSEW)
but14.grid(row=4, column=3, padx=3, pady=3, stick=NSEW)
but15.grid(row=4, column=2, padx=3, pady=3, stick=NSEW)
but16.grid(row=4, column=1, padx=3, pady=3, stick=NSEW)

root.mainloop()
