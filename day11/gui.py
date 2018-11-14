import tkinter as tk
import random

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.canvas_width = 640
        self.canvas_height = 480
        self.w = tk.Canvas(master,width=self.canvas_width,height=self.canvas_height)
        self.master = master

        self.w.pack(expand = "YES", fill = "both")
        self.w.bind("<B1-Motion>", self.draw)
        self.w.bind("<Button-3>", self.clearscreen)
    def draw(self, event):
        python_green = "#476042"
        x1, y1 = (event.x - 1), (event.y -1)
        x2, y2 = (event.x +1), (event.y + 1)
        self.w.create_oval(x1, y1, x2, y2, fill = python_green)
    def clearscreen(self, event):
        self.w.delete("all")


root = tk.Tk()
root.title("Painting thing")
app = Application(master=root)
app.mainloop()
        
