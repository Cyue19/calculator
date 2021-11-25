#Example: Calculator
import tkinter
top = tkinter.Tk()
top.title("Simple Calculator")

entry = tkinter.Entry(top, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
    current = entry.get()
    entry.delete(0, "end")
    entry.insert(0, str(current) + str(number))

def button_clear():
    entry.delete(0, "end")

def button_add():
    global num1
    global func
    func = "add"
    num1 = int(entry.get())
    entry.delete(0, "end")

def button_equal():
    global num1
    num2 = int(entry.get())
    if func == "add":
        result = num1 + num2
    elif func == "subtract":
        result = num1 - num2
    elif func == "multiply":
        result = num1 * num2
    elif func == "divide":
        result = num1 / num2
    entry.delete(0, "end")
    entry.insert(0, result)

def button_subtract():
    global num1
    global func
    num1 = int(entry.get())
    func = "subtract"
    entry.delete(0, "end")

def button_multiply():
    global num1
    global func
    num1 = int(entry.get())
    func = "multiply"
    entry.delete(0, "end")

def button_divide():
    global num1
    global func
    num1 = int(entry.get())
    func = "divide"
    entry.delete(0, "end")

button1 = tkinter.Button(top, text="1", pady=20, padx=40, command=lambda: button_click(1))
button2 = tkinter.Button(top, text="2", pady=20, padx=40, command=lambda: button_click(2))
button3 = tkinter.Button(top, text="3", pady=20, padx=40, command=lambda: button_click(3))
button4 = tkinter.Button(top, text="4", pady=20, padx=40, command=lambda: button_click(4))
button5 = tkinter.Button(top, text="5", pady=20, padx=40, command=lambda: button_click(5))
button6 = tkinter.Button(top, text="6", pady=20, padx=40, command=lambda: button_click(6))
button7 = tkinter.Button(top, text="7", pady=20, padx=40, command=lambda: button_click(7))
button8 = tkinter.Button(top, text="8", pady=20, padx=40, command=lambda: button_click(8))
button9 = tkinter.Button(top, text="9", pady=20, padx=40, command=lambda: button_click(9))
button0 = tkinter.Button(top, text="0", pady=20, padx=40, command=lambda: button_click(0))
button_add = tkinter.Button(top, text="+", padx=39, pady=20, command=button_add)
button_equal = tkinter.Button(top, text="=", padx=39, pady=20, command=button_equal)
button_clear = tkinter.Button(top, text="Clear", padx=124, pady=20, command=button_clear)

button_subtract = tkinter.Button(top, text="-", padx=40, pady=20, command=button_subtract)
button_multiply = tkinter.Button(top, text="*", padx=41, pady=20, command=button_multiply)
button_divide = tkinter.Button(top, text="/", padx=40, pady=20, command=button_divide)

#Put buttons on screen
button1.grid(row=4, column=0)
button2.grid(row=4, column=1)
button3.grid(row=4, column=2)

button4.grid(row=3, column=0)
button5.grid(row=3, column=1)
button6.grid(row=3, column=2)

button7.grid(row=2, column=0)
button8.grid(row=2, column=1)
button9.grid(row=2, column=2)

button0.grid(row=5, column=0)
button_clear.grid(row=1, column=0, columnspan=3)
button_add.grid(row=6, column=0)
button_equal.grid(row=6, column=2)

button_subtract.grid(row=6, column=1)
button_multiply.grid(row=5, column=1)
button_divide.grid(row=5, column=2)


top.mainloop()