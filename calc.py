import tkinter as tk
import customtkinter as ctk

window = tk.Tk()

window.title("calc")
# screen_width, screen_height = window.winfo_screenwidth(), window.winfo_screenheight()
# window.geometry(f"{screen_width}x{screen_height}+0+0")

# buttons
# count = 0
# def add():
#     global count
#     count +=1
#     label = tk.Label(window, text=count)
#     label.pack()

# button = ctk.CTkButton(window, text="cookie", padx=50, pady=50, command=add, fg="white", bg="black").pack()

# input field
# e = tk.Entry(window, fg="white", bg="black")
# e.pack()
# e.insert(0, "placeholder")
# def click():
#     label = tk.Label(window, text=e.get())
#     label.pack()
# button = tk.Button(window, text="go", command=click)
# button.pack()

e = tk.Entry(window, width=32, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# 0 -> DEC
# 1 -> BIN
# 2 -> HEX

mode = 0


def click(num):
    global mode
    if num == "clear":
        e.delete(0, tk.END)
    elif num == "=":
        exp = e.get()
        e.delete(0, tk.END)
        if mode == 0:
            e.insert(0, eval(exp))
        elif mode == 1:
            if "*" in exp:
                a, b = exp.split("*")
                fin = bin(int(a, 2) * int(b, 2))
                e.insert(0, fin[2:])
            elif "+" in exp:
                a, b = exp.split("+")
                fin = bin(int(a, 2) + int(b, 2))
                e.insert(0, fin[2:])
            elif "-" in exp:
                a, b = exp.split("-")
                fin = bin(int(a, 2) - int(b, 2))
                e.insert(0, fin[2:])
            elif "-" in exp:
                a, b = exp.split("-")
                fin = bin(int(a, 2) - int(b, 2))
                e.insert(0, fin[2:])
        elif mode == 2:
            if "*" in exp:
                a, b = exp.split("*")
                fin = hex(int(a, 16) * int(b, 16))
                e.insert(0, fin[2:])
            elif "+" in exp:
                a, b = exp.split("+")
                fin = hex(int(a, 16) + int(b, 16))
                e.insert(0, fin[2:])
            elif "-" in exp:
                a, b = exp.split("-")
                fin = hex(int(a, 16) - int(b, 16))
                e.insert(0, fin[2:])
            elif "-" in exp:
                a, b = exp.split("-")
                fin = hex(int(a, 16) - int(b, 16))
                e.insert(0, fin[2:])
            
    else:
        string = e.get()
        e.delete(0, tk.END)
        e.insert(0, string + str(num))

def change(modalIndex):
    global mode
    prev = mode
    mode = modalIndex


    if mode == 0:
        if prev == 1:
            binNum = e.get()[::-1]
            count = 0
            for i in range(len(binNum)):
                count += int(binNum[i]) * (2 ** i)
            e.delete(0, tk.END)
            e.insert(0, count)
        elif prev == 2:
            hexNum = e.get()

            e.delete(0, tk.END)
            e.insert(0, int(hexNum, 16))

        enableKeys = buttons[:10]
        for i in enableKeys:
            i.config(state="active")
        disableKeys = buttons[10:]
        for i in disableKeys:
            i.config(state="disabled")
    
    elif mode == 1:
        if prev == 0:
            decNum = e.get()
            e.delete(0, tk.END)
            e.insert(0, bin(int(decNum))[2:])
        elif prev == 2:
            hexNum = e.get()
            e.delete(0, tk.END)
            hexNum = int(hexNum, 16)
            e.insert(0, bin(hexNum)[2:].upper())
        enableKeys = buttons[:2]
        for i in enableKeys:
            i.config(state="active")
        disableKeys = buttons[2:]
        for i in disableKeys:
            i.config(state="disabled")
    
    elif mode == 2:
        if prev == 0:
            decNum = e.get()
            e.delete(0, tk.END)
            e.insert(0, hex(int(decNum))[2:].upper())
        elif prev == 1:
            binNum = e.get()
            e.delete(0, tk.END)
            binNum = int(binNum, 2)
            e.insert(0, hex(binNum)[2:].upper())
        for i in buttons:
            i.config(state="active")

    ops[prev].config(state="active")
    ops[modalIndex].config(state="disabled")
    

buttons = [tk.Button(master=window, text="0", padx=40, pady=20, command=lambda: click(0)), 
tk.Button(master=window, text=1, padx=40, pady=20, command=lambda: click(1)), 
tk.Button(master=window, text=2, padx=40, pady=20, command=lambda: click(2)), 
tk.Button(master=window, text=3, padx=40, pady=20, command=lambda: click(3)),
tk.Button(master=window, text=4, padx=40, pady=20, command=lambda: click(4)),
tk.Button(master=window, text=5, padx=40, pady=20, command=lambda: click(5)),
tk.Button(master=window, text=6, padx=40, pady=20, command=lambda: click(6)),
tk.Button(master=window, text=7, padx=40, pady=20, command=lambda: click(7)),
tk.Button(master=window, text=8, padx=40, pady=20, command=lambda: click(8)),
tk.Button(master=window, text=9, padx=40, pady=20, command=lambda: click(9)),
tk.Button(master=window, text="A", padx=40, pady=20, command=lambda: click("A")),
tk.Button(master=window, text="B", padx=40, pady=20, command=lambda: click("B")),
tk.Button(master=window, text="C", padx=39, pady=20, command=lambda: click("C")),
tk.Button(master=window, text="D", padx=39, pady=20, command=lambda: click("D")),
tk.Button(master=window, text="E", padx=40, pady=20, command=lambda: click("E")),
tk.Button(master=window, text="F", padx=42, pady=20, command=lambda: click("F"))]




DEC = tk.Button(master=window, text="DEC", padx=30, pady=49, command=lambda: change(0))
BIN = tk.Button(master=window, text="BIN", padx=34, pady=52, command=lambda: change(1))
HEX = tk.Button(master=window, text="HEX", padx=30, pady=52, command=lambda: change(2))

ops = [DEC, BIN, HEX]

buttonClear = tk.Button(master=window, text="AC", padx=34, pady=20, command=lambda: click("clear"))
buttonDivide = tk.Button(master=window, text="/", padx=42, pady=20, command=lambda: click("/"))
buttonMult = tk.Button(master=window, text="*", padx=42, pady=20, command=lambda: click("*"))
buttonSubtract = tk.Button(master=window, text="-", padx=42, pady=20, command=lambda: click("-"))
buttonAdd = tk.Button(master=window, text="+", padx=38, pady=52, command=lambda: click("+"))
buttonEquals = tk.Button(master=window, text="=", padx=38, pady=52, command=lambda: click("="))
buttonDot = tk.Button(master=window, text=".", padx=43, pady=20, command=lambda: click("."))

for i in range(3):
    cur = buttons[7:]
    cur[i].grid(row=2, column=i)

for i in range(3):
    cur = buttons[4:7]
    cur[i].grid(row=3, column=i)

for i in range(3):
    cur = buttons[1:5]
    cur[i].grid(row=4, column=i)

for i in range(5):
    cur = buttons[11:]
    cur[i].grid(row=6, column=i)

buttons[0].grid(row=5, column=1)
buttons[10].grid(row=5, column=0)
buttonClear.grid(row=1, column=0)
buttonDivide.grid(row=1, column=1)
buttonSubtract.grid(row=1, column=2)
buttonMult.grid(row=1, column=3)
buttonAdd.grid(row=2, column=3, rowspan=2)
buttonEquals.grid(row=4, column=3, rowspan=2)
buttonDot.grid(row=5, column=2)

DEC.grid(row=0, column=4, rowspan=2)
BIN.grid(row=2, column=4, rowspan=2)
HEX.grid(row=4, column=4, rowspan=2)


window.mainloop()