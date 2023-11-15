from tkinter import *
from tkinter import ttk
import math
from math import radians


op = None
def handler(ops):
    firstVal = result_entry.get()
    global f_num
    global op
    op = ops
    try:
          f_num = float(firstVal)
          result_entry.delete(0, END)
    except:
         result_entry.delete(0, END)
         result_entry.insert(0, "Syntax Error")
    

def single(ops):
    firstVal = result_entry.get()
    global f_num
    global op
    op = ops
    try:
         f_num = float(firstVal)
         result_entry.delete(0, END)
    except:
         result_entry.delete(0, END)
         result_entry.insert(0, "Syntax Error")
    result_entry.delete(0, END)
    match ops:
        case "root":
            classic_print(math.sqrt(f_num))
        case "sin":
            classic_print(math.sin(radians(f_num)))
        case "cos":
            classic_print(math.cos(radians(f_num)))
        case "tan":
            classic_print(math.tan(radians(f_num)))
    

def clear():
    result_entry.delete(0, END)

def clear1():
    result_entry.delete(len(result_entry.get()) - 1, END)

def classic_print(result):
    if result.is_integer():
            result_entry.insert(0, int(result))
    else:
            result_entry.insert(0, result)
def add_neg():
    firstVal = result_entry.get()
    try:
         f_num = float(firstVal)
         f_num *= -1
         result_entry.delete(0, END)
    except:
         result_entry.delete(0, END)
         result_entry.insert(0, "Syntax Error")
    result_entry.delete(0, END)
    classic_print(f_num)


def equal():
    secon_num = result_entry.get()
    try:
        secon_num = float(secon_num)
        result_entry.delete(0, END)
        match op:
            case "add":
                        classic_print(f_num + secon_num)
            case "sub":
                classic_print(f_num - secon_num)
            case "mul":
                classic_print(f_num * secon_num)
            case "div":
                try:
                    result_entry.insert(0, f_num / secon_num)
                except ZeroDivisionError:
                    result_entry.insert(0, "Math Error")
            case "squ":
                classic_print(math.pow(f_num, secon_num))
            case "root" | "sin" | "cos" | "tan":
                result_entry.get()
            case _:
                result_entry.insert(0, "Syntax Error")
    except:
        result_entry.delete(0, END)
        result_entry.insert(0, "Syntax Error")

def button_click(number):
    current = result_entry.get()
    result_entry.delete(0, END)
    result_entry.insert(0, str(current) + str(number))




root = Tk()
root.title("Calculator")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

root.maxsize(370, 200)
root.minsize(300, 200)
result_entry = Entry(root, font=('Comic Sans', 16), justify="right", bg="black", fg="white")
result_entry.grid(row=0, column=0, columnspan=6, sticky="nsew")

style = ttk.Style()
style.configure("TButton", font=("Comic Sans", 12))

btn1 = ttk.Button(root, text="7", command=lambda:  button_click(7), style="TButton", width=5).grid(column=0, row=1)
btn2 = ttk.Button(root, text="8", command=lambda:  button_click(8), style="TButton", width=5).grid(column=1, row=1)
btn3 = ttk.Button(root, text="9", command=lambda:  button_click(9), style="TButton", width=5).grid(column=2, row=1)
btn4 = ttk.Button(root, text="+", command=lambda:  handler("add"), style="TButton", width=5).grid(column=3, row=1)
btn5 = ttk.Button(root, text="DEL", command=lambda:  clear1(), style="TButton", width=5).grid(column=4, row=1)
btn6 = ttk.Button(root, text="AC", command=lambda:  clear(), style="TButton", width=5).grid(column=5, row=1)
btn7 = ttk.Button(root, text="4", command=lambda:  button_click(4), style="TButton", width=5).grid(column=0, row=2)
btn8 = ttk.Button(root, text="5", command=lambda:  button_click(5), style="TButton", width=5).grid(column=1, row=2)
btn9 = ttk.Button(root, text="6", command=lambda:  button_click(6), style="TButton", width=5).grid(column=2, row=2)
btn10 = ttk.Button(root, text="-", command=lambda:  handler("sub"), style="TButton", width=5).grid(column=3, row=2)
btn11 = ttk.Button(root, text="x", command=lambda:  handler("mul"), style="TButton", width=5).grid(column=4, row=2)
btn12 = ttk.Button(root, text="/", command=lambda:  handler("div"), style="TButton", width=5).grid(column=5, row=2)
btn13 = ttk.Button(root, text="1", command=lambda:  button_click(1), style="TButton", width=5).grid(column=0, row=3)
btn14 = ttk.Button(root, text="2", command=lambda:  button_click(2), style="TButton", width=5).grid(column=1, row=3)
btn15 = ttk.Button(root, text="3", command=lambda:  button_click(3), style="TButton", width=5).grid(column=2, row=3)
btn16 = ttk.Button(root, text=".", command=lambda:  button_click("."), style="TButton", width=5).grid(column=3, row=3)
btn17 = ttk.Button(root, text="x**y", command=lambda:  handler("squ"), style="TButton", width=5).grid(column=4, row=3)
btn18 = ttk.Button(root, text="2√x", command=lambda:  single("root"), style="TButton", width=5).grid(column=5, row=3)
btn19 = ttk.Button(root, text="+/-", command=lambda:  add_neg(), style="TButton", width=5).grid(column=0, row=4)
btn20 = ttk.Button(root, text="0", command=lambda:  button_click(0), style="TButton", width=5).grid(column=1, row=4)
btn21 = ttk.Button(root, text="=", command=lambda:  equal(), style="TButton", width=5).grid(column=2, row=4)
btn22 = ttk.Button(root, text="sin", command=lambda:  single("sin"), style="TButton", width=5).grid(column=3, row=4)
btn23 = ttk.Button(root, text="cos", command=lambda:  single("cos"), style="TButton", width=5).grid(column=4, row=4)
btn24 = ttk.Button(root, text="tan", command=lambda:  single("tan"), style="TButton", width=5).grid(column=5, row=4)

root.mainloop()
