# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 10:19:07 2023

@author: Kavya
"""

from tkinter import*
from tkinter.messagebox import*
from tkinter import ttk
import tempfile
import os
import datetime
wn=Tk()
wn.geometry("1300x740")
wn.title("MINI PROJECT")
amount=0
#date and time
now=datetime.datetime.now()
a=now.strftime("%d-%m-%y")
b=now.strftime("%H:%M:%S")
#---------------title---------------
title=Label(wn,text="NK Hotel",bg="orange",fg="black",font="times 40 bold")#label for name of canteen
title.pack(fill=X)
#-----------  Generating Bill Reciept -------
def bill():
    B=e1.get()  # retrieving the text wt u hv entered in entry box in string format
    F=e2.get()
    E=e3.get()
    G=e4.get()
    M=e5.get()
    P=e6.get()
    if B==""or F==""or E==""or G=="" or M=="" or P=="" or u1.get()=="" or u2.get() == "":
        showwarning("Warning","PLEASE DON'T LEFT THE ENTRY'S BLANK")
        #messagebox showing warning not to left the entrys blank
    else:
        amount=(int(B)*55+int(F)*50+int(E)*45+int(G)*50+int(M)*60+int(P)*40)# calculating total amount
        Tot_items = int(B)+int(F)+int(E)+int(G)+int(M)+int(P)
        textarea.delete(1.0,END)  # deleting the previous inserted text entirely
        textarea.insert(END,f'\n    \t         NK Hotel ')
        textarea.insert(END,"\n")
        textarea.insert(END,f"\nDate :-  {a}	\nTime :-  {b}")
        textarea.insert(END,f"\nCustomer_Name	:-  {u1.get()}")
        textarea.insert(END,f"\nMob_No\t\t :-  {u2.get()}")
        textarea.insert(END,'\n')
        textarea.insert(END,f'\n    Items\t        No of Items\t      Price')
        textarea.insert(END,f'\n\n Biriyani\t\t {e1.get()} \t     {int(B)*55}')
        textarea.insert(END,f'\n Fried Rice\t\t {e2.get()} \t     {int(F)*50}')
        textarea.insert(END,f'\n Egg Rice\t\t {e3.get()} \t     {int(E)*45}')
        textarea.insert(END,f'\n Gobi Rice\t\t {e4.get()} \t     {int(G)*50}')
        textarea.insert(END,f'\n Meals  \t\t {e5.get()} \t     {int(M)*60}')
        textarea.insert(END,f'\n Parota  \t\t {e6.get()} \t     {int(P)*40}')
        textarea.insert(END,f'\n\n=======================================')
        textarea.insert(END,f'\n Total     \t\t {Tot_items}\t Rs{amount}')
        textarea.insert(END,f'\n=======================================')
#-------- reset  --------------
def clear():
    L=[e1,e2,e3,e4,e5,e6]
    for i in L:
        i.delete(0,"end")    # deleting the text wt u hv entered in entry boxes
    u1.delete(0,"end")       # deleting the customer name
    u2.delete(0,"end")       # deleting the phone number
    textarea.delete(1.0,END) # deleting the  previously generated bill reciept
    p.current(0)
    e1.insert(0,0)
    e2.insert(0,0)
    e3.insert(0,0)
    e4.insert(0,0)
    e5.insert(0,0)
    e6.insert(0,0)
#----------- Payment ----
def payment(self):
    B=e1.get()  # retrieving the text wt u hv entered in entry box in string format
    F=e2.get()
    E=e3.get()
    G=e4.get()
    M=e5.get()
    P=e6.get()
    amount=(int(B)*55+int(F)*50+int(E)*45+int(G)*50+int(M)*60+int(P)*40)
    msg=f'you can pay {amount} rupees through {p.get()}'
    if p.get()=="Cash":
        showinfo('Payment',msg)
    else:
        showinfo("Payment",f"You can {p.get()} {amount} rupees to these number\n\n9347858073   or\t9398354978")
#--------------print------------------
def print():
    receipt=textarea.get(1.0,END)
    filename=tempfile.mktemp(".txt")
    open(filename,"w").write(receipt)
    os.startfile(filename,"Print")
#-----------------customer details--------------------
t1=Label(wn,text="Customer Details",bg="mediumvioletred",fg="white",font="times 18 bold")
t1.place(x=90,y=270)
t2=Label(wn,text="Customer Name",font="times 16 bold")
t2.place(x=20,y=310)
u1=Entry(wn)
u1.place(x=200,y=315)
t3=Label(wn,text="Phone No",font="times 16 bold")
t3.place(x=20,y=340)
u2=Entry(wn)
u2.place(x=200,y=345)



#--------------- bill receipt area-----
f1=Frame(wn,relief=GROOVE,bd=10)  # adding frame to the Tk window
f1.place(x=900,y=340,width=400,height=350)
br=Label(f1,text="Bill Receipt",font='arial 15 bold',bg="darkorchid",bd=7,relief=GROOVE).pack(fill=X)
br2=Label(f1,text="Welcome To NK Hotel",font="arial 13 bold").pack()
scrol=Scrollbar(f1,orient=VERTICAL)

#adding Scrollbar to the frame
scrol.pack(side=RIGHT,fill=Y)
textarea=Text(f1,font='arial 12 bold',yscrollcommand=scrol.set) # adding Text area to the frame
textarea.pack(fill=BOTH)
scrol.config(command=textarea.yview)




#--------------- Menu Card-----------
l1=Label(wn,text="MENU",font="times 23 bold",bg="blue",fg="white")
l1.place(x=1080,y=70)
l2=Label(wn,text="Biriyani              Rs 55",font="times 18 bold")
l2.place(x=1000,y=130)
l3=Label(wn,text="Fried Rice          Rs 50",font="times 18 bold")
l3.place(x=1000,y=160)
l4=Label(wn,text="Egg Rice             Rs 45",font="times 18 bold")
l4.place(x=1000,y=190)
l5=Label(wn,text="Gobi Rice           Rs 50",font="times 18 bold")
l5.place(x=1000,y=220)
l6=Label(wn,text="Meals                  Rs 60",font="times 18 bold")
l6.place(x=1000,y=250)
l7=Label(wn,text="Parota                 Rs 40",font="times 18 bold")
l7.place(x=1000,y=280)



#----- selection of items----------------
l8=Label(wn,text="Select the number of items",bg="indigo",fg="white",font="times 20 bold")
l8.place(x=150,y=70)
l9=Label(wn,text="Biriyani",font="times 18 bold")
l9.place(x=20,y=120)
e1=Entry(wn)
e1.place(x=20,y=150)
e1.insert(0,0)
l10=Label(wn,text="Fried Rice",font="times 18 bold")
l10.place(x=250,y=120)
e2=Entry(wn)
e2.place(x=250,y=150)
e2.insert(0,0)
l11=Label(wn,text="Egg Rice",font="times 18 bold")
l11.place(x=20,y=200)
e3=Entry(wn)
e3.place(x=20,y=230)
e3.insert(0,0)
l12=Label(wn,text="Gobi Rice",font="times 18 bold")
l12.place(x=250,y=200)
e4=Entry(wn)
e4.place(x=250,y=230)
e4.insert(0,0)
l13=Label(wn,text="Meals",font="times 18 bold")
l13.place(x=480,y=120)
e5=Entry(wn)
e5.place(x=480,y=150)
e5.insert(0,0)
l14=Label(wn,text="Parota",font="times 18 bold")
l14.place(x=480,y=200)
e6=Entry(wn)
e6.place(x=480,y=230)
e6.insert(0,0)
#----------- Buttons-------------------
b1=Button(wn,text="Bill Receipt",width=10,bg="green",fg="white",font="times 15 bold",command=bill)
#for generating bill reciept
b1.place(x=100,y=500)
b2=Button(wn,text="Reset",width=10,bg="red",fg="white",font="times 15 bold",command=clear)
# to reset the previously entered data
b2.place(x=260,y=500)
b3=Button(wn,text="Print",width=10,bg="crimson",fg="white",font="times 15 bold",command=print)
# to print the bill receipt
b3.place(x=600,y=500)
b4=Button(wn,text="Exit",width=10,bg="dodgerblue",fg="white",font="times 15 bold",command=wn.destroy)
# to destroy the tk window
b4.place(x=750,y=500)



#-----------Combobox------------------
l=Label(wn,text="   Payment  ",font="times 21 bold",fg="white",bg="magenta")
l.place(x=420,y=500)
n=StringVar()
p=ttk.Combobox(wn,width=20,textvariable=n)
p["values"]=("Cash","Google Pay","Paytm","Phone Pay")
p.place(x=420,y=550)
p.current(0)
p.bind('<<ComboboxSelected>>',payment) #binding the event with function
wn.mainloop()
