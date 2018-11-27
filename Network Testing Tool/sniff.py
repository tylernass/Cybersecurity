from tkinter import *

attacks = ["Malware", "Network Attack", "Scapy"]
methods = ["Enter # of attacks to run: ", "Enter time period for attacks: "]
num = freq = 0

def init():
    def nm():
        c = Tk()

        e1 = Entry(c)
        e1.pack()
        e2 = Entry(c)
        e2.pack()

        a = e1.get()
        e1.grid(row=0, column=1)
        Label(c, text=methods[0]).grid(row=0)

        b=e2.get()
        e2.grid(row=1, column=1)
        Label(c, text = methods[1]).grid(row=1)

        Button(c, text = "Enter", command=lambda: gt()).grid(row=0, column=2)
        Button(c, text= "Enter", command=lambda: gt()).grid(row=1, column=2)
        z = Button(c, text="Return to main menu", height=1, width=18, command=lambda: init())
        z.grid(row=2, column=1)


        def gt():
            a = e1.get()

        # d = Button(c, text=methods[0], height=1, width=18, command=lambda: time())
        # d.pack(side = LEFT, row=0)
        # num = Entry(c, width = 10)
        # num.pack(side = LEFT, row=0)
        #
        # z = Button(c, text="Return to main menu", height=1, width=18, command=lambda: init())
        # z.pack(row=1)
        c.mainloop()
        a.destroy()

    a = Tk()
    for x in range(len(attacks)):
        b = Button(a, text=attacks[x], height=1, width=10, command=lambda: nm())
        b.pack()
    if(b == 0): print('Mal')
    a.mainloop()


init()

print(freq)
