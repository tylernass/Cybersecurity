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

NORM_FONT = ("Helvetica", 10)
buttons = ["Port Scan", "IP Address Scan", "Sniff Packets"]

def scan():
    print("1")

def ip():
    print("2")

def sniff():
    print("3")




master = Tkinter.Tk()

a = Tkinter.Button(master, text=buttons[0], command= lambda: scan())
a.pack()

b = Tkinter.Button(master, text=buttons[1], command = lambda: ip())
b.pack()

c = Tkinter.Button(master, text=buttons[2], command = lambda: sniff())
c.pack()
i=j=k=0

if(a):
    if(i >= 1):
        scan()
    else:
        i += 1

if(b):
    if (j >= 1):
        ip()
    else:
        j += 1

if(c):
    if (k >= 1):
        sniff()
    else:
        k += 1


mainloop()
e = Entry(master, width=50)

def makeentry(parent, caption, width=None, **options):
    Label(parent, text=caption).pack(side=LEFT)
    entry = Entry(parent, **options)
    if width:
        entry.config(width=width)
    entry.pack(side=LEFT)
    return entry

content = StringVar()
entry = Entry(parent, text=caption, textvariable=content)

text = content.get()
content.set(text)
