import tkinter as tk
import pandas as pd
from tkinter import filedialog


class Actions:
    def __init__(self) -> None:
        """ Constructor """
        pass

    def submit_button(self):
        self.dict = {
            "Name": [str(self.x1.get())],
            "Email": [str(self.x2.get())],
            "Staff ID": [str(self.x3.get())],
            "Department": [str(self.x4.get())],
            "Phone number": [str(self.x5.get())],
        }
        self.df = pd.DataFrame(self.dict)
        # file = filedialog 

    def l_essentials(self):
        essentials = tk.Tk()
        essentials.eval("tk::PlaceWindow . center")
        #
        self.x1 = tk.StringVar()
        self.x2 = tk.StringVar()
        self.x3 = tk.StringVar()
        self.x4 = tk.StringVar()
        self.x5 = tk.StringVar()
        #
        tk.Label(
            essentials,
            text="Provide the following information",
        ).grid(row=0, column=0, columnspan=3)
        #
        tk.Label(essentials, text="Name: ").grid(row=1, column=0)
        tk.Entry(essentials, width=20, textvariable=self.x1).grid(
            row=1, column=1)
        #
        tk.Label(essentials, text="Email: ").grid(row=2, column=0)
        tk.Entry(essentials, width=20, textvariable=self.x2).grid(
            row=2, column=1)
        #
        tk.Label(essentials, text="Staff ID: ").grid(row=3, column=0)
        tk.Entry(essentials, width=20, textvariable=self.x3).grid(
            row=3, column=1)
        #
        tk.Label(essentials, text="Department: ").grid(row=4, column=0)
        tk.Entry(essentials, width=20, textvariable=self.x4).grid(
            row=4, column=1)
        #
        tk.Label(essentials, text="Phone number: ").grid(row=5, column=0)
        tk.Entry(essentials, width=20, textvariable=self.x5).grid(
            row=5, column=1)
        #
        tk.Button(essentials, text="Submit", command=self.submit_button).grid(
            row=6, column=0, columnspan=3
        )
        essentials.mainloop()

    def s_essentials(self):
        essentials = tk.Tk()
        essentials.eval("tk::PlaceWindow . center")
        tk.Label(essentials, text="Provide the following information").grid(
            row=0, column=0, columnspan=3
        )
        #
        tk.Label(essentials, text="Name: ").grid(row=1, column=0)
        tk.Entry(essentials, width=20).grid(row=1, column=1)
        #
        tk.Label(essentials, text="Email: ").grid(row=2, column=0)
        tk.Entry(essentials, width=20).grid(row=2, column=1)
        #
        tk.Label(essentials, text="Matriculation number: ").grid(
            row=3, column=0)
        tk.Entry(essentials, width=20).grid(row=3, column=1)
        #
        tk.Label(essentials, text="Department: ").grid(row=4, column=0)
        tk.Entry(essentials, width=20).grid(row=4, column=1)
        #
        tk.Label(essentials, text="Academic level: ").grid(row=5, column=0)
        tk.Entry(essentials, width=20).grid(row=5, column=1)
        #
        tk.Label(essentials, text="Phone number: ").grid(row=6, column=0)
        tk.Entry(essentials, width=20).grid(row=6, column=1)
        #
        tk.Label(essentials, text="Gender: ").grid(row=7, column=0)
        tk.Entry(essentials, width=20).grid(row=7, column=1)

        tk.Label(essentials, text="Date of birth: ").grid(row=8, column=0)
        tk.Entry(essentials, width=20).grid(row=8, column=1)
        #
        tk.Button(essentials, text="Submit", command=self.submit_button).grid(
            row=9, column=0, columnspan=3
        )
        essentials.mainloop()
