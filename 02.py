from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

class Program():
    def __init__(self,master):
        self.root = root.geometry("1280x720"), root.resizable(width=False, height=False)
        self.screen()

    def screen(self):
        # frame 0 = top-left
        # frame 1 = top-right
        # frame 2 = botton-left
        # frame 3 = botton-right

        load = Image.open("stocks/ABEV3/c0books_read.jpeg")
        render = ImageTk.PhotoImage(load)
        graph1 = Label(root, image=render)
        graph1.image = render
        graph1.place(x=25, y=25)

        load = Image.open("stocks/ABEV3/c0books_read.jpeg")
        render = ImageTk.PhotoImage(load)
        graph1 = Label(root, image=render)
        graph1.image = render
        graph1.place(x=659, y=24)

        load = Image.open("stocks/ABEV3/c0books_read.jpeg")
        render = ImageTk.PhotoImage(load)
        graph1 = Label(root, image=render)
        graph1.image = render
        graph1.place(x=28, y=412)

        load = Image.open("stocks/ABEV3/c0books_read.jpeg")
        render = ImageTk.PhotoImage(load)
        graph1 = Label(root, image=render)
        graph1.image = render
        graph1.place(x=660, y=412)

        # self.photo = PhotoImage(file="images/c0books_read.jpeg")
        # self.backlabel = Label(self.frame0, image=self.photo).place(x=-1, y=-1)




root = tk.Tk()
Program(root)
root.mainloop()