from tkinter import *


root =Tk()
root.title("QS progarm")
root.iconbitmap('Thesquid.ink-Free-Flat-Sample-Owl.ico')
def de():
    rootd=Tk()
    rootd.title("Deterministic system")

    l1=Label(rootd,text="lamda value is:")
    l1.grid(row=0,column=0)
    entre1=Entry(rootd,width=50)
    entre1.grid(row=0,column=1)
    entre1.insert(0,"0")
    l2= Label(rootd, text="meo value is:")
    l2.grid(row=1, column=0)
    entre2 = Entry(rootd, width=50)
    entre2.grid(row=1, column=1)
    entre2.insert(0, "0")
    def mul(x,y):
     rtd=Tk()
     rtd.title("Result screen")
     z=x*y

     l3=Label(rtd,text=str(z),width=100)
     l3.pack()
     rtd.mainloop()
    btn = Button(rootd, text="submit", padx=50, pady=50, command=lambda:mul(int(entre1.get()),int(entre2.get())))
    btn.grid(row=2)
    rootd.mainloop()

fram=LabelFrame(root,text="welcom to the QS program",padx=100,pady=100,bg="red")
fram.grid(row=0)
f=LabelFrame(root,image=)
btnd=Button(fram,text="Determinstic",command=de,padx=100,pady=100)
btnd.grid(row=0)

btnm=Button(root,text="M/M....",padx=110,pady=100)
btnm.grid(row=2)





root.mainloop()