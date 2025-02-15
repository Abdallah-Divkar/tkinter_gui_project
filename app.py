import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tkinter GUI Application")
        self.geometry("400x300")
        self.resizable(True, True)