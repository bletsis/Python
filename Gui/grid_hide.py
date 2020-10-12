from tkinter import *

def hide_me(event):
    event.widget.grid_forget()

def unhide(event):
    btn.grid(column=0, row=0)

root = Tk()
root.geometry("200x100")
btn=Button(root, text="Click me to hide")
btn.bind('<Button-1>', hide_me)
btn.grid(column=0, row=0)
btn2=Button(root, text="Click to Unhide button")

btn2.bind('<Button-1>', unhide)

btn2.grid(column=0, row=1)

root.mainloop()