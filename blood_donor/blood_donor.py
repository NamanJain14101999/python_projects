from tkinter import *
from PIL import ImageTk,Image
import sqlite3
from scrolling_area import *
import tkinter.messagebox
from tkcalendar import *

root=Tk()
root.geometry("900x690+0+0")
root.config(bg="darkred")
root.title("blood group")
root.resizable(0,0)
l=Label(text="BLOOD DONATION", fg="BLACK", bg="darkred", font=("goudy stout", 25, "bold "))
l.pack()

def blood():
    frame = Frame(root, width=900, height=690, bg="red")
    frame.pack()
    img = ImageTk.PhotoImage(Image.open("pro4.jpg"))
    Label(frame, image=img, height=900, width=820).pack()
    b=Button(text="ADD", width=18, bd=10, bg="red", fg="black",command=lambda:add(frame,root))
    b.place(x=200, y=100)
    b1 = Button(text="SHOW", width=18, bd=10, bg="red", fg="black",command=lambda:show(frame,root))
    b1.place(x=400, y=100)

    frame.mainloop()

    #working of add btton

def add(frame,root):
    frame.destroy()
    frame2= Frame(root, width=1000, height=1000, bg="yellow")
    frame2.pack()
    img= ImageTk.PhotoImage(Image.open("pro3.jpg"))
    Label(frame2, image=img, height=900, width=690).pack()
    #entry
    l1 = Label(text="NAME", fg="black", font=("arial", 14, "bold "))
    l1.place(x=40, y=100)
    e1 = Entry(textvariable=StringVar(),width=32, bd=10, font=("arial", 14, "bold"))
    e1.place(x=300, y=90)
    l2 = Label(text="BLOOD GROUP", fg="black", font=("arial", 14, "bold "))
    l2.place(x=40, y=210)
    variable=StringVar(frame2)
    variable.set("A+")
    e2= OptionMenu(frame2,variable,"A+","B+","AB+","O+","A-","B-","AB-","O-")
    e2.config(width=32,bd=10)
    e2.place(x=300, y=150)
    l3 = Label(text="DOB", fg="black", font=("arial", 14, "bold "))
    l3.place(x=40, y=310)
    car1=IntVar()
    e3 = DateEntry(textvariable=car1,width=32, bd=10, font=("arial", 14, "bold"))
    e3.place(x=300, y=300)
    l4 = Label(text="CONTACT", fg="black", font=("arial", 14, "bold "))
    l4.place(x=40, y=410)
    e4 = Entry(textvariable=IntVar(),width=32, bd=10, font=("arial", 14, "bold"))
    e4.place(x=300, y=400)
    l5 = Label(text="ADDRESS", fg="black", font=("arial", 14, "bold "))
    l5.place(x=40, y=520)
    e5 = Entry(textvariable=StringVar(),width=32, bd=10, font=("arial", 14, "bold"))
    e5.place(x=300, y=510)
    #buttons in add
    b2 = Button(text="SUBMIT", width=20, bd=10, bg="red", fg="black",command=lambda:submit(frame2,root,e1,variable,e3,e4,e5))
    b2.place(x=50, y=600)
    b3 = Button(text="BACK", width=20, bd=10, bg="red", fg="black",command=lambda:back(frame2,root))
    b3.place(x=300, y=600)
    b4 = Button(text="RESET", width=20, bd=10, bg="red", fg="black",command=lambda:add(frame2,root))
    b4.place(x=580, y=600)

    frame2.mainloop()
   # def reset():
    #    e1.delete(0, END)
    #    e3.delete(0, END)
    #   e4.delete(0, END)
    #    e5.delete(0, END)
   # b4 = Button(text="RESET", width=20, bd=10, bg="red", fg="black",command=reset)
    #b4.place(x=580, y=600)

def back(frame2,root):     ##DATA BASE MANAGEMENT
    frame2.destroy()
    blood()


def back(frame3,root):     ##DATA BASE MANAGEMENT
    frame3.destroy()
    blood()


def submit(frame2,root,e1,variable,e3,e4,e5):

   ## if(len(a)==0 and len(b)==0 and len(c)==0 and len(d)==0 and len(e)==0 ) :
      ##  (tkinter.messagebox.showwarning("INCOMLPETE REGISTRAION","FIRSTLY FILL TE ENTIRE ENTRY BLOCK"))
    a=e1.get()
    b=variable.get()
    c=e3.get()
    d=e4.get()
    e=e5.get()
    print(a,b,c,d,e)
    con=sqlite3.connect("BLOODGROUP")
    con.execute("create table if not exists TEST(NAME char[20],BLOODGROUP char[20],DOB int[10],CONTACT int[30],ADDRESS char[80])")
    query="insert into TEST(NAME,BLOODGROUP,DATE,CONTACT,ADDRESS)Values('{}','{}',{},{},'{}')".format(a,b,c,d,e)
    i=con.execute(query)
    con.commit()
    m=con.execute("select * from TEST")
    print(list(m))
    print("DATA WILL BE SUCCESSFULLY INSERTED")
    con.close()


    if (len(a) == 0 or len(b) == 0 or len(c) == 0 or len(d) == 0 or len(e) == 0):
        tkinter.messagebox.showwarning("INCOMPLETE REGISTRATION", "FIRST FILL THE ENTRY BLOCKS")
    else:
        tkinter.messagebox.showinfo("SUCCESS", "REGISTRATION IS COMPLETED")
def show(frame,root):
    frame.destroy()
    frame3= Frame(root, width=900, height=690, bg="SKYBLUE")
    frame3.pack()
    img = ImageTk.PhotoImage(Image.open("pro2.jpg"))
    Label(frame3, image=img, height=900, width=790).pack()


    a = IntVar()
    b = IntVar()
    c = IntVar()
    d = IntVar()
    e = IntVar()
    f = IntVar()
    g = IntVar()
    h = IntVar()
    c1=Checkbutton(frame3,text="A+",height=2,width=2,bg="red",variable=a)
    c1.place(x=20,y=40)
    c2 = Checkbutton(frame3, text="B+", height=2, width=2, bg="red",variable=b)
    c2.place(x=20, y=100)
    c3 = Checkbutton(frame3, text="AB+", height=2, width=2, bg="red",variable=c)
    c3.place(x=20, y=160)
    c4 = Checkbutton(frame3, text="O+", height=2, width=2, bg="red",variable=d)
    c4.place(x=20, y=220)
    c5 = Checkbutton(frame3, text="A-", height=2, width=2, bg="red",variable=e)
    c5.place(x=20, y=280)
    c6 = Checkbutton(frame3, text="B-", height=2, width=2, bg="red",variable=f)
    c6.place(x=20, y=340)
    c7 = Checkbutton(frame3, text="AB-", height=2, width=2, bg="red",variable=g)
    c7.place(x=20, y=400)
    c8 = Checkbutton(frame3, text="O-", height=2, width=2, bg="red",variable=h)
    c8.place(x=20, y=460)


    b5= Button(text="OK", width=20, bd=10, bg="red", fg="black",command=lambda :OK(frame3,root,a,b,c,d,e,f,g,h))
    b5.place(x=50, y=600)
    b6 = Button(text="BACK", width=20, bd=10, bg="red", fg="black", command=lambda: back(frame3, root))
    b6.place(x=300, y=600)
    b7 = Button(text="RESET", width=20, bd=10, bg="red", fg="black", command=lambda: show(frame3, root))
    b7.place(x=580, y=600)

    frame3.mainloop()


def OK(frame3,root,a,b,c,d,e,f,g,h):
    frame3.destroy()
    frame4= Frame(root, width=900, height=690, bg="SKYBLUE")
    frame4.pack()
    img = ImageTk.PhotoImage(Image.open("pro5.jpg"))
    Label(frame4, image=img, height=1200, width=900).pack()

    b8 = Button(text="BACK", width=20, bd=10, bg="red", fg="black",command=lambda :show(frame4,root))
    b8.place(x=150, y=100)

    f1 = a.get()
    f2 = b.get()
    f3 = c.get()
    f4 = d.get()
    f5 = e.get()
    f6 = f.get()
    f7 = g.get()
    f8 = h.get()
    print(f1, f2, f3, f4, f5, f6, f7, f8)
    con = sqlite3.connect("BLOODGROUP")
    scrolling_area = Scrolling_Area(frame4, height=250)
    scrolling_area.place(x=120, y=350)
    table = Table(scrolling_area.innerframe,
                                        ["NAME","BLOODGROUP","DOB","CONTACT","ADDRESS"],
                                        column_minwidths=[120, 120, 120, 120, 120])
    table.pack(expand=True, fill=X)
    table.on_change_data(scrolling_area.update_viewport)

    if f1==1 :
        o1 = con.execute("select * from TEST where BLOODGROUP='A+'")
        con.commit()

        data = []
        for row in o1:
            column = []
            data.append(column)
            for r in row:
                print(r)
                column.append(r)

        table.set_data(data)

    if f2 == 1 :
        o2 = con.execute("select * from TEST where BLOODGROUP='B+'")
        con.commit()

        data = []
        for row in o2:
            column = []
            data.append(column)
            for r in row:
                column.append(r)

        table.set_data(data)

    if f3 == 1 :
        o3 = con.execute("select * from TEST where BLOODGROUP='AB+' ")
        con.commit()

        data = []
        for row in o3:
            column = []
            data.append(column)
            for r in row:
                column.append(r)

        table.set_data(data)

    if f4 == 1 :
        o4 = con.execute("select * from TEST where BLOODGROUP ='O+'")
        con.commit()

        data = []
        for row in o4:
            column = []
            data.append(column)
            for r in row:
                column.append(r)

        table.set_data(data)

    if f5 == 1 :
        o5 = con.execute("select * from TEST where BLOODGROUP='A-'")
        con.commit()

        data = []
        for row in o5:
            column = []
            data.append(column)
            for r in row:
                column.append(r)

        table.set_data(data)

    if f6 == 1 :
        o6 = con.execute("select * from TEST where BLOODGROUP='B-'")
        con.commit()

        data = []
        for row in o6:
            column = []
            data.append(column)
            for r in row:
                column.append(r)

        table.set_data(data)

    if f7 == 1 :
        o7 = con.execute("select * from TEST where BLOODGROUP='AB-'")
        con.commit()

        data = []
        for row in o7:
            column = []
            data.append(column)
            for r in row:
                column.append(r)

        table.set_data(data)

    if f8 == 1 :
        o8 = con.execute("select * from TEST where BLOODGROUP='O-'")
        con.commit()

        data = []
        for row in o8:
            column = []
            data.append(column)
            for r in row:
                column.append(r)

        table.set_data(data)

    if (f1 == 0 and f2 == 0 and f3 == 0 and f4 == 0 and f5 == 0 and f6 == 0 and f7 == 0 and f8 == 0):
         tkinter.messagebox.showwarning("INCOMPLETE REGISTRATION", "FIRST FILL THE ENTRY IN ADD")
    else:
        tkinter.messagebox.showinfo("SUCCESS", "DATA IS SHOWN")



    frame4.mainloop()
blood()