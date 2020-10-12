from PIL import ImageTk

import tkinter as tk

window = tk.Tk()
window.geometry("1000x1000")

window2 = tk.Toplevel(window)

icon = ImageTk.PhotoImage(file="katerina.png")
icon2 = ImageTk.PhotoImage(file="Costis.jpg")

lbl = tk.Label(window, image=icon)
lbl.pack()

lbl2 = tk.Label(window2, image=icon2)
lbl2.pack()


# canvas = tk.Canvas(window, width = 600, height = 900)
# canvas.pack()
# canvas.create_image(0,0, anchor=tk.NW, image=icon)


window.mainloop()
