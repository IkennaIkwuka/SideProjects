#Completed
import tkinter as tk

def calculate():
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_index = 1
col_index = 0
for button in buttons:
    if button == '=':
        tk.Button(root, text=button, padx=30, pady=20, command=calculate).grid(row=row_index, column=col_index)
    else:
        tk.Button(root, text=button, padx=30, pady=20, command=lambda x=button: entry.insert(tk.END, x)).grid(row=row_index, column=col_index)
    col_index += 1
    if col_index > 3:
        col_index = 0
        row_index += 1

root.mainloop()
