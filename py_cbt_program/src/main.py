import os
import tkinter as tk
from tkinter import filedialog
from src.actions import Actions
os.makedirs("/src",exist_ok=True)
# import pandas as pd
from tkinter import messagebox


def submit_button():
    file = filedialog.asksaveasfilename(title="csv")
    ...


def login():
    ...


def l_essentials():
    user.destroy()
    l_essentials = Actions()
    l_essentials = l_essentials.l_essentials()


def s_essentials():
    user.destroy()
    s_essentials = Actions()
    s_essentials = s_essentials.s_essentials()


#! START


welcome_question = messagebox.askyesnocancel(
    title="Hello...", message="Is this your first time accessing this program?"
)

if welcome_question:
    user = tk.Tk()
    user.title("Question")
    user.geometry("240x100")
    user.eval("tk::PlaceWindow . center")  # ? To center window frame
    frame = tk.Frame(user, bg="blue", bd=10, relief=tk.SUNKEN)
    frame.pack(expand=True, fill="both")
    tk.Label(
        frame, text="Are you a Lecturer or a student?", font=("Arial", 10, "bold")
    ).pack(pady=5)
    tk.Button(frame, text="Lecturer", width=12, command=l_essentials).pack(
        side=tk.LEFT, expand=True, fill="both"
    )
    tk.Button(frame, text="Student", width=12, command=s_essentials).pack(
        side=tk.LEFT, expand=True, fill="both"
    )
    user.mainloop()
elif not welcome_question:
    user = tk.Tk()
    user.title("Question")
    user.geometry("240x100")
    user.eval("tk::PlaceWindow . center")
    frame = tk.Frame(user, bg="blue", bd=10, relief=tk.SUNKEN)
    frame.pack(expand=True, fill="both")
    tk.Label(
        frame, text="Are you a Lecturer or a student?", font=("Arial", 10, "bold")
    ).pack(pady=5)
    tk.Button(frame, text="Lecturer", width=12, command=login).pack(
        side=tk.LEFT, expand=True, fill="both"
    )
    tk.Button(frame, text="Student", width=12, command=login).pack(
        side=tk.LEFT, expand=True, fill="both"
    )
    user.mainloop()
