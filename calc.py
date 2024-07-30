'''
This is a simple calculator from @taminur.
'''

import tkinter as tk

window = tk.Tk()
window.title("Simple Calculator")
window.geometry("375x460")

history = tk.Listbox(window, font=("Times New Roman", 15))
history.grid(row=1,column=1, columnspan=4, sticky="nsew")

field = tk.Text(window, height=2, width=20, font=("Times New Roman", 20))
field.grid(row=2, column=1, columnspan=4, sticky="ew")

ans = 0.0

def add_to_field(symbol):
    field.insert(tk.END, symbol)

def add_operator_to_field(symbol):
    
    if len(field.get("1.0", tk.END)) > 1:
        add_to_field(symbol)
    else:
        add_to_field(str(ans) + symbol)

def calc(_):
    field_text = field.get("1.0",tk.END)
    global ans
    ans = eval(field_text)

    field_text = field_text.removesuffix("\n")
        
    history.insert(tk.END, field_text)
    width = 50
    
    history.insert(tk.END, "---".rjust(width))
    history.insert(tk.END, str(ans).rjust(width))
    history.see(tk.END) # to scroll the listbox to the bottom
    field.delete("1.0", tk.END)

class Buttons(tk.Button):
    def __init__(self, symbol, func=add_to_field):

        super().__init__(text=symbol, command=lambda: func(symbol))
      
button_symbos = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"]
]


# create buttons based on button symbol list
for r, row in enumerate(button_symbos):
    for c, btn in enumerate(row):
        if btn == "=":
            Buttons(btn, calc).grid(row=r+3, column=c+1)
        elif btn in ("/*-+"):
            Buttons(btn, add_operator_to_field).grid(row=r+3, column=c+1)
        else:
            Buttons(btn).grid(row=r+3, column=c+1)

window.mainloop()
