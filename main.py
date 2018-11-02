from tkinter import *
from scapy.all import *
import tkinter as tk
from tkinter import ttk
import tkMessageBox
NORM_FONT = ("Helvetica", 10)

def snf(pkt):
    a = sniff(count=int(pkt))

    popup = tk.Tk()
    for i in range(len(a)):
        popup.wm_title("Network Report")
        label = ttk.Label(popup, text=a[i].summary(), font=NORM_FONT)
        label.pack(side="top", fill="x", pady=10)

    popup.mainloop()

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
def makeentry(parent, caption, width=None, **options):
    Label(parent, text=caption).pack(side=LEFT)
    entry = Entry(parent, **options)
    if width:
        entry.config(width=width)
    entry.pack(side=LEFT)
    return entry

# user = makeentry(parent, "User name:", 10)
# password = makeentry(parent, "Password:", 10, show="*")
content = StringVar()
entry = Entry(parent, text=caption, textvariable=content)

text = content.get()
content.set(text)
