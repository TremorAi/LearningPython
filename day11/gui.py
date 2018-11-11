import tkinter as tk
import random

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.choice = ["top","bottom","left","right"]
    
    def create_widgets(self):
        self.hi_there = tk.Button(self, text="hey", command=self.say_hi)
        self.hi_there.pack(side="top")
    def say_hi(self):
        self.guy_there = tk.Button(self, text="hey", command=self.say_hi)
        self.guy_there.pack(side=random.choice(self.choice))

root = tk.Tk()
app = Application(master=root)
app.mainloop()
        
