import tkinter as tk

window = tk.Tk()
window.geometry("400x300")
label1 = tk.Label(text = "Type a character")
label1.pack()
label2 = tk.Label(text = "You have typed:")
label2.pack()
label3 = tk.Label(text = "")
label3.pack()
def handle_keypress(event):
    """Print the character associated to the key pressed"""
    label3["text"] = f"{event.char}"
    print(event.char)

# Bind keypress event to handle_keypress()
window.bind("<Key>", handle_keypress)

window.mainloop()