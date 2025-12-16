import tkinter as tk

def click_button(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + value)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def clear():
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, width=20, font=('Arial', 24), borderwidth=2, relief="solid", justify='right')
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0, 4)
]

for text, row, col, *rest in buttons:
    if text == 'C':
        button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 20), command=clear)
    elif text == '=':
        button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 20), command=calculate)
    else:
        button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 20), command=lambda char=text: click_button(char))
    button.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()
