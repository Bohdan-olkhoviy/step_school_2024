from tkinter import *

def Red():
    Label1.config(text="Red")
    Entry1.delete(0,END)
    Entry1.insert(0,"#ff0000")

def Orange():
    Label1.config(text="Orange")
    Entry1.delete(0,END)
    Entry1.insert(0,"#ff7d00")

def Yellow():
    Label1.config(text="Yellow")
    Entry1.delete(0,END)
    Entry1.insert(0,"#FFFF00")

def Green():
    Label1.config(text="Green")
    Entry1.delete(0,END)
    Entry1.insert(0,"#008000")

def Cyne():
    Label1.config(text="Cyne")
    Entry1.delete(0,END)
    Entry1.insert(0,"#66ffff")

def Blue():
    Label1.config(text="Blue")
    Entry1.delete(0,END)
    Entry1.insert(0,"#0000FF")

def Purple():
    Label1.config(text="Purple")
    Entry1.delete(0,END)
    Entry1.insert(0,"#800080")

window = Tk()

window.title("Домашне завданя N4")
window.minsize(400,400)
window.resizable(False,False)

Label1 = Label(window,text="COLOR",font=('Cosmic Sans Ms',30))
Label1.pack()

Entry1 = Entry(width=30,justify="center")
Entry1.pack()

Btn1 = Button(text="Красний",width=25,bg="#ff0000",fg="white",command=Red)
Btn1.pack()

Btn1 = Button(text="Орвнжевий",width=25,bg="#ff7d00",fg="white",command=Orange)
Btn1.pack()

Btn1 = Button(text="Желтий",width=25,bg="#FFFF00",fg="white",command=Yellow)
Btn1.pack()

Btn1 = Button(text="Зелений",width=25,bg="#008000",fg="white",command=Green)
Btn1.pack()

Btn1 = Button(text="Голубой",width=25,bg="#66ffff",fg="white",command=Cyne)
Btn1.pack()

Btn1 = Button(text="Синий",width=25,bg="#0000FF",fg="white",command=Blue)
Btn1.pack()

Btn1 = Button(text="Фиолетовий",width=25,bg="#800080",fg="white",command=Purple)
Btn1.pack()

window.mainloop()
