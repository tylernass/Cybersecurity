from tkinter import *
from scapy.all import *
import tkinter as tk
from tkinter import ttk

NORM_FONT = ("Helvetica", 10)

def snf(pkt):
    a = sniff(count=int(pkt))

    popup = tk.Tk()
    scrollbar = Scrollbar(popup)
    scrollbar.pack(side=RIGHT, fill=Y)

    mylist = Listbox(popup, yscrollcommand=scrollbar.set)
    popup.wm_title("Network Report")
    for i in range(len(a)):
        label = ttk.Label(popup, text=a[i].summary(), font=NORM_FONT)
        label.pack(side="top", fill="x", pady=10)

    mylist.pack(side=LEFT, fill=BOTH)
    scrollbar.config(command=mylist.yview)
    popup.mainloop()

def man():
    master = Tk()

    e = Entry(master)
    e.pack()

    e.focus_set()

    def callback():
        pkt = e.get()
        snf(pkt)

    b = Button(master, text="How many packets would you like to send?", width=40, command=callback)
    b.pack()

    mainloop()
    e = Entry(master, width=50)
    e.pack()
    text = e.get()
