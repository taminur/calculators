'''
This is a calculator for Ana Gonda from @taminur.
set limit from 'TK' to 'TIL'

    1 taka equaivalent to 1 in decimal system
    1 taka      = 16 ana
    1 ana       = 20 gonda
    1 gonda     = 4 kora
    1 kora      = 3 kranti
    1 kranti    = 20 til

'''

import tkinter as tk

window = tk.Tk()
window.title("Simple Calculator")
# window.geometry("375x460")

history = tk.Listbox(window, font=("Times New Roman", 15))
history.grid(row=1,column=1, columnspan=4, sticky="nsew")

field = tk.Text(window, height=2, width=20, font=("Times New Roman", 20))
field.grid(row=2, column=1, columnspan=4, sticky="ew")

field2 = tk.Text(window, height=2, width=5, font=("Times New Roman", 20))
field2.grid(row=2, column=5, columnspan=4, sticky="ew")

ans = 0.0
# all units are reference to corresponding TIL unit
UNITS={
    "AN":4800,
    "GO": 240,
    "KO": 60,
    "KR": 20,
    "TI": 1
}


def remove_suffix(s:str) -> str:
    while True:
        if s[-1] in '+-*/\n ':
            s = s[:-1]
        else:
            return s

        
def to_decimal():
    field_text = field.get("1.0", tk.END)
    for unit in UNITS.keys():
        field_text = field_text.replace(unit, "*"+str(UNITS[unit]))
    field_text = field_text.replace("~", "+")

    # print(field_text)
    # print("-----------------------")
    field_text = remove_suffix(field_text)
    # print(field_text)
    # print("-----------------------")
    res = eval(field_text)/76800
    return res

def add_to_field(symbol):
    if symbol in '+-*/':
        if len(field.get("1.0", tk.END)) > 1:
            field.insert(tk.END, symbol)
        else:
            field.insert(tk.END, (str(ans) + symbol))
    else:
        field.insert(tk.END, symbol)

def add_units_to_field(symbol):
    field.insert(tk.END, symbol + "~")
    
    field2.delete("1.0", tk.END)
    field2.insert("1.0", to_decimal())

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
    ["AN", "GO", "KO", "KR", "TI"],
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
        elif btn in ["AN", "GO", "KO", "KR", "TI"]:
            Buttons(btn, add_units_to_field).grid(row=r+3, column=c+1)
        else:
            Buttons(btn).grid(row=r+3, column=c+1)

window.mainloop()
