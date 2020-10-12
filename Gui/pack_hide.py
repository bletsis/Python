from tkinter import *

def hide_me(event):
    event.widget.pack_forget()

def unhide(event):
    btn.pack()

root = Tk()
root.geometry("200x100")
btn=Button(root, text="Click me to hide")
btn.bind('<Button-1>', hide_me)
btn.pack()
btn2=Button(root, text="Click to Unhide button")

btn2.bind('<Button-1>', unhide)

btn2.pack()

root.mainloop()