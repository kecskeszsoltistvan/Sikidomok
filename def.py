from tkinter import*
from math import*

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