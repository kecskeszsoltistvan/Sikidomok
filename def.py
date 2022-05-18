from tkinter import*
import math

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
        #terület
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
         #terület
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
        #terulet
        terulet=a*m
        teredmeny.delete(0, END)
        teredmeny.insert(0, str(terulet)+"cm3")

#paralelogramma
def paralelogramma():
    if not s:
        keredmeny.delete(0, END)
        keredmeny.insert(0, str("Szám adat kell"))
        teredmeny.delete(0, END)
        teredmeny.insert(0, str("Szám adat kell"))
    a=float(v1.get())
    b=float(v2.get())
    ma=float(v3.get())
    
    if a==ures or ma==ures or b==ures:
        keredmeny.delete(0, END)
        keredmeny.insert(0, str("Szám adat kell"))
        teredmeny.delete(0, END)
        teredmeny.insert(0, str("Szám adat kell"))
    
    if a<=0 or ma<=0 or b<=0:
            keredmeny.delete(0,END)
            keredmeny.insert(0, str("pozitív szám kell"))
    else:
        #kerület
        kerulet=2*(a+b)
        keredmeny.delete(0, END)
        keredmeny.insert(0, str(kerulet)+"cm2")
        #terulet
        terulet=a*ma
        teredmeny.delete(0, END)
        teredmeny.insert(0, str(terulet)+"cm3")

#trapéz
def trapéz():
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
        keredmeny.insert(0, str(kerulet)+"cm2")
        #terulet
        terulet=((a+c)/2)*m
        teredmeny.delete(0, END)
        teredmeny.insert(0, str(terulet)+"cm3")

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
            keredmeny.insert(0, str(kerulet)+"cm2")
            #terulet
            terulet=(e*f)/2
            teredmeny.delete(0, END)
            teredmeny.insert(0, str(terulet)+"cm3")

#kör
def kor():
    if not s:
        keredmeny.delete(0, END)
        keredmeny.insert(0, str("Szám adat kell"))
        teredmeny.delete(0, END)
        teredmeny.insert(0, str("Szám adat kell"))
    r=float(v1.get())
    
    
    if r==ures:
        keredmeny.delete(0, END)
        keredmeny.insert(0, str("Szám adat kell"))
        teredmeny.delete(0, END)
        teredmeny.insert(0, str("Szám adat kell"))
    
    if r<=0:
            keredmeny.delete(0,END)
            keredmeny.insert(0, str("pozitív szám kell"))
    else:
        #kerület
        kerulet=2*(r*math.pi)
        keredmeny.delete(0, END)
        keredmeny.insert(0, str(kerulet)+"cm2")
        #terület
        terulet=math.pi*(r*r)
        teredmeny.delete(0, END)
        teredmeny.insert(0, str(terulet)+"cm")

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
        keredmeny.insert(0, str(kerulet)+"cm2")
        #terület
        terulet=(ma*a)/2
        teredmeny.delete(0, END)
        teredmeny.insert(0, str(terulet)+"cm")

