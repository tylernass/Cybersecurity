from threading import Thread
import tkinter
import sys
import tkinter as tk
from tkinter import ttk
import socket
open = []
counting_close = []
threads = []
NORM_FONT = ("Helvetica", 10)

# def function():
#     def hello(OPm, IPm):
#        print('Great success!')
#        popup = tk.Tk()
#        popup.wm_title("Network Report")
#        label = ttk.Label(popup, text=IPm, font =NORM_FONT)
#        label.pack(side="top", fill="x", pady="10")
#        label = ttk.Label(popup, text=OPm, font=NORM_FONT)
#        label.pack(side="top", fill="x", pady="10")
#        popup.mainloop()
#        sys.exit()
#
#
#     def scan(port):
#         s = socket.socket()
#         result = s.connect_ex((host, port))
#         if result == 0:
#             open.append(port)
#             s.close()
#         else:
#             counting_close.append(port)
#             s.close()
#
#
#     for i in range(0, 4096):
#         t=Thread(target=scan(i))
#         threads.append(t)
#         t.start()


def man():
    top = tkinter.Tk()
    print(open)
    host = socket.gethostbyname(socket.gethostname())
    OPm = "Open ports are: " + str(open)
    # remoteServerIP = socket.gethostbyname(IP)

    def function():
        def hello(OPm, IPm):
            print('Great success!')
            popup = tk.Tk()
            popup.wm_title("Network Report")
            label = ttk.Label(popup, text=IPm, font=NORM_FONT)
            label.pack(side="top", fill="x", pady="10")
            label = ttk.Label(popup, text=OPm, font=NORM_FONT)
            label.pack(side="top", fill="x", pady="10")
            popup.mainloop()
            sys.exit()

        def scan(port):
            s = socket.socket()
            result = s.connect_ex((host, port))
            if result == 0:
                open.append(port)
                s.close()
            else:
                counting_close.append(port)
                s.close()

        print(str(open))
        for i in range(0, 4096):
            t = Thread(target=scan(i))
            threads.append(t)
            t.start()

    B1 = tkinter.Button(top, text="Run Port Scan", command=function)
    B1.pack()

if __name__ == '__main__':
    man()
