from email import message
from tkinter import *
from tkinter import ttk
from math import *

szamitas = "None"

#Számolások
ures=None
s=''
#negyzet
def negyzet():
    if not s:
        keredmeny.delete(0, END)
        keredmeny.insert(0, str("Szám adat kell"))
        teredmeny.delete(0, END)
        teredmeny.insert(0, str("Szám adat kell"))
    a=float(v1.get())
    b=float(v2.get())
    
    if a==ures or b==ures:
        keredmeny.delete(0, END)
        keredmeny.insert(0, str("Szám adat kell"))
        teredmeny.delete(0, END)
        teredmeny.insert(0, str("Szám adat kell"))
    
    if a<=0 or b<=0:
            keredmeny.delete(0,END)
            keredmeny.insert(0, str("pozitív szám kell"))
    else:
        #kerület
        kerulet=2*(a+b)
        keredmeny.delete(0, END)
        keredmeny.insert(0, str(kerulet)+"cm2")
        terulet=a*b
        teredmeny.delete(0, END)
        teredmeny.insert(0, str(terulet)+"cm3")

#teglalap
def teglalap():
    if not s:
        keredmeny.delete(0, END)
        keredmeny.insert(0, str("Szám adat kell"))
        teredmeny.delete(0, END)
        teredmeny.insert(0, str("Szám adat kell"))
    a=float(v1.get())
    b=float(v2.get())
    
    if a==ures or b==ures:
        keredmeny.delete(0, END)
        keredmeny.insert(0, str("Szám adat kell"))
        teredmeny.delete(0, END)
        teredmeny.insert(0, str("Szám adat kell"))
    
    if a<=0 or b<=0:
            keredmeny.delete(0,END)
            keredmeny.insert(0, str("pozitív szám kell"))
    else:
        #kerület
        kerulet=2*(a+b)
        keredmeny.delete(0, END)
        keredmeny.insert(0, str(kerulet)+"cm2")
        terulet=a*b
        teredmeny.delete(0, END)
        teredmeny.insert(0, str(terulet)+"cm3")

#rombusz
def rombusz():
    if not s:
        keredmeny.delete(0, END)
        keredmeny.insert(0, str("Szám adat kell"))
        teredmeny.delete(0, END)
        teredmeny.insert(0, str("Szám adat kell"))
    a=float(v1.get())
    m=float(v2.get())
    
    if a==ures or m==ures:
        keredmeny.delete(0, END)
        keredmeny.insert(0, str("Szám adat kell"))
        teredmeny.delete(0, END)
        teredmeny.insert(0, str("Szám adat kell"))
    
    if a<=0 or m<=0:
            keredmeny.delete(0,END)
            keredmeny.insert(0, str("pozitív szám kell"))
    else:
        #kerület
        kerulet=4*a
        keredmeny.delete(0, END)
        keredmeny.insert(0, str(kerulet)+"cm2")
        terulet=a*b
        teredmeny.delete(0, END)
        teredmeny.insert(0, str(terulet)+"cm3")
#Számolások vége. Menügombok.

def negyzet_v():
    jelenleg.set("Alakzat: Négyzet")

#Menügombok vége. Ablak.

def nevjegy():
    abl2 = Toplevel(ablak1)
    uz2 = Message(abl2, text="Készítette:\nKecskés Zsolt és Tátrai Dominik Oszkár\n2022.04.10", width=300)
    kilep = Button(abl2, text="Exit", command=abl2.destroy)
    uz2.pack()
    kilep.pack()
    abl2.mainloop()

ablak1 = Tk()
ablak1.title("IKT Projekt - Síkidomok - 2022.04.27")
ablak1.geometry('600x400')
ablak1.maxsize(600, 400)
ablak1.minsize(600, 400)
ablak1.config(background="#eeeeee")
icon = PhotoImage(file = "ikon.png")
ablak1.iconphoto(True, icon)

ms = Frame(ablak1)
ms.grid(row=0, column=0)
v1 = Label(
    ablak1,
    text='Változó1:', 
    bg='#eeeeee'
).place(x=20, y=30)
v2 = Label(
    ablak1,
    text='Változó2:', 
    bg='#eeeeee'
).place(x=20, y=60)
v3 = Label(
    ablak1,
    text='Változó3:', 
    bg='#eeeeee'
).place(x=20, y=90)
a = ttk.Entry(ablak1)
a.place(x=80, y=30)
b = ttk.Entry(ablak1)
b.place(x=80, y=60)
c = ttk.Entry(ablak1)
c.place(x=80, y=90)
kerulet = Label(
    ablak1,
    text='Kerület:', 
    bg='#eeeeee'
).place(x=10, y=250)
terulet = Label(
    ablak1,
    text='Terület:', 
    bg='#eeeeee'
).place(x=10, y=280)
e3 = Label(
    ablak1,
    text='Eredmény3:', 
    bg='#eeeeee'
).place(x=10, y=310)

keredmeny = ttk.Entry(ablak1)
keredmeny.place(x=80, y=250)
teredmeny = ttk.Entry(ablak1)
teredmeny.place(x=80, y=280)
ec = ttk.Entry(ablak1)
ec.place(x=80, y=310)
sym = PhotoImage(file="ikon_nagy.png")
kep = ttk.Label(
    ablak1,
    image=sym
).place(x=440, y=250)
canvas = Canvas(ablak1, height = 200, width = 300, bg = "white", bd = 10).place(x=250, y=20) # Canvas
szamitas = Button(ablak1, text = "Számítás", command = ablak1.destroy, height = 1, width = 11, font = "Impact 28").place(x=17, y=125) # Gomb
# Milyen alakzatot csinálsz éppen?
jelenleg = StringVar()
jelenleg.set = (ablak1, "Alakzat: -", "jelenlegi állapot")
jelenlegl = Label(
    ablak1,
    text=jelenleg, 
    bg='#eeeeee'
).place(x=15, y=220)

Manual = Button(ablak1, text = "Olvassel megnyitása", command = ablak1.destroy, height = 2, width = 30).place(x=195, y=350) # Gomb
Button(ablak1, text = "Kilépés", command = ablak1.destroy, height = 2, width = 20).place(x=20, y=350) # Gomb

m1 = Menubutton(ms, text = "Fájl", underline = 0)
m1.pack(side = LEFT)
fm = Menu(m1)
fm.add_command(label="Névjegy",command=nevjegy, underline = 0)
fm.add_command(label="Kilépés",command=ablak1.destroy, underline = 0)
m1.config(menu = fm)
m2 = Menubutton(ms, text="Síkidomok", underline = 0)
m2.pack(side = LEFT)
tm = Menu(m2)
tm.add_command(label="Négyzet",command=negyzet_v, underline = 0)
tm.add_command(label="Téglalap",command=ablak1.destroy, underline = 0)
m2.config(menu = tm)
ablak1.mainloop()