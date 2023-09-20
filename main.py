from tkinter import *
from tkinter.ttk import *



root = Tk()
root.title("Calculator")
root.geometry("400x200")
num = StringVar() # создадим переменную для отображения значений на табло калькулятора
num.set(0)        # установим значение переменной равное 0
label = Entry(text=num, justify=RIGHT)
label.pack()

Button(text=1).place(x=0, y=50)
Button(text=2).place(x=75, y=50)
Button(text=3).place(x=150, y=50)
Button(text=4).place(x=230, y=50)
Button(text=5).place(x=310, y=50)
Button(text=6).place(x=0, y=75)
Button(text=7).place(x=75, y=75)
Button(text=8).place(x=150, y=75)
Button(text=9).place(x=230, y=75)
Button(text=0).place(x=310, y=75)
Button(text="/").place(x=0, y=100)
Button(text="*").place(x=75, y=100)
Button(text="-").place(x=150, y=100)
Button(text="+").place(x=230, y=100)
Button(text="=").place(x=310, y=100)

root.mainloop()