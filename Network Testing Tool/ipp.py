import tkinter
import sys
import tkinter as tk
from tkinter import ttk
import socket
open = []
counting_close = []
threads = []
NORM_FONT = ("Helvetica", 10)

def man():
    top = tkinter.Tk()

    IP = socket.gethostbyname(socket.gethostname())
    IPm = "IP Address is: " + str(IP)

    def hello():
       print('Great success!')
       popup = tk.Tk()
       popup.wm_title("Network Report")
       label = ttk.Label(popup, text=IPm, font =NORM_FONT)
       label.pack(side="top", fill="x", pady="10")
       label = ttk.Label(popup, text=OPm, font=NORM_FONT)
       label.pack(side="top", fill="x", pady="10")
       popup.mainloop()
       sys.exit()


    # def scan(port):
    #     s = socket.socket()
    #     result = s.connect_ex((IP, port))
    #     if result == 0:
    #         open.append(port)
    #         s.close()
    #     else:
    #         counting_close.append(port)
    #
    #
    #
    # # OPm = "Open ports are: " + str(open)
    # def button():
    #     hello(IPm)
    #     # for i in range(0, 1024):
    #     #     t=Thread(target=scan(i))
    #     #     threads.append(t)
    #     #     t.start()
    #     # OPm = "Open port are: " + str(open)
    #     # print(OPm)
    #     # hello(OPm, IPm)


    B1 = tkinter.Button(top, text = "Get IP Address", command = hello)
    B1.pack()

    top.mainloop()

if __name__ == '__main__':
    man()
