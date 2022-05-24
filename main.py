from email import message
from tkinter import *
import math
'''
Hosszú történet röviden, ennek a kódnak úgy 80%-át újra írtam, mert csak így működött.
Az egész egy kódműtétként indult, de aztán elkezdtem az én részemet is csinálni, és puff, kész van (majdnem).
Néhány számítást még át kell írni, mert túl sok adatot kér, de azon kívül minden jó.  
Ja, meg az olvassel.pdf-t kell befejezni. Azt addig átadom a munkatársamnak.
A maradék úgy is meglesz.                                - Kecskés Zsolt. 2022.05.22.
'''
szamitas = "None"
ures=None
aa = 0
bb = 0
cc = 0
m = 0
r = 0
atloe = True
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
        kerulet = 4 * aa
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
    if m > aa:
        vb.delete(0, END)
        vb.insert(0, str("Túl nagy magasság"))
    elif m == aa:
        vb.delete(0, END)
        vb.insert(0, str("Az alakzat egy Négyzet"))
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
        m=float(vc.get())
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
    if m > aa:
        vc.delete(0,END)
        vc.insert(0, str("Túl nagy a magasság"))
    else:
        #kerület
        kerulet=2*(aa+bb)
        keredmeny.delete(0, END)
        keredmeny.insert(0, str(kerulet)+" cm")
        #terulet
        terulet=aa * m
        teredmeny.delete(0, END)
        teredmeny.insert(0, str(terulet)+" cm²")
#trapéz
def trapez():
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
        cc=float(vc.get())
    except:
        vc.delete(0, END)
        vc.insert(0, str("Szám adat kell"))
        keredmeny.delete(0, END)
        teredmeny.delete(0, END)
    try:
        dd=float(vd.get())
    except:
        vd.delete(0, END)
        vd.insert(0, str("Szám adat kell"))
        keredmeny.delete(0, END)
        teredmeny.delete(0, END)
    try:
        m=float(ve.get())
    except:
        ve.delete(0, END)
        ve.insert(0, str("Szám adat kell"))
        keredmeny.delete(0, END)
        teredmeny.delete(0, END)
    
    if aa<=0:
        va.delete(0,END)
        va.insert(0, str("Pozitív szám kell"))
    if bb<=0:
        vb.delete(0,END)
        vb.insert(0, str("Pozitív szám kell"))
    if cc<=0:
        vc.delete(0,END)
        vc.insert(0, str("Pozitív szám kell"))
    if dd<=0:
        vd.delete(0,END)
        vd.insert(0, str("Pozitív szám kell"))
    if m<=0:
        ve.delete(0,END)
        ve.insert(0, str("Pozitív szám kell"))
    if m > aa or m > dd:
        ve.delete(0,END)
        ve.insert(0, str("Túl nagy a magasság"))
    else:
        #kerület
        kerulet=aa+bb+cc+dd
        keredmeny.delete(0, END)
        keredmeny.insert(0, str(kerulet)+" cm")
        #terulet
        terulet=((aa+cc)/2)*m
        teredmeny.delete(0, END)
        teredmeny.insert(0, str(terulet)+" cm²")
#deltoid
def deltoid():
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
        e=float(vc.get())
    except:
        vc.delete(0, END)
        vc.insert(0, str("Szám adat kell"))
        keredmeny.delete(0, END)
        teredmeny.delete(0, END)
    try:
        f=float(vd.get())
    except:
        vd.delete(0, END)
        vd.insert(0, str("Szám adat kell"))
        keredmeny.delete(0, END)
        teredmeny.delete(0, END)
    if aa<=0:
        va.delete(0,END)
        va.insert(0, str("Pozitív szám kell"))
    if bb<=0:
        vb.delete(0,END)
        vb.insert(0, str("Pozitív szám kell"))
    if e<=0:
        vc.delete(0,END)
        vc.insert(0, str("Pozitív szám kell"))
    if e>= aa + bb:
        vc.delete(0,END)
        vc.insert(0, str("Túl nagy szám"))
    if f<=0:
        vd.delete(0,END)
        vd.insert(0, str("Pozitív szám kell"))
    if f>= aa * 2:
        vd.delete(0,END)
        vd.insert(0, str("Túl nagy szám"))
    else:
        #kerület
        kerulet=2*(aa+bb)
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
        cc=float(vc.get())
    except:
        vc.delete(0, END)
        vc.insert(0, str("Szám adat kell"))
        keredmeny.delete(0, END)
        teredmeny.delete(0, END)
    if aa<=0:
        va.delete(0,END)
        va.insert(0, str("Pozitív szám kell"))
    elif bb<=0:
        vb.delete(0,END)
        vb.insert(0, str("Pozitív szám kell"))
    elif cc<=0:
        vc.delete(0,END)
        vc.insert(0, str("Pozitív szám kell"))
    elif aa + bb <= cc or bb + cc <= aa or aa + cc <= bb:
        keredmeny.delete(0, END)
        keredmeny.insert(0, str("Lehetetlen háromszög"))
    else:
        #kerület
        kerulet= aa + bb + cc
        keredmeny.delete(0, END)
        keredmeny.insert(0, str(kerulet)+" cm")
        #Magasság számolása:
        m = (math.sqrt(aa+bb+cc) * math.sqrt(-aa+bb+cc) * math.sqrt(aa-bb+cc) * math.sqrt(aa+bb-cc)) / (2 * cc)
        vd.configure(state="normal")
        vd.delete(0, END)
        vd.insert(0, str(m)+" cm")
        vd.configure(state="disabled")
        #terület
        terulet=(m * aa) / 2
        teredmeny.delete(0, END)
        teredmeny.insert(0, str(terulet)+" cm²") # Számolások vége. Menügomb funkciók.
def negyzet_v(): # Egy ilyen funkció leírása gyorsan:
    jlg.set("Alakzat: Négyzet") # Számolás gomb alatt írja hogy mit számolunk
    val1.set("A oldal:") # Szám adat 1
    val2.set("Semmi:") # Szám adat 2, ez esetben, nem kell, ezért semmit írunk
    val3.set("Semmi:") # Szám adat 3
    val4.set("Semmi:") # Szám adat 4
    val5.set("Semmi:") # Szám adat 5
    cal.configure(command=negyzet) # Számításgomb funkció átírása
    va.configure(state="normal") # Szám adat 1 engedélyezése
    vb.configure(state="disabled") # Szám adat 2 leállítása
    vc.configure(state="disabled") # Szám adat 3 leállítása
    vd.configure(state="disabled") # Szám adat 4 leállítása
    ve.configure(state="disabled") # Szám adat 5 leállítása
    eat.configure(state="normal")
    fat.configure(state="normal")
    canvas.delete("all") # Törölje le a táblát
    forma = canvas.create_line(100, 50, 220, 50, 220, 170, 100, 170, 100, 50, width = 2) # Rajzolja fel az alakzatot
    va.bind("<1>", negyzetrajz) # Ha rányomunk az Entry-re fusson le a function
    vb.bind("<1>", negyzetr)
    vc.bind("<1>", negyzetr)
    vd.bind("<1>", negyzetr)
    ve.bind("<1>", negyzetr)
def teglalap_v():

        jlg.set("Alakzat: Téglalap")
        val1.set("A oldal:")
        val2.set("B oldal:")
        val3.set("Semmi:")
        val4.set("Semmi:")
        val5.set("Semmi:")
        cal.configure(command=teglalap)
        va.configure(state="normal")
        vb.configure(state="normal")
        vc.configure(state="disabled")
        vd.configure(state="disabled")
        ve.configure(state="disabled")
        eat.configure(state="normal")
    fat.configure(state="normal")
        canvas.delete("all") # Törölje le a táblát
        forma = canvas.create_line(120, 50, 200, 50, 200, 170, 120, 170, 120, 50, width = 2)
        va.bind("<1>", teglalaprajza)
        vb.bind("<1>", teglalaprajzb)
        vc.bind("<1>", teglalapr)
        vd.bind("<1>", teglalapr)
        ve.bind("<1>", teglalapr)
def rombusz_v():
    jlg.set("Alakzat: Rombusz")
    val1.set("A oldal:")
    val2.set("Magasság:")
    val3.set("Semmi:")
    val4.set("Semmi:")
    val5.set("Semmi:")
    cal.configure(command=rombusz)
    va.configure(state="normal")
    vb.configure(state="normal")
    vc.configure(state="disabled")
    vd.configure(state="disabled")
    ve.configure(state="disabled")
    eat.configure(state="normal")
    fat.configure(state="normal")
    canvas.delete("all")
    forma = canvas.create_line(140, 50, 280, 50, 200, 170, 60, 170, 140, 50, width = 2)
    va.bind("<1>", rombuszrajza)
    vb.bind("<1>", rombuszrajzm)
    vc.bind("<1>", rombuszr)
    vd.bind("<1>", rombuszr)
    ve.bind("<1>", rombuszr)
def paralelogramma_v():
    jlg.set("Alakzat: Paralelogramma")
    val1.set("A oldal:")
    val2.set("B oldal:")
    val3.set("Magasság:")
    val4.set("Semmi:")
    val5.set("Semmi:")
    cal.configure(command=paralelogramma)
    va.configure(state="normal")
    vb.configure(state="normal")
    vc.configure(state="normal")
    vd.configure(state="disabled")
    ve.configure(state="disabled")
    eat.configure(state="normal")
    fat.configure(state="normal")
    canvas.delete("all")
    forma = canvas.create_line(120, 50, 300, 50, 220, 170, 40, 170, 120, 50, width = 2)
    va.bind("<1>", pararajza)
    vb.bind("<1>", pararajzb)
    vc.bind("<1>", pararajzm)
    vd.bind("<1>", parar)
    ve.bind("<1>", parar)
def trapez_v():
    jlg.set("Alakzat: Trapéz")
    val1.set("A oldal:")
    val2.set("B oldal:")
    val3.set("C oldal:")
    val4.set("D oldal:")
    val5.set("Magasság:")
    cal.configure(command=trapez)
    va.configure(state="normal")
    vb.configure(state="normal")
    vc.configure(state="normal")
    vd.configure(state="disabled")
    ve.configure(state="normal")
    eat.configure(state="normal")
    fat.configure(state="normal")
    canvas.delete("all")
    forma = canvas.create_line(120, 50, 220, 50, 280, 170, 40, 170, 120, 50, width = 2)
    va.bind("<1>", traprajza)
    vb.bind("<1>", traprajzb)
    vc.bind("<1>", traprajzc)
    vd.bind("<1>", traprajzd)
    ve.bind("<1>", traprajzm)
def deltoid_v():
    jlg.set("Alakzat: Deltoid")
    val1.set("A oldal:")
    val2.set("B oldal:")
    val3.set("E átló (Hosszabb):")
    val4.set("F átló (Rövidebb):")
    val5.set("Semmi:")
    cal.configure(command=deltoid)
    va.configure(state="normal")
    vb.configure(state="normal")
    vc.configure(state="normal")
    vd.configure(state="disabled")
    ve.configure(state="disabled")
    eat.configure(state="normal")
    fat.configure(state="normal")
    canvas.delete("all")
    forma = canvas.create_line(50, 110, 220, 60, 270, 110, 220, 160, 50, 110, width = 2)
    va.bind("<1>", deltrajza)
    vb.bind("<1>", deltrajzb)
    vc.bind("<1>", deltrajze)
    vd.bind("<1>", deltrajzf)
    ve.bind("<1>", deltr)

def eatlo():
    atloe = True
    vc.configure(state="normal")
    vd.configure(state="disabled")
def fatlo():
    atloe = False
    vc.configure(state="disabled")
    vd.configure(state="normal")
def kor_v():
    try:
        eat.destroy()
        fat.destroy()
    finally:
        jlg.set("Alakzat: Kör")
        val1.set("Sugár:")
        val2.set("Semmi:")
        val3.set("Semmi:")
        val4.set("Semmi:")
        val5.set("Semmi:")
        cal.configure(command=kor)
        va.configure(state="normal")
        vb.configure(state="disabled")
        vc.configure(state="disabled")
        vd.configure(state="disabled")
        ve.configure(state="disabled")
        eat.configure(state="normal")
    fat.configure(state="normal")
        canvas.delete("all")
        forma = canvas.create_oval(100, 50, 230, 180, width = 2)
        va.bind("<1>", korrajz)
        vb.bind("<1>", korr)
        vc.bind("<1>", korr)
        vd.bind("<1>", korr)
        ve.bind("<1>", korr)
def haromszog_v():
    jlg.set("Alakzat: Háromszög")
    val1.set("A oldal:")
    val2.set("B oldal:")
    val3.set("C oldal:")
    val4.set("M(a)gasság:")
    val5.set("Semmi:")
    cal.configure(command=haromszog)
    va.configure(state="normal")
    vb.configure(state="normal")
    vc.configure(state="normal")
    vd.configure(state="disabled")
    ve.configure(state="disabled")
    eat.configure(state="normal")
    fat.configure(state="normal")
    canvas.delete("all")
    forma = canvas.create_line(50, 170, 130, 50, 270, 170, 50, 170, width = 2)
    va.bind("<1>", hrszrajza)
    vb.bind("<1>", hrszrajzb)
    vc.bind("<1>", hrszrajzc)
    vd.bind("<1>", hrszrajzm)
    ve.bind("<1>", hrszr)
def nevjegy():
    abl2 = Toplevel(ablak1)
    uz2 = Message(abl2, text="Készítette:\nKecskés Zsolt és Tátrai Dominik Oszkár\n2022.04.10", width=300)
    kilep = Button(abl2, text="Exit", command=abl2.destroy)
    uz2.pack()
    kilep.pack()
    abl2.mainloop() #Menügomb funkciók vége. Rajzolás
def negyzetr(event):
    canvas.delete("all")
    forma = canvas.create_line(100, 50, 220, 50, 220, 170, 100, 170, 100, 50, width = 2)
def teglalapr(event):
    canvas.delete("all")
    forma = canvas.create_line(120, 50, 200, 50, 200, 170, 120, 170, 120, 50, width = 2)
def rombuszr(event):
    canvas.delete("all")
    forma = canvas.create_line(140, 50, 280, 50, 200, 170, 60, 170, 140, 50, width = 2)
def parar(event):
    canvas.delete("all")
    forma = canvas.create_line(120, 50, 300, 50, 220, 170, 40, 170, 120, 50, width = 2)
def deltr(event):
    canvas.delete("all")
    canvas.create_line(50, 110, 220, 60, 270, 110, 220, 160, 50, 110, width = 2)
def korr(event):
    canvas.delete("all")
    forma = canvas.create_oval(100, 50, 230, 180, width = 2)
def hrszr(event):
    canvas.delete("all")
    forma = canvas.create_line(50, 170, 130, 50, 270, 170, 50, 170, width = 2)
def negyzetrajz(event):
    canvas.delete("all")
    forma = canvas.create_line(100, 50, 220, 50, 220, 170, 100, 170, 100, 50, width = 2)
    jeloles = canvas.create_line(100, 50, 100, 170, width = 2, fill = "red")
    iras = canvas.create_text(90, 110, text = "A", fill = "red")
def teglalaprajza(event):
    canvas.delete("all")
    forma = canvas.create_line(120, 50, 200, 50, 200, 170, 120, 170, 120, 50, width = 2)
    jeloles1 = canvas.create_line(120, 50, 120, 170, width = 2, fill = "red")
    jeloles2 = canvas.create_line(200, 50, 200, 170, width = 2, fill = "red")
    iras1 = canvas.create_text(110, 110, text = "A", fill = "red")
    iras2 = canvas.create_text(210, 110, text = "A", fill = "red")
def teglalaprajzb(event):
    canvas.delete("all")
    forma = canvas.create_line(120, 50, 200, 50, 200, 170, 120, 170, 120, 50, width = 2)
    jeloles1 = canvas.create_line(120, 170, 200, 170, width = 2, fill = "red")
    jeloles2 = canvas.create_line(120, 50, 200, 50, width = 2, fill = "red")
    iras1 = canvas.create_text(160, 40, text = "B", fill = "red")
    iras2 = canvas.create_text(160, 180, text = "B", fill = "red")
def rombuszrajza(event):
    canvas.delete("all")
    forma = canvas.create_line(140, 50, 280, 50, 200, 170, 60, 170, 140, 50, width = 2)
    jeloles = canvas.create_line(60, 170, 140, 50, width = 2, fill = "red")
    iras = canvas.create_text(90, 100, text = "A", fill = "red")
def rombuszrajzm(event):
    canvas.delete("all")
    forma = canvas.create_line(140, 50, 280, 50, 200, 170, 60, 170, 140, 50, width = 2)
    jeloles = canvas.create_line(140, 170, 140, 50, width = 2, fill = "red")
    iras = canvas.create_text(130, 130, text = "M", fill = "red")
def pararajza(event):
    canvas.delete("all")
    forma = canvas.create_line(120, 50, 300, 50, 220, 170, 40, 170, 120, 50, width = 2)
    jeloles1 = canvas.create_line(40, 170, 120, 50, width = 2, fill = "red")
    iras1 = canvas.create_text(70, 100, text = "A", fill = "red")
    jeloles2 = canvas.create_line(220, 170, 300, 50, width = 2, fill = "red")
    iras2 = canvas.create_text(270, 110, text = "A", fill = "red")
def pararajzb(event):
    canvas.delete("all")
    forma = canvas.create_line(120, 50, 300, 50, 220, 170, 40, 170, 120, 50, width = 2)
    jeloles1 = canvas.create_line(120, 50, 300, 50, width = 2, fill = "red")
    iras1 = canvas.create_text(210, 40, text = "B", fill = "red")
    jeloles2 = canvas.create_line(40, 170, 220, 170, width = 2, fill = "red")
    iras2 = canvas.create_text(130, 180, text = "B", fill = "red")
def pararajzm(event):
    canvas.delete("all")
    forma = canvas.create_line(120, 50, 300, 50, 220, 170, 40, 170, 120, 50, width = 2)
    jeloles = canvas.create_line(140, 170, 140, 50, width = 2, fill = "red")
    iras = canvas.create_text(130, 130, text = "M", fill = "red")
def traprajza(event):
    canvas.delete("all")
    canvas.create_line(120, 50, 220, 50, 280, 170, 40, 170, 120, 50, width = 2)
    jeloles = canvas.create_line(120, 50, 220, 50, width = 2, fill = "red")
    iras = canvas.create_text(170, 40, text = "A", fill = "red")
def traprajzb(event):
    canvas.delete("all")
    canvas.create_line(120, 50, 220, 50, 280, 170, 40, 170, 120, 50, width = 2)
    jeloles = canvas.create_line(280, 170, 220, 50, width = 2, fill = "red")
    iras = canvas.create_text(260, 100, text = "B", fill = "red")
def traprajzc(event):
    canvas.delete("all")
    canvas.create_line(120, 50, 220, 50, 280, 170, 40, 170, 120, 50, width = 2)
    jeloles = canvas.create_line(40, 170, 280, 170, width = 2, fill = "red")
    iras = canvas.create_text(160, 180, text = "C", fill = "red")
def traprajzd(event):
    canvas.delete("all")
    canvas.create_line(120, 50, 220, 50, 280, 170, 40, 170, 120, 50, width = 2)
    jeloles = canvas.create_line(40, 170, 120, 50, width = 2, fill = "red")
    iras = canvas.create_text(70, 100, text = "D", fill = "red")
def traprajzm(event):
    canvas.delete("all")
    canvas.create_line(120, 50, 220, 50, 280, 170, 40, 170, 120, 50, width = 2)
    jeloles = canvas.create_line(120, 170, 120, 50, width = 2, fill = "red")
    iras = canvas.create_text(110, 150, text = "M", fill = "red")
def deltrajza(event):
    canvas.delete("all")
    canvas.create_line(50, 110, 220, 60, 270, 110, 220, 160, 50, 110, width = 2)
    jeloles1 = canvas.create_line(220, 60, 270, 110, width = 2, fill = "red")
    iras1 = canvas.create_text(250, 70, text = "A", fill = "red")
    jeloles1 = canvas.create_line(270, 110, 220, 160, width = 2, fill = "red")
    iras1 = canvas.create_text(250, 150, text = "A", fill = "red")
def deltrajzb(event):
    canvas.delete("all")
    canvas.create_line(50, 110, 220, 60, 270, 110, 220, 160, 50, 110, width = 2)
    jeloles1 = canvas.create_line(50, 110, 220, 60, width = 2, fill = "red")
    iras1 = canvas.create_text(130, 70, text = "B", fill = "red")
    jeloles1 = canvas.create_line(50, 110, 220, 160, width = 2, fill = "red")
    iras1 = canvas.create_text(130, 150, text = "B", fill = "red")
def deltrajze(event):
    canvas.delete("all")
    canvas.create_line(50, 110, 220, 60, 270, 110, 220, 160, 50, 110, width = 2)
    jeloles = canvas.create_line(50, 110, 270, 110, width = 2, fill = "red")
    iras = canvas.create_text(200, 100, text = "E", fill = "red")
def deltrajzf(event):
    canvas.delete("all")
    canvas.create_line(50, 110, 220, 60, 270, 110, 220, 160, 50, 110, width = 2)
    jeloles = canvas.create_line(220, 60, 220, 160, width = 2, fill = "red")
    iras = canvas.create_text(210, 110, text = "F", fill = "red")
def korrajz(event):
    canvas.delete("all")
    forma = canvas.create_oval(100, 50, 230, 180, width = 2)
    jeloles = canvas.create_line(165, 115, 230, 115, width = 2, fill = "red")
    iras = canvas.create_text(200, 105, text = "r", fill = "red")
def hrszrajza(event):
    canvas.delete("all")
    forma = canvas.create_line(50, 170, 130, 50, 270, 170, 50, 170, width = 2)
    jeloles = canvas.create_line(50, 170, 270, 170, width = 2, fill = "red")
    iras = canvas.create_text(160, 180, text = "A", fill = "red")
def hrszrajzb(event):
    canvas.delete("all")
    forma = canvas.create_line(50, 170, 130, 50, 270, 170, 50, 170, width = 2)
    jeloles = canvas.create_line(50, 170, 130, 50, width = 2, fill = "red")
    iras = canvas.create_text(80, 100, text = "B", fill = "red")
def hrszrajzc(event):
    canvas.delete("all")
    forma = canvas.create_line(50, 170, 130, 50, 270, 170, 50, 170, width = 2)
    jeloles = canvas.create_line(270, 170, 130, 50, width = 2, fill = "red")
    iras = canvas.create_text(210, 100, text = "C", fill = "red")
def hrszrajzm(event):
    canvas.delete("all")
    forma = canvas.create_line(50, 170, 130, 50, 270, 170, 50, 170, width = 2)
    jeloles = canvas.create_line(130, 170, 130, 50, width = 2, fill = "red")
    iras = canvas.create_text(120, 150, text = "M", fill = "red") #Rajzolás vége. Főablak.
ablak1 = Tk()
ablak1.title("IKT Projekt - Síkidomok - 2022.04.27")
ablak1.geometry('600x400')
ablak1.maxsize(600, 400)
ablak1.minsize(600, 400)
ablak1.config(background="#eeeeee")
icon = PhotoImage(file = "ikon.png")
ablak1.iconphoto(True, icon)
jlg = StringVar() # Dinamikusan változó szövegek
jlg.set("Alakzat: -")
val1 = StringVar()
val1.set("Semmi:")
val2 = StringVar()
val2.set("Semmi:")
val3 = StringVar()
val3.set("Semmi:")
val4 = StringVar()
val4.set("Semmi:")
val5 = StringVar()
val5.set("Semmi:")
ms = Frame(ablak1) # Maga a test
ms.grid(row=0, column=0)
v1 = Label(  #Változók
    ablak1,
    textvariable=val1, 
    bg='#eeeeee'
).place(x=20, y=20)
v2 = Label(
    ablak1,
    textvariable=val2, 
    bg='#eeeeee'
).place(x=20, y=40)
v3 = Label(
    ablak1,
    textvariable=val3, 
    bg='#eeeeee'
).place(x=20, y=60)
v4 = Label(
    ablak1,
    textvariable=val4, 
    bg='#eeeeee'
).place(x=20, y=80)
v5 = Label(
    ablak1,
    textvariable=val5, 
    bg='#eeeeee'
).place(x=20, y=100)
va = Entry(ablak1, state="disabled")
va.place(x=80, y=20)
vb = Entry(ablak1, state="disabled")
vb.place(x=80, y=40)
vc = Entry(ablak1, state="disabled")
vc.place(x=80, y=60)
vd = Entry(ablak1, state="disabled")
vd.place(x=80, y=80)
ve = Entry(ablak1, state="disabled")
ve.place(x=80, y=100)
eat = Radiobutton(ablak1, variable = atloe, value=True, command = eatlo, background="#eeeeee", state = "disabled")
eat.place(x=205, y=60)
fat = Radiobutton(ablak1, variable = atloe, value=False, command = fatlo, background="#eeeeee", state = "disabled")
fat.place(x=205, y=80)
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
canvas = Canvas(ablak1, height = 200, width = 300, bg = "white", bd = 10) # Canvas
canvas.place(x=250, y=20)
cal = Button(ablak1, text = "Számítás", command = ablak1.destroy, height = 1, width = 11, font = "Impact 28")# Számítás gomb, ami dinamikusan változtatja a funkcióját
cal.place(x=17, y=125) 
jelenlegl = Label(
    ablak1,
    textvariable=jlg, 
    bg='#eeeeee'
).place(x=15, y=220) # Milyen alakzatot csinálsz éppen?
Manual = Button(ablak1, text = "Olvassel megnyitása", command = ablak1.destroy, height = 2, width = 30).place(x=195, y=350) # Gomb
Button(ablak1, text = "Kilépés", command = ablak1.destroy, height = 2, width = 20).place(x=20, y=350) # Gomb
m1 = Menubutton(ms, text = "Fájl", underline = 0) # Menügombok
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
# Ha ilyen kódot kell mégegyszer írnom én felmondok