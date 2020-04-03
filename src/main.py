import tkinter as tk
import os
from tkinter import ttk, filedialog

class Main(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super(Main, self).__init__()
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.src_file = ''
        self.dst_file = ''

        self.labelFrame = ttk.LabelFrame(self, text="Open A Source File")
        self.labelFrame.grid(column=0, row=1, padx=20, pady=20)

        self.button = ttk.Button(self.labelFrame,
                                 text="Browse A File",
                                 command=self.fileDialog)
        self.button.grid(column=1, row=1)


        self.labelFrameDst = ttk.LabelFrame(self,
                                            text="Open A Destination File")
        self.labelFrameDst.grid(column=0, row=2, padx=20, pady=20)

        self.buttonDst = ttk.Button(self.labelFrameDst,
                                    text="Browse A File",
                                    command=self.fileDialogDst)
        self.buttonDst.grid(column=1, row=3)


    def fileDialog(self):
        self.filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                title="Select A File",
                filetypes=(("JSON", "*.json"), ("All Files","*.*")))
        self.src_file = self.filename
        self.label = ttk.Label(self.labelFrame, text="")
        self.label.grid(column=1, row=2)
        self.label.configure(text=self.filename)
        print(f"src: {self.src_file}")
        print(f"dst: {self.dst_file}")

    def fileDialogDst(self):
        self.filenameDst = filedialog.askopenfilename(initialdir=os.getcwd(),
                                                      title="Select A File",
                                                      filetypes=(("JSON", "*.json"),
                                                                 ("All Files", "*.*")))
        self.dst_file = self.filenameDst
        self.labelDst = ttk.Label(self.labelFrameDst, text="")
        self.labelDst.grid(column=1, row=2)
        self.labelDst.configure(text=self.filenameDst)
        print(f"src: {self.src_file}")
        print(f"dst: {self.dst_file}")
