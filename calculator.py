import tkinter as tk
from tkinter import *
import cx_Freeze
import math
from tkinter import messagebox
screen=tk.Tk()
screen.geometry('400x500')
screen.title('sci_calculator')
screen.configure(bg='yellow')
screen.maxsize(height=520,width=530)
screen.minsize(height=520,width=530)
screen.iconbitmap('cal2.png')
#############################################
def clk(number):
    global op
    op+=str(number)
    inpval.set(op)

def clear():
    global op
    op=' '
    inpval.set(op)

def equal():
    global op
    r=eval(op)
    op=str(r)
    inpval.set(op)
###################################
def btn0enter(e):
    button0.configure(bg='orange')
def btn0leave(l):
    button0.configure(bg='green')
 
def btn1enter(e):
    button1.configure(bg='orange')
def btn1leave(l):
    button1.configure(bg='green')

def btn2enter(e):
    button2.configure(bg='orange')
def btn2leave(l):
    button2.configure(bg='green')

def btn3enter(e):
    button3.configure(bg='orange')
def btn3leave(l):
    button3.configure(bg='green')

def btn4enter(e):
    button4.configure(bg='orange')
def btn4leave(l):
    button4.configure(bg='green')

def btn5enter(e):
    button5.configure(bg='orange')
def btn5leave(l):
    button5.configure(bg='green')

def btn6enter(e):
    button6.configure(bg='orange')
def btn6leave(l):
    button6.configure(bg='green')
 
def btn7enter(e):
    button7.configure(bg='orange')
def btn7leave(l):
    button7.configure(bg='green')
 
def btn8enter(e):
    button8.configure(bg='orange')
def btn8leave(l):
    button8.configure(bg='green')
 
def btn9enter(e):
    button9.configure(bg='orange')
def btn9leave(l):
    button9.configure(bg='green')

def btnaddenter(e):
    buttonadd.configure(bg='orange')
def btnaddleave(l):
    buttonadd.configure(bg='green')
 
def btnminusenter(e):
    buttonminus.configure(bg='orange')
def btnminusleave(l):
    buttonminus.configure(bg='green')
  
def btnmultienter(e):
    buttonmulti.configure(bg='orange')
def btnmultileave(l):
    buttonmulti.configure(bg='green')
 
def btndiventer(e):
    buttondiv.configure(bg='orange')
def btndivleave(l):
    buttondiv.configure(bg='green')
  
def btncenter(e):
    buttonc.configure(bg='orange')
def btncleave(l):
    buttonc.configure(bg='green')

def btnequalenter(e):
    buttonequal.configure(bg='orange')
def btnequalleave(l):
    buttonequal.configure(bg='green')

def btnsinenter(e):
    buttonsin.configure(bg='orange')
def btnsinleave(l):
    buttonsin.configure(bg='green')
       
def btncosenter(e):
    buttoncos.configure(bg='orange')
def btncosleave(l):
    buttoncos.configure(bg='green')

def btntanenter(e):
    buttontan.configure(bg='orange')
def btntanleave(l):
    buttontan.configure(bg='green')

def btnlogenter(e):
    buttonlog.configure(bg='orange')
def btnlogleave(l):
    buttonlog.configure(bg='green')

def btnsqrtenter(e):
    buttonsqrt.configure(bg='orange')
def btnsqrtleave(l):
    buttonsqrt.configure(bg='green')
###############sci fun###############
def btnsin():
    global op
    try:
        r=math.sin(eval(inpval.get()))
        op=str(r)
        inpval.set(r)
    except:
        messagebox.showinfo('Notification','invalid syntax')
def btncos():
    global op
    try:
        r=math.cos(eval(inpval.get()))
        op=str(r)
        inpval.set(r)
    except:
        messagebox.showinfo('Notification','invalid syntax')
def btntan():
    global op
    try:
        r=math.tan(eval(inpval.get()))
        op=str(r)
        inpval.set(r)
    except:
        messagebox.showinfo('Notification','invalid syntax')
def btnlog():
    global op
    try:
        r=math.log(eval(inpval.get()))
        op=str(r)
        inpval.set(r)
    except:
        messagebox.showinfo('Notification','invalid syntax')
def btnsqrt():
    global op
    try:
        r=math.sqrt(eval(inpval.get()))
        op=str(r)
        inpval.set(r)
    except:
        messagebox.showinfo('Notification','invalid syntax')
 ##################################      
inpval=StringVar()
op=''

entrybox=tk.Entry(screen,bg='red',font=('arial',25,'italic bold'),bd='25',textvar=inpval)
entrybox.grid(row=0,columnspan=4)

button7=tk.Button(screen,text='7',font=('arial',25,'italic bold'),bg='green',padx=20,pady=15,bd=10,command=lambda:clk(7),activebackground='blue')
button7.grid(row=1,column=0,sticky=tk.W)
button7.bind('<Enter>',btn7enter)
button7.bind('<Leave>',btn7leave)
button8=tk.Button(screen,text='8',font=('arial',25,'italic bold'),bg='green',padx=20,pady=15,bd=10,command=lambda:clk(8),activebackground='blue')
button8.grid(row=1,column=1,sticky=tk.W)
button8.bind('<Enter>',btn8enter)
button8.bind('<Leave>',btn8leave)
button9=tk.Button(screen,text='9',font=('arial',25,'italic bold'),bg='green',padx=20,pady=15,bd=10,command=lambda:clk(9),activebackground='blue')
button9.grid(row=1,column=2,sticky=tk.W)
button9.bind('<Enter>',btn9enter)
button9.bind('<Leave>',btn9leave)
buttonadd=tk.Button(screen,text='+',font=('arial',25,'italic bold'),bg='green',padx=20,pady=15,bd=10,command=lambda:clk('+'),activebackground='blue')
buttonadd.grid(row=1,column=3,sticky=tk.W)
buttonadd.bind('<Enter>',btnaddenter)
buttonadd.bind('<Leave>',btnaddleave)


button4=tk.Button(screen,text='4',font=('arial',25,'italic bold'),bg='green',padx=20,pady=15,bd=10,command=lambda:clk(4),activebackground='blue')
button4.grid(row=2,column=0,sticky=tk.W)
button4.bind('<Enter>',btn4enter)
button4.bind('<Leave>',btn4leave)
button5=tk.Button(screen,text='5',font=('arial',25,'italic bold'),bg='green',padx=20,pady=15,bd=10,command=lambda:clk(5),activebackground='blue')
button5.grid(row=2,column=1,sticky=tk.W)
button5.bind('<Enter>',btn5enter)
button5.bind('<Leave>',btn5leave)
button6=tk.Button(screen,text='6',font=('arial',25,'italic bold'),bg='green',padx=20,pady=15,bd=10,command=lambda:clk(6),activebackground='blue')
button6.grid(row=2,column=2,sticky=tk.W)
button6.bind('<Enter>',btn6enter)
button6.bind('<Leave>',btn6leave)
buttonminus=tk.Button(screen,text='-',font=('arial',25,'italic bold'),bg='green',padx=24,pady=15,bd=10,command=lambda:clk('-'),activebackground='blue')
buttonminus.grid(row=2,column=3,sticky=tk.W)
buttonminus.bind('<Enter>',btnminusenter)
buttonminus.bind('<Leave>',btnminusleave)

button1=tk.Button(screen,text='1',font=('arial',25,'italic bold'),bg='green',padx=20,pady=15,bd=10,command=lambda:clk(1),activebackground='blue')
button1.grid(row=3,column=0,sticky=tk.W)
button1.bind('<Enter>',btn1enter)
button1.bind('<Leave>',btn1leave)
button2=tk.Button(screen,text='2',font=('arial',25,'italic bold'),bg='green',padx=20,pady=15,bd=10,command=lambda:clk(2),activebackground='blue')
button2.grid(row=3,column=1,sticky=tk.W)
button2.bind('<Enter>',btn2enter)
button2.bind('<Leave>',btn2leave)
button3=tk.Button(screen,text='3',font=('arial',25,'italic bold'),bg='green',padx=20,pady=15,bd=10,command=lambda:clk(3),activebackground='blue')
button3.grid(row=3,column=2,sticky=tk.W)
button3.bind('<Enter>',btn3enter)
button3.bind('<Leave>',btn3leave)
buttonmulti=tk.Button(screen,text='x',font=('arial',25,'italic bold'),bg='green',padx=20,pady=15,bd=10,command=lambda:clk('*'),activebackground='blue')
buttonmulti.grid(row=3,column=3,sticky=tk.W)
buttonmulti.bind('<Enter>',btnmultienter)
buttonmulti.bind('<Leave>',btnmultileave)

button0=tk.Button(screen,text='0',font=('arial',25,'italic bold'),bg='green',padx=20,pady=15,bd=10,command=lambda:clk(0),activebackground='blue')
button0.grid(row=4,column=0,sticky=tk.W)
button0.bind('<Enter>',btn0enter)
button0.bind('<Leave>',btn0leave)
buttonc=tk.Button(screen,text='C',font=('arial',25,'italic bold'),bg='green',padx=17,pady=15,bd=10,command=clear,activebackground='blue')
buttonc.grid(row=4,column=1,sticky=tk.W)
buttonc.bind('<Enter>',btncenter)
buttonc.bind('<Leave>',btncleave)
buttonequal=tk.Button(screen,text='=',font=('arial',25,'italic bold'),bg='green',padx=20,pady=15,bd=10,command=equal,activebackground='blue')
buttonequal.grid(row=4,column=2,sticky=tk.W)
buttonequal.bind('<Enter>',btnequalenter)
buttonequal.bind('<Leave>',btnequalleave)
buttondiv=tk.Button(screen,text='%',font=('arial',25,'italic bold'),bg='green',padx=15,pady=15,bd=10,command=lambda:clk('/'),activebackground='blue')
buttondiv.grid(row=4,column=3,sticky=tk.W)
buttondiv.bind('<Enter>',btndiventer)
buttondiv.bind('<Leave>',btndivleave)
##################scientific oper####
buttonsin=tk.Button(screen,text='sin',font=('arial',25,'italic bold'),bg='green',padx=15,pady=15,bd=10,command=btnsin,activebackground='blue')
buttonsin.grid(row=0,column=4,sticky=tk.W)
buttonsin.bind('<Enter>',btnsinenter)
buttonsin.bind('<Leave>',btnsinleave)

buttoncos=tk.Button(screen,text='cos',font=('arial',25,'italic bold'),bg='green',padx=15,pady=15,bd=10,command=btncos,activebackground='blue')
buttoncos.grid(row=1,column=4,sticky=tk.W)
buttoncos.bind('<Enter>',btncosenter)
buttoncos.bind('<Leave>',btncosleave)

buttontan=tk.Button(screen,text='tan',font=('arial',25,'italic bold'),bg='green',padx=15,pady=15,bd=10,command=btntan,activebackground='blue')
buttontan.grid(row=2,column=4,sticky=tk.W)
buttontan.bind('<Enter>',btntanenter)
buttontan.bind('<Leave>',btntanleave)

buttonlog=tk.Button(screen,text='log',font=('arial',25,'italic bold'),bg='green',padx=15,pady=15,bd=10,command=btnlog,activebackground='blue')
buttonlog.grid(row=3,column=4,sticky=tk.W)
buttonlog.bind('<Enter>',btnlogenter)
buttonlog.bind('<Leave>',btnlogleave)

buttonsqrt=tk.Button(screen,text='sqrt',font=('arial',25,'italic bold'),bg='green',padx=15,pady=15,bd=10,command=btnsqrt,activebackground='blue')
buttonsqrt.grid(row=4,column=4,sticky=tk.W)
buttonsqrt.bind('<Enter>',btnsqrtenter)
buttonsqrt.bind('<Leave>',btnsqrtleave)
########################################################



screen.mainloop()