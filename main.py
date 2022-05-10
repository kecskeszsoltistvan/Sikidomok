from email import message
from tkinter import *
from tkinter import ttk

def nevjegy():
    abl2 = Toplevel(ablak1)
    uz2 = Message(abl2, text="Készítette:\nKecskés Zsolt és Tátrai Dominik Oszkár\n2022.04.10", width=300)
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
v1 = Label(
    ablak1,
    text='Változó1:', 
    bg='#eeeeee'
).place(x=20, y=50)
v2 = Label(
    ablak1,
    text='Változó2:', 
    bg='#eeeeee'
).place(x=20, y=100)
v3 = Label(
    ablak1,
    text='Változó3:', 
    bg='#eeeeee'
).place(x=20, y=150)
a = ttk.Entry(ablak1)
a.place(x=80, y=50)
b = ttk.Entry(ablak1)
b.place(x=80, y=100)
c = ttk.Entry(ablak1)
c.place(x=80, y=150)
e1 = Label(
    ablak1,
    text='Eredmény1:', 
    bg='#eeeeee'
).place(x=10, y=250)
e2 = Label(
    ablak1,
    text='Eredmény2:', 
    bg='#eeeeee'
).place(x=10, y=280)
e3 = Label(
    ablak1,
    text='Eredmény3:', 
    bg='#eeeeee'
).place(x=10, y=310)
e4 = Label(
    ablak1,
    text='Eredmény4:', 
    bg='#eeeeee'
).place(x=220, y=250)
e5 = Label(
    ablak1,
    text='Eredmény5:', 
    bg='#eeeeee'
).place(x=220, y=280)
e6 = Label(
    ablak1,
    text='Eredmény6:', 
    bg='#eeeeee'
).place(x=220, y=310)
ea = ttk.Entry(ablak1)
ea.place(x=80, y=250)
eb = ttk.Entry(ablak1)
eb.place(x=80, y=280)
ec = ttk.Entry(ablak1)
ec.place(x=80, y=310)
ed = ttk.Entry(ablak1)
ed.place(x=290, y=250)
ee = ttk.Entry(ablak1)
ee.place(x=290, y=280)
ef = ttk.Entry(ablak1)
ef.place(x=290, y=310)
canvas = Canvas(ablak1, height = 200, width = 300, bg = "white", bd = 10).place(x=250, y=20) # Canvas
gomb = Button(ablak1, text = "Számítás", command = ablak1.destroy, height = 2, width = 28).place(x=20, y=200) # Gomb
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