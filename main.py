from tkinter import *
from tkinter import ttk

def nevjegy():
    abl2 = Toplevel(ablak1)
    uz2 = Message(abl2, text="Készítette: Kecskés Zsolt\n2022.04.10", width=300)
    kilep = Button(abl2, text="Exit", command=abl2.destroy)
    uz2.pack()
    kilep.pack()
    abl2.mainloop()

ablak1 = Tk()
ablak1.title("IKT Projekt - Síkidomok - 2022.04.27")
ablak1.geometry('600x500')
ablak1.maxsize(600, 500)
ablak1.minsize(600, 500)
ablak1.config(background="#eeeeee")


ms = Frame(ablak1)
ms.grid(row=0, column=0)
Label(
    ablak1,
    text='Változó1:', 
    bg='#eeeeee'
).grid(row=1, column=0)
Label(
    ablak1,
    text='Változó2:', 
    bg='#eeeeee'
).grid(row=2, column=0)
Label(
    ablak1,
    text='Változó3:', 
    bg='#eeeeee'
).grid(row=3, column=0)
a = ttk.Entry(ablak1)
a.grid(row=1, column=1)
b = ttk.Entry(ablak1)
b.grid(row=2, column=1)
c = ttk.Entry(ablak1)
c.grid(row=3, column=1)
canvas = Canvas(ablak1, height = 200, width = 300, bg = "white", bd = 10).grid(row=4, column=2, sticky = "e") # Canvas
gomb = Button(ablak1, text = "Számítás", command = ablak1.destroy).grid(row=4, column=1, sticky = "e") # Gomb
m1 = Menubutton(ms, text = "Fájl", underline = 0)
m1.pack(side = LEFT)
fm = Menu(m1)
fm.add_command(label="Névjegy",command=nevjegy, underline = 0)
fm.add_command(label="Kilépés",command=ablak1.destroy, underline = 0)
m1.config(menu = fm)
m2 = Menubutton(ms, text="Síkidomok", underline = 0)
m2.pack(side = LEFT)
tm = Menu(m2)
tm.add_command(label="Négyzet",command=ablak1.destroy, underline = 0)
tm.add_command(label="Téglalap",command=ablak1.destroy, underline = 0)
m2.config(menu = tm)
ablak1.mainloop()