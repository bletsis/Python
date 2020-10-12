import tkinter as tk

from tkinter import ttk

from tkinter import scrolledtext as sct

window = tk.Tk()

############################################################
#                                                          #
#                      RADIOBUTTON                         #
#                                                          #
############################################################

# def sel():
#    selection = "You selected the option " + str(var.get())
#    label.config(text = selection)
#
# var = tk.IntVar()
# R1 = ttk.Radiobutton(window, text="Option 1", variable=var, value=1,
#                   command=sel)
# R1.pack( anchor = tk.W )
#
# R2 = ttk.Radiobutton(window, text="Option 2", variable=var, value=2,
#                   command=sel)
# R2.pack( anchor = tk.W )
#
# R3 = ttk.Radiobutton(window, text="Option 3", variable=var, value=3,
#                   command=sel)
# R3.pack( anchor = tk.W)
#
# label = tk.Label(window)
# label.pack()

############################################################
#                                                          #
#                      CHECKBUTTON                         #
#                                                          #
############################################################

# def callBackFunc1():
#     if var1.get() == 1:
#         print ("Oh. I'm selected 1")
# var1 = tk.IntVar()
# chk1 = tk.Checkbutton(window, text="Selection 1", var = var1, command=callBackFunc1)
# chk1.pack()
#
# def callBackFunc2():
#     if var2.get() == 1:
#         print ("Oh. I'm selected 2")
#
# var2 = tk.IntVar()
# chk2 = tk.Checkbutton(window, text="Selection 2", var = var2, command=callBackFunc2)
# chk2.pack()
#
# def callBackFunc3():
#     if var3.get() == 1:
#         print ("Oh. I'm selected 3")
#
# var3 = tk.IntVar()
# chk3 = tk.Checkbutton(window, text="Selection 3", var = var3, command=callBackFunc3)
# chk3.pack()

############################################################
#                                                          #
#                      COMBOBOX                            #
#                                                          #
############################################################

# combo = ttk.Combobox(window)
# list=[]
# for i in range(6):
#     list.append(i)
#
# combo['values']= list
# combo.grid(column=0, row=0)
# combo["values"] += ("END",)
#
# def callback(eventObject):
#     print(combo.get())
# combo.bind("<<ComboboxSelected>>", callback)
#
# style = ttk.Style()
# style.configure("OW.TLabel", foreground="orange", background="white")
#
# l1 = ttk.Label(text="Test", style="OW.TLabel")
# l2 = ttk.Label(text="Test", style="OW.TLabel")
#
# l1.grid(column=0, row=1)
# l2.grid(column=1, row=1)

############################################################
#                                                          #
#                      SCROLLEDTEXT                        #
#                                                          #
############################################################

# scrolW=30
# scrolH=5
# scr=sct.ScrolledText(window, width=scrolW, height=scrolH, wrap=tk.WORD)
# scr.grid(column=0, columnspan=3)
# scr.insert(tk.INSERT,
# """
# This is a scrolledtext widget to make tkinter text read only.
# Hi
# Geeks !!!
# Geeks !!!
# Geeks !!!
# Geeks !!!
# Geeks !!!
# Geeks !!!
# Geeks !!!
# """)
# scr.configure(state ='disabled') #to kanei apokleistika readable

############################################################
#                                                          #
#                      SPINBOX                             #
#                                                          #
############################################################

# spin = tk.Spinbox(window, from_=0, to=100, width=5)
# spin.pack()

window.mainloop()
