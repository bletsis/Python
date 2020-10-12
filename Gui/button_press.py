import tkinter as tk

def relief_button(row, col):
    Frame1 = tk.Frame(window, borderwidth= 50)
    Frame1.grid(row=row, column=col)
    mymessage=tk.Label (Frame1, relief='raised',anchor='center', text="test", bd=20)
    mymessage.grid(padx= 20, pady= 20)

def handle_click(event):
    label1["text"] = "Button Clicked!"

def handle_enter(event):
    label1["text"] = "Mouse Enter!"

def handle_leave(event):
    label1["text"] = "Mouse Leave!"

window = tk.Tk()
window.geometry("400x300")

label1 = tk.Label(text="")
label1.grid(row=3, column=3)
relief_button(1, 3)
button = tk.Button(text="Click me!")
button.grid(row=1, column=3)

button.bind("<Button-1>", handle_click)
button.bind("<Leave>", handle_leave)
button.bind("<Enter>", handle_enter)

window.mainloop()
