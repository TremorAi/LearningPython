import tkinter as tk
import random

class Application(tk.Frame):
    hi_there = None
    def __init__(self, master=None):
        super().__init__(master)
        self.canvas_width = 640
        self.canvas_height = 480
        self.w = tk.Canvas(master,width=self.canvas_width,height=self.canvas_height)
        self.master = master
        self.draw()
        self.pack()
        self.w.pack()
    def draw(self):
        self.w.create_rectangle(0, 0, self.canvas_width, self.canvas_height, fill="#476042")
        for i in range(20):
            self.w.create_line(i*20, 0, i*20, self.canvas_height)
            self.w.create_line(0, i*20, self.canvas_width, i*20)

root = tk.Tk()
app = Application(master=root)
app.mainloop()
        
