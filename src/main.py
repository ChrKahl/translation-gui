import tkinter as tk

class Main(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent


        self.label = tk.Label(self, text="Welcome to Translation-GUI", anchor="c", bg="yellow")
        self.label.pack(side="top", fill="x")
