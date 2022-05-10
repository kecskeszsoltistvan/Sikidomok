from tkinter import*
from math import*

ures=None
s=''
def negyzet():
    if not s:
        keredmeny.delete(0, END)
        keredmeny.insert(0, str("Szám adat kell"))
        teredmeny.delete(0, END)
        teredmeny.insert(0, str("Szám adat kell"))
    a=float(a.get())
    b=float(b.get())
    
    if a==ures or b==ures:
        keredmeny.delete(0, END)
        keredmeny.insert(0, str("Szám adat kell"))
        teredmeny.delete(0, END)
        teredmeny.insert(0, str("Szám adat kell"))
    
    if a<=0 or b<=0:
            keredmeny.delete(0,END)
            keredmeny.insert(0, str("pozitív szám kell"))
    else:
        kerulet=2*(a+b)
        keredmeny.delete(0, END)
        keredmeny.insert(0, str(kerulet)+"cm2")
        terulet=a*b
        teredmeny.delete(0, END)
        teredmeny.insert(0, str(terulet)+"cm3")

def teglalap():
    if not s:
        keredmeny.delete(0, END)
        keredmeny.insert(0, str("Szám adat kell"))
        teredmeny.delete(0, END)
        teredmeny.insert(0, str("Szám adat kell"))
    a=float(a.get())
    b=float(b.get())
    
    if a==ures or b==ures:
        keredmeny.delete(0, END)
        keredmeny.insert(0, str("Szám adat kell"))
        teredmeny.delete(0, END)
        teredmeny.insert(0, str("Szám adat kell"))
    
    if a<=0 or b<=0:
            keredmeny.delete(0,END)
            keredmeny.insert(0, str("pozitív szám kell"))
    else:
        kerulet=2*(a+b)
        keredmeny.delete(0, END)
        keredmeny.insert(0, str(kerulet)+"cm2")
        terulet=a*b
        teredmeny.delete(0, END)
        teredmeny.insert(0, str(terulet)+"cm3")