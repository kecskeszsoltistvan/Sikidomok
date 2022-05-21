from email import message
from tkinter import *
import math

szamitas = "None"
ures=None
s=''
a = 0
b = 0
c = 0
ma = 0
r = 0
#Számolások
#negyzet
def negyzet():
    try:
        aa=float(va.get())
    except:
        va.delete(0, END)
        va.insert(0, str("Szám adat kell"))
        keredmeny.delete(0, END)
        teredmeny.delete(0, END)
    if aa<=0:
        va.delete(0,END)
        va.insert(0, str("Pozitív szám kell"))
    else:
        #kerület
        kerulet = 2 * aa
        keredmeny.delete(0, END)
        keredmeny.insert(0, str(kerulet)+" cm")
        #terület
        terulet = aa * aa
        teredmeny.delete(0, END)
        teredmeny.insert(0, str(terulet)+" cm²")
#teglalap
def teglalap():
    try:
        aa=float(va.get())
    except:
        va.delete(0, END)
        va.insert(0, str("Szám adat kell"))
        keredmeny.delete(0, END)
        teredmeny.delete(0, END)
    try:
        bb=float(vb.get())
    except:
        vb.delete(0, END)
        vb.insert(0, str("Szám adat kell"))
        keredmeny.delete(0, END)
        teredmeny.delete(0, END)
    if aa<=0:
        va.delete(0,END)
        va.insert(0, str("Pozitív szám kell"))
    if bb<=0:
        vb.delete(0,END)
        vb.insert(0, str("Pozitív szám kell"))
    else:
        #kerület
        kerulet = 2 * (aa + bb)
        keredmeny.delete(0, END)
        keredmeny.insert(0, str(kerulet)+" cm")
        #terület
        terulet = aa * bb
        teredmeny.delete(0, END)
        teredmeny.insert(0, str(terulet)+" cm²")
#rombusz
def rombusz():
    try:
        aa=float(va.get())
    except:
        va.delete(0, END)
        va.insert(0, str("Szám adat kell"))
        keredmeny.delete(0, END)
        teredmeny.delete(0, END)
    try:
        m=float(vb.get())
    except:
        vb.delete(0, END)
        vb.insert(0, str("Szám adat kell"))
        keredmeny.delete(0, END)
        teredmeny.delete(0, END)
    
    if aa<=0:
        va.delete(0,END)
        va.insert(0, str("Pozitív szám kell"))
    if m<=0:
        vb.delete(0,END)
        vb.insert(0, str("Pozitív szám kell"))
    else:
        #kerület
        kerulet= 4 * aa
        keredmeny.delete(0, END)
        keredmeny.insert(0, str(kerulet)+" cm")
        #terulet
        terulet= aa * m
        teredmeny.delete(0, END)
        teredmeny.insert(0, str(terulet)+" cm²")
#paralelogramma
def paralelogramma():
    try:
        aa=float(va.get())
    except:
        va.delete(0, END)
        va.insert(0, str("Szám adat kell"))
        keredmeny.delete(0, END)
        teredmeny.delete(0, END)
    try:
        bb=float(vb.get())
    except:
        vb.delete(0, END)
        vb.insert(0, str("Szám adat kell"))
        keredmeny.delete(0, END)
        teredmeny.delete(0, END)
    try:
        m=float(vb.get())
    except:
        vc.delete(0, END)
        vc.insert(0, str("Szám adat kell"))
        keredmeny.delete(0, END)
        teredmeny.delete(0, END)
    if aa<=0:
        va.delete(0,END)
        va.insert(0, str("Pozitív szám kell"))
    if bb<=0:
        vb.delete(0,END)
        vb.insert(0, str("Pozitív szám kell"))
    if m<=0:
        vc.delete(0,END)
        vc.insert(0, str("Pozitív szám kell"))
    else:
        #kerület
        kerulet=2*(aa+bb)
        keredmeny.delete(0, END)
        keredmeny.insert(0, str(kerulet)+" cm")
        #terulet
        terulet=a * m
        teredmeny.delete(0, END)
        teredmeny.insert(0, str(terulet)+" cm²")
#trapéz
def trapez():
    if not s:
        keredmeny.delete(0, END)
        keredmeny.insert(0, str("Szám adat kell"))
        teredmeny.delete(0, END)
        teredmeny.insert(0, str("Szám adat kell"))
    a=float(v1.get())
    b=float(v2.get())
    c=float(v3.get())
    d=float(v4.get())
    m=float(v5.get())
    
    if a==ures or m==ures or b==ures or c==ures:
        keredmeny.delete(0, END)
        keredmeny.insert(0, str("Szám adat kell"))
        teredmeny.delete(0, END)
        teredmeny.insert(0, str("Szám adat kell"))
    
    if a<=0 or m<=0 or b<=0 or c<=0:
            keredmeny.delete(0,END)
            keredmeny.insert(0, str("pozitív szám kell"))
    else:
        #kerület
        kerulet=a+b+c+d
        keredmeny.delete(0, END)
        keredmeny.insert(0, str(kerulet)+" cm")
        #terulet
        terulet=((a+c)/2)*m
        teredmeny.delete(0, END)
        teredmeny.insert(0, str(terulet)+" cm²")
#deltoid
def deltoid():
    if not s:
        keredmeny.delete(0, END)
        keredmeny.insert(0, str("Szám adat kell"))
        teredmeny.delete(0, END)
        teredmeny.insert(0, str("Szám adat kell"))
    a=float(v1.get())
    b=float(v2.get())
    e=float(v3.get())
    f=float(v4.get())
        
    if a==ures or e==ures or b==ures or f==ures:
        keredmeny.delete(0, END)
        keredmeny.insert(0, str("Szám adat kell"))
        teredmeny.delete(0, END)
        teredmeny.insert(0, str("Szám adat kell"))
        
    if a<=0 or e<=0 or b<=0 or f==ures:
            keredmeny.delete(0,END)
            keredmeny.insert(0, str("pozitív szám kell"))
    else:
        #kerület
        kerulet=2*(a+b)
        keredmeny.delete(0, END)
        keredmeny.insert(0, str(kerulet)+" cm")
        #terulet
        terulet=(e*f)/2
        teredmeny.delete(0, END)
        teredmeny.insert(0, str(terulet)+" cm²")
#kör
def kor():
    try:
        r=float(va.get())
    except:
        va.delete(0, END)
        va.insert(0, str("Szám adat kell"))
        keredmeny.delete(0, END)
        teredmeny.delete(0, END)
    if r<=0:
        va.delete(0,END)
        va.insert(0, str("Pozitív szám kell"))
    else:
        #kerület
        kerulet=2*(r*math.pi)
        keredmeny.delete(0, END)
        keredmeny.insert(0, str(kerulet)+" cm")
        #terület
        terulet=math.pi*(r*r)
        teredmeny.delete(0, END)
        teredmeny.insert(0, str(terulet)+" cm²")
#Háromszög
def haromszog():
    if not s:
        keredmeny.delete(0, END)
        keredmeny.insert(0, str("Szám adat kell"))
        teredmeny.delete(0, END)
        teredmeny.insert(0, str("Szám adat kell"))
    a=float(v1.get())
    b=float(v2.get())
    c=float(v3.get())
    ma=float(v4.get())
    
    
    if a==ures or ma==ures or b==ures or c==ures:
        keredmeny.delete(0, END)
        keredmeny.insert(0, str("Szám adat kell"))
        teredmeny.delete(0, END)
        teredmeny.insert(0, str("Szám adat kell"))
    
    if a<=0 or b<=0 or c<=0 or ma<=0:
            keredmeny.delete(0,END)
            keredmeny.insert(0, str("pozitív szám kell"))
    else:
        #kerület
        kerulet=a+b+c
        keredmeny.delete(0, END)
        keredmeny.insert(0, str(kerulet)+" cm")
        #terület
        terulet=(ma*a)/2
        teredmeny.delete(0, END)
        teredmeny.insert(0, str(terulet)+" cm²")
# Számolások vége. Menügomb funkciók.
def negyzet_v(): # Egy ilyen funkció leírása gyorsan:
    jlg.set("Alakzat: Négyzet") # Számolás gomb alatt írja hogy mit számolunk
    val1.set("A oldal:") # Szám adat 1
    val2.set("Semmi:") # Szám adat 2, ez esetben, nem kell, ezért leállítjuk
    val3.set("Semmi:") # Szám adat 3
    val4.set("Semmi:") # Szám adat 4
    cal.configure(command=negyzet) # Számításgomb funkció átírása
    va.configure(state="normal") # Szám adat 1 engedélyezése
    vb.configure(state="disabled") # Szám adat 2 leállítása
    vc.configure(state="disabled") # Szám adat 3 leállítása
    vd.configure(state="disabled") # Szám adat 4 leállítása
def teglalap_v():
    jlg.set("Alakzat: Téglalap")
    val1.set("A oldal:")
    val2.set("B oldal:")
    val3.set("Semmi:")
    val4.set("Semmi:")
    cal.configure(command=teglalap)
    va.configure(state="normal")
    vb.configure(state="normal")
    vc.configure(state="disabled")
    vd.configure(state="disabled")
def rombusz_v():
    jlg.set("Alakzat: Rombusz")
    val1.set("A oldal:")
    val2.set("Magasság:")
    val3.set("Semmi:")
    val4.set("Semmi:")
    cal.configure(command=rombusz)
    va.configure(state="normal")
    vb.configure(state="normal")
    vc.configure(state="disabled")
    vd.configure(state="disabled")
def paralelogramma_v():
    jlg.set("Alakzat: Paralelogramma")
    val1.set("A oldal:")
    val2.set("B oldal:")
    val3.set("Magasság:")
    val4.set("Semmi:")
    cal.configure(command=paralelogramma)
    va.configure(state="normal")
    vb.configure(state="normal")
    vc.configure(state="normal")
    vd.configure(state="disabled")
def trapez_v():
    jlg.set("Alakzat: Trapéz")
    val1.set("A oldal:")
    val2.set("B oldal:")
    val3.set("C oldal:")
    val4.set("Magasság:")
    cal.configure(command=trapez)
    va.configure(state="normal")
    vb.configure(state="normal")
    vc.configure(state="normal")
    vd.configure(state="normal")
def deltoid_v():
    jlg.set("Alakzat: Deltoid")
    val1.set("A oldal:")
    val2.set("B oldal:")
    val3.set("E átló (Hosszabb):")
    val4.set("Semmi:")
    cal.configure(command=deltoid)
    va.configure(state="normal")
    vb.configure(state="normal")
    vc.configure(state="normal")
    vd.configure(state="disabled")
def kor_v():
    jlg.set("Alakzat: Kör")
    val1.set("Sugár:")
    val2.set("Semmi:")
    val3.set("Semmi:")
    val4.set("Semmi:")
    cal.configure(command=kor)
    va.configure(state="normal")
    vb.configure(state="disabled")
    vc.configure(state="disabled")
    vd.configure(state="disabled")
def haromszog_v():
    jlg.set("Alakzat: Háromszög")
    val1.set("A oldal:")
    val2.set("B oldal:")
    val3.set("C oldal:")
    val4.set("Magasság:")
    cal.configure(command=kor)
    va.configure(state="normal")
    vb.configure(state="normal")
    vc.configure(state="normal")
    vd.configure(state="disabled")
def nevjegy():
    abl2 = Toplevel(ablak1)
    uz2 = Message(abl2, text="Készítette:\nKecskés Zsolt és Tátrai Dominik Oszkár\n2022.04.10", width=300)
    kilep = Button(abl2, text="Exit", command=abl2.destroy)
    uz2.pack()
    kilep.pack()
    abl2.mainloop()
#Menügomb funkciók vége. Ablak.
ablak1 = Tk()
ablak1.title("IKT Projekt - Síkidomok - 2022.04.27")
ablak1.geometry('600x400')
ablak1.maxsize(600, 400)
ablak1.minsize(600, 400)
ablak1.config(background="#eeeeee")
icon = PhotoImage(file = "ikon.png")
ablak1.iconphoto(True, icon)
# Dinamikusan válozó szövegek
jlg = StringVar()
jlg.set("Alakzat: -")
val1 = StringVar()
val1.set("Változó1:")
val2 = StringVar()
val2.set("Változó2:")
val3 = StringVar()
val3.set("Változó3:")
val4 = StringVar()
val4.set("Változó3:")
# Maga a test
    #Változók
ms = Frame(ablak1)
ms.grid(row=0, column=0)
v1 = Label(
    ablak1,
    textvariable=val1, 
    bg='#eeeeee'
).place(x=20, y=30)
v2 = Label(
    ablak1,
    textvariable=val2, 
    bg='#eeeeee'
).place(x=20, y=50)
v3 = Label(
    ablak1,
    textvariable=val3, 
    bg='#eeeeee'
).place(x=20, y=70)
v4 = Label(
    ablak1,
    textvariable=val4, 
    bg='#eeeeee'
).place(x=20, y=90)
va = Entry(ablak1, state="disabled")
va.place(x=80, y=30)
vb = Entry(ablak1, state="disabled")
vb.place(x=80, y=50)
vc = Entry(ablak1, state="disabled")
vc.place(x=80, y=70)
vd = Entry(ablak1, state="disabled")
vd.place(x=80, y=90)
kerulet = Label(
    ablak1,
    text='Kerület:', 
    bg='#eeeeee'
).place(x=15, y=253)
terulet = Label(
    ablak1,
    text='Terület:', 
    bg='#eeeeee'
).place(x=15, y=303)
keredmeny = Entry(ablak1)
keredmeny.place(x=80, y=250, height=30)
teredmeny = Entry(ablak1)
teredmeny.place(x=80, y=300, height=30)
sym = PhotoImage(file="ikon_nagy.png")
kep = Label(
    ablak1,
    image=sym
).place(x=440, y=250)
canvas = Canvas(ablak1, height = 200, width = 300, bg = "white", bd = 10).place(x=250, y=20) # Canvas
cal = Button(ablak1, text = "Számítás", command = ablak1.destroy, height = 1, width = 11, font = "Impact 28")# Számítás gomb, ami dinamikusan változtatja a funkcióját
cal.place(x=17, y=125) 
# Milyen alakzatot csinálsz éppen?
jelenlegl = Label(
    ablak1,
    textvariable=jlg, 
    bg='#eeeeee'
).place(x=15, y=220)
# Ha ilyen kódot kell mégegyszer írnom én felmondok
# Gombok
Manual = Button(ablak1, text = "Olvassel megnyitása", command = ablak1.destroy, height = 2, width = 30).place(x=195, y=350) # Gomb
Button(ablak1, text = "Kilépés", command = ablak1.destroy, height = 2, width = 20).place(x=20, y=350) # Gomb
# Menügombok
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
tm.add_command(label="Téglalap",command=teglalap_v, underline = 0)
tm.add_command(label="Rombusz",command=rombusz_v, underline = 0)
tm.add_command(label="Paralelogramma",command=paralelogramma_v, underline = 0)
tm.add_command(label="Trapéz",command=trapez_v, underline = 0)
tm.add_command(label="Deltoid",command=deltoid_v, underline = 0)
tm.add_command(label="Kör",command=kor_v, underline = 0)
tm.add_command(label="Háromszög",command=haromszog_v, underline = 0)
m2.config(menu = tm)
ablak1.mainloop()