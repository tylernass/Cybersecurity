# Network tool for running: Port Scan, IP Address Scan, and Sniffing IP Packets

# 4 windows for portal to
# import Tkinter
#
# buttons = ["Port Scan", "IP Address Scan", "Sniff Packets"]
#
# win = Tkinter.Tk()
# def prnt(i):
#     print(i+1)
#
# for i in range(len(buttons)):
#     b = Tkinter.Button(win, text=buttons[i], command=prnt(i))
#     b.pack()
#
# win.mainloop()




##########################

from tkinter import *
from scapy.all import *
import Tkinter
import tkinter as tk
from tkinter import ttk
import tkMessageBox
NORM_FONT = ("Helvetica", 10)
buttons = ["Port Scan", "IP Address Scan", "Sniff Packets"]


# def snf(pkt):
#     a = sniff(count=int(pkt))
#
#     popup = tk.Tk()
#     for i in range(len(a)):
#         popup.wm_title("Network Report")
#         label = ttk.Label(popup, text=a[i].summary(), font=NORM_FONT)
#         label.pack(side="top", fill="x", pady=10)
#
#     popup.mainloop()

master = Tk()

# e = Entry(master)
# e.pack()
#
# e.focus_set()

def function(i):
    print(i)

for i in range(len(buttons)):
    b = Tkinter.Button(master, text=buttons[i], command=function(i))
    b.pack()

mainloop()
e = Entry(master, width=50)

# text = e.get()
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
