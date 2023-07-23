#Packages
from tkinter import *
from tkinter import messagebox
from datetime import datetime
import os


#///MAINWINDOW///
root=Tk()
root.title("Calculator")
root.resizable(0,0)
root.iconbitmap("Calculator.ico")
root.config(bg="azure3")


#///VARIABLES///
w=7  #Weight Buttoms
h=3  #Heigh Buttoms
opctheme = IntVar() #ThemeVar
opctheme.set(0)  #DefaultTheme(White)
opcsize = IntVar() #SizeVar
opcsize.set(0)  #DefaulSize
character = ""  #ButtonPressed
total = ""  #SetOfButtonsPressed
equation = StringVar()  #WhatAppearsInTheScreen


#///FUNCTIONS///
def About():
    messagebox.showinfo("About","☛ Armand Sans López\n☛ Summer 2023\n☛ First GUI practice")

def Exit():
    root.destroy()

def Appearance():
    appareance = Toplevel(root)
    appareance.resizable(0,0)
    appareance.grab_set()
    appareance.title("Skin")
    appareance.iconbitmap("Appareance.ico")

    lf1 = LabelFrame(appareance, text="Theme")      #ThemeOptions
    lf1.grid(row=0,column=0, padx=5, pady=5)
    Radiobutton(lf1, text="White", variable=opctheme, value=0, command=Theme).grid(row=1,column=0,sticky="W")
    Radiobutton(lf1, text="Black", variable=opctheme, value=1, command=Theme).grid(row=2,column=0,sticky="W")
    Radiobutton(lf1, text="Orange", variable=opctheme, value=2, command=Theme).grid(row=1, column=1,sticky="w")
    Radiobutton(lf1, text="Blue", variable=opctheme, value=3, command=Theme).grid(row=2, column=1,sticky="w")

    lf2 = LabelFrame(appareance, text="Size")       #SizeOptions
    lf2.grid(row=0, column=1, padx=5, pady=5)
    Radiobutton(lf2, text="Normal", variable=opcsize, value=0, command=Size).grid(row=1,column=0,sticky="W")
    Radiobutton(lf2, text="Oversized", variable=opcsize, value=1, command=Size).grid(row=2,column=0,sticky="W")

def Theme():
    skinfile = open(os.path.join(os.getcwd(), "skin.txt"), "r+")
    skinfile.seek(0)
    skinfile.write(str(opctheme.get()))
    skinfile.close()

    if opctheme.get() == 0:   #WhiteTheme
        root.config(bg="azure3")
        Screen.config(fg="Black",highlightbackground="azure3",highlightcolor="azure3")
        Equal.config(bg="#FF0000",fg="Black")
        buttoms1 = [Num7, Num8, Num9, Num4, Num5, Num6, Num1, Num2, Num3, Num0, Dot]
        for i in buttoms1:
            i.config(bg="#F0F0F0", fg="black")
        buttoms2 = [Mult,Min,Plus,Div]
        for i in buttoms2:
            i.config(bg="#B4B4B4", fg="black")

    if opctheme.get() == 1:  #BlackTheme
        root.config(bg="#282828")
        Screen.config(fg="Black",highlightbackground="#282828",highlightcolor="#282828")
        Equal.config(bg="#930000",fg="White")
        buttoms1 = [Num7, Num8, Num9, Num4, Num5, Num6, Num1, Num2, Num3, Num0, Dot]
        for i in buttoms1:
            i.config(bg="#3C3C3C", fg="White")
        buttoms2 = [Mult, Min, Plus, Div]
        for i in buttoms2:
            i.config(bg="#101010", fg="White")

    if opctheme.get() == 2:  #OrangeTheme
        root.config(bg="#E89700")
        Screen.config(fg="black",highlightbackground="#E89700",highlightcolor="#E89700")
        Equal.config(bg="#C16810",fg="White")
        buttoms1 = [Num7, Num8, Num9, Num4, Num5, Num6, Num1, Num2, Num3, Num0, Dot]
        for i in buttoms1:
            i.config(bg="#FFB121", fg="White")
        buttoms2 = [Mult, Min, Plus, Div]
        for i in buttoms2:
            i.config(bg="#DB9105", fg="White")

    if opctheme.get() == 3:  #BlueTheme
        root.config(bg="#0323C2")
        Screen.config(fg="black",highlightbackground="#0323C2",highlightcolor="#0323C2")
        Equal.config(bg="#0000A6",fg="White")
        buttoms1 = [Num7, Num8, Num9, Num4, Num5, Num6, Num1, Num2, Num3, Num0, Dot]
        for i in buttoms1:
            i.config(bg="#1CA9FF", fg="White")
        buttoms2 = [Mult, Min, Plus, Div]
        for i in buttoms2:
            i.config(bg="#0065DE", fg="White")

def Size():
    skinfile = open(os.path.join(os.getcwd(), "skin.txt"), "r+")
    skinfile.seek(1)
    skinfile.write(str(opcsize.get()))
    skinfile.close()

    if opcsize.get() == 0:
        Screen.config(font=("Arial 24"))
        Screen.grid(pady=0)
        buttoms1 = [Num7, Num8, Num9, Num4, Num5, Num6, Num1, Num2, Num3, Num0, Dot, Mult, Min, Plus, Div, Equal]
        for i in buttoms1:
            i.config(font=("Arial 9"))

    if opcsize.get() == 1:
        Screen.config(font=("Arial 45"))
        Screen.grid(pady=4)
        buttoms1 = [Num7, Num8, Num9, Num4, Num5, Num6, Num1, Num2, Num3, Num0, Dot, Mult, Min, Plus, Div, Equal]
        for i in buttoms1:
            i.config(font=("Arial 18"))



def Logs():
    userlogs = Toplevel(root)
    userlogs.title("Logs")
    userlogs.iconbitmap("Calculator.ico")
    userlogs.grab_set()

    logstext=Text(userlogs,width=28,height=14)
    logstext.grid(row=0,column=0,padx=(10,0),pady=10)
    logstext.config(font="arial 9")

    def cleanlogs():
        logfile = open(os.path.join(os.getcwd(), "logs.txt"), "w")
        logfile.close()
        logstext.config(state="normal")
        logstext.delete(1.0,END)
        logstext.config(state="disable")

    Button(userlogs,text="Clean",width=10,command=cleanlogs).grid(row=1,padx=10,pady=(0,10),sticky="w")

    scroll1 = Scrollbar(userlogs, command=logstext.yview)
    scroll1.grid(row=0,column=1,padx=(0,0),pady=10,sticky="nsew")

    logstext.config(yscrollcommand=scroll1.set)
    try:
        logfile = open(os.path.join(os.getcwd(), "logs.txt"), "r")
        lines = logfile.readlines()
        for i in lines:
            logstext.insert(INSERT, i)
    except:
        logfile = open(os.path.join(os.getcwd(), "logs.txt"), "w")
    finally:
        logstext.config(state="disabled")
        logfile.close()
        userlogs.resizable(0,0)


def calculate(character):
    global total
    time = datetime.now()
    time = time.strftime("%d/%m/%Y %H:%M:%S")  # UsedInLogs
    if character == "=":
        try:
            if total == "":
                equation.set("EMPTY")
            else:
                answer = eval(total)
                answer = round(answer,2)
                equation.set(answer)

                logfile = open(os.path.join(os.getcwd(), "logs.txt"), "a")   #LogCreation
                log = time,"\n","-> "+str(total)+"="+str(answer)+"\n"+"\n"
                logfile.writelines(log)
                logfile.close()

                total = ""
        except:
            equation.set("ERROR")
            total = ""
    else:
        total = total + str(character)      #AcumulateTheCharactersOfTheOperation
        if len(total) > 12:                 #MaxLengthError
           equation.set("MaxLength")
           total = ""
        else:
            equation.set(total)             #PrintTheProgress

#///MENU///
topmenu=Menu(root)
root.config(menu=topmenu)
Options = Menu(topmenu,tearoff=0)
Info = Menu(topmenu,tearoff=0)

topmenu.add_cascade(label="Options",menu=Options)
topmenu.add_cascade(label="Info",menu=Info)

Options.add_command(label="Appearance",command=Appearance)
Options.add_command(label="View logs",command=Logs)
Options.add_separator()
Options.add_command(label="Exit",command=Exit)
Info.add_command(label="About",command=About)


#///CALCULATOR SCREEN///
Screen=Entry(root,width=12,font=('Arial 24'),textvariable=equation)
Screen.grid(row=0,columnspan=4)
Screen.config(justify="right",highlightthickness=5,highlightbackground="azure3",highlightcolor="azure3", state="readonly")


#///CALCULATOR BUTTOMS///
Num7=Button(root,text="7",width=w,height=h,command=lambda: calculate(7))
Num7.grid(row=1,column=0)
Num8=Button(root,text="8",width=w,height=h,command=lambda: calculate(8))
Num8.grid(row=1,column=1)
Num9=Button(root,text="9",width=w,height=h,command=lambda: calculate(9))
Num9.grid(row=1,column=2)
Div=Button(root,text="/",width=w,height=h,bg="#C6C6C6",command=lambda: calculate("/"))
Div.grid(row=1,column=3)


Num4=Button(root,text="4",width=w,height=h,command=lambda: calculate(4))
Num4.grid(row=2,column=0)
Num5=Button(root,text="5",width=w,height=h,command=lambda: calculate(5))
Num5.grid(row=2,column=1)
Num6=Button(root,text="6",width=w,height=h,command=lambda: calculate(6))
Num6.grid(row=2,column=2)
Mult=Button(root,text="X",width=w,height=h,bg="#C6C6C6",command=lambda: calculate("*"))
Mult.grid(row=2,column=3)


Num1=Button(root,text="1",width=w,height=h,command=lambda: calculate(1))
Num1.grid(row=3,column=0)
Num2=Button(root,text="2",width=w,height=h,command=lambda: calculate(2))
Num2.grid(row=3,column=1)
Num3=Button(root,text="3",width=w,height=h,command=lambda: calculate(3))
Num3.grid(row=3,column=2)
Min=Button(root,text="-",width=w,height=h,bg="#C6C6C6",command=lambda: calculate("-"))
Min.grid(row=3,column=3)


Num0=Button(root,text="0",width=w,height=h,command=lambda: calculate("0"))
Num0.grid(row=4,column=0)
Dot=Button(root,text=".",width=w,height=h,command=lambda: calculate("."))
Dot.grid(row=4,column=1)
Equal=Button(root,text="=",width=w,height=h,bg="#FF0000",command=lambda: calculate("="))
Equal.grid(row=4,column=2)
Plus=Button(root,text="+",width=w,height=h,bg="#C6C6C6",command=lambda: calculate("+"))
Plus.grid(row=4,column=3)

#///SKINLOADER///
try:
    skinfile = open(os.path.join(os.getcwd(), "skin.txt"), "r")
    config = skinfile.read()
    if config[0] == "0":
        opctheme.set(0)
    elif config[0] == "1":
        opctheme.set(1)
    elif config[0] == "2":
        opctheme.set(2)
    else:
        opctheme.set(3)
    if config[1] == "0":
        opcsize.set(0)
    else:
        opcsize.set(1)
    Theme()
    Size()
    skinfile.close()
except:
    skinfile = open(os.path.join(os.getcwd(), "skin.txt"), "w")
    skinfile.write("00")
    skinfile.close()


root.mainloop()