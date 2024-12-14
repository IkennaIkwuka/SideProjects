#Incomplete

import tkinter as tk

class CustomTkinter(tk.Canvas):
    def __init__(self, master, width, height, **kwargs):
        super().__init__(master, width=width, height=height, **kwargs)
        self.configure(bg="#f0f0f0", highlightthickness=0)
        self.button_bg = "#ffffff"
        self.button_active_bg = "#e0e0e0"
        self.button_fg = "#000000"
        self.font = ("Arial", 14)

    def create_button(self, x, y, text, command=None):
        button = tk.Button(self, text=text, bg=self.button_bg, activebackground=self.button_active_bg,
                    fg=self.button_fg, font=self.font, relief="flat", command=command)
        button.place(x=x, y=y, width=50, height=50)



class CalculatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Custom Calculator")
        self.master.geometry("220x290")
        
        self.custom_tkinter = CustomTkinter(self.master, width=220, height=290)
        self.custom_tkinter.pack()

        self.entry = tk.Entry(self.master, font=("Arial", 20), bd=0, justify="right")
        self.entry.place(x=10, y=10, width=200, height=50)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ('7', 10, 70), ('8', 70, 70), ('9', 130, 70), ('/', 190, 70),
            ('4', 10, 130), ('5', 70, 130), ('6', 130, 130), ('*', 190, 130),
            ('1', 10, 190), ('2', 70, 190), ('3', 130, 190), ('-', 190, 190),
            ('0', 10, 250), ('.', 70, 250), ('=', 130, 250), ('+', 190, 250)
        ]
        for button in buttons:
            text, x, y = button
            if text == '=':
                command = self.calculate
            else:
                command = lambda t=text: self.entry.insert(tk.END, t)
            self.custom_tkinter.create_button(x, y, text, command)

    def calculate(self):
        try:
            result = eval(self.entry.get())
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        except Exception as e:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")

root = tk.Tk()
app = CalculatorApp(root)
root.mainloop()
