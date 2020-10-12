import tkinter as tk
from tkinter import Frame

def relief_button(row, col):
    Frame1 = tk.Frame(window, borderwidth= 50)
    Frame1.grid(row=row, column=col)
    mymessage=tk.Label (Frame1, relief='raised',anchor='center', text="test", bd=20)
    mymessage.grid(padx= 20, pady= 20)

window = tk.Tk()
window.title("GUI    TEST")
window.geometry("1000x600")

l1 = tk.Label(
    window,
    text="Hello World!",
    font=("Arial Bold", 14),
    bg="yellow",
    fg="#FF0000",
    width=20,
    height=2
)
l1.grid(row=0, column=0)

def clicked():
    l1.configure(text="Button was clicked !!")

relief_button(1, 0)
btn1 = tk.Button(window, text ="Click", command=clicked)
btn1.grid(row=1, column=0)

def undo():
    l1.configure(text="Hello again !!")

relief_button(1, 1)
btn2 = tk.Button(window, text ="Undo", command=undo)
btn2.grid(row=1, column=1)

def text():
    message = "Hi " + txt.get()
    l1.configure(text=message)

txt = tk.Entry(window, width=10)
txt.grid(row=3, column=0)

l2 = tk.Label(
    window,
    text="Give a Name",
    font=("Arial Bold", 14),
    bg="yellow",
    fg="#FF0000",
    width=20,
    height=1
)
l2.grid(row=2, column=0)

relief_button(3, 1)
btn3 = tk.Button(window, text ="text", command=text)
btn3.grid(row=3, column=1)

window.mainloop()