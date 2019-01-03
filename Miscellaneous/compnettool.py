from scapy.all import *
import Tkinter
from tkinter import *
from scapy.all import *

import snff, prt, ipp

NORM_FONT = ("Helvetica", 10)
buttons = ["Port Scan", "IP Address Scan", "Sniff Packets"]


def scn():
    prt.man()

def ip():
    ipp.man()

def sniff():
    snff.man()




master = Tkinter.Tk()

a = Tkinter.Button(master, text=buttons[0], command= lambda: scn())
a.pack()

b = Tkinter.Button(master, text=buttons[1], command = lambda: ip())
b.pack()

c = Tkinter.Button(master, text=buttons[2], command = lambda: sniff())
c.pack()
i=j=k=0

if(a):
    if(i >= 1):
        scn()
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
