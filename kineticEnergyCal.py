from tkinter import*
from tkinter import messagebox
root=Tk()
root.title('Kinetic Energy Calculator')
root.geometry('700x500')

#======================================Variable=================
mass=StringVar()
velosity=StringVar()
Enery=StringVar()

def Calculate():
    a=mass.get()
    b=velosity.get()
    if a=='' or b=='':
        messagebox.showerror('Error','Please the data to be calculated')
    else:
        try:
            m=float(a)
            v=float(b)
            KE=0.5 * m * v * v
            Enery.set(KE)
            messagebox.showinfo('Kinetic Energy Calculator',Enery.get()+'\tJoules of Energy')
        except(ValueError,TypeError):
            messagebox.showwarning('Kinetic Energy Calculator','Invalid Data Entered')
            Reset()
            return False

def Reset():
    mass.set('')
    velosity.set('')
    Enery.set('')

def Exit():
    if messagebox.askyesno('Kinetic Energy Calculator','Do you really want to exit'):
        root.destroy()
        return


#======================================Frames=================
CF=Frame(root,bd=10,padx=20,pady=20,bg='#990099',relief=RIDGE)
CF.grid()
MF=Frame(CF,bd=10,width=640,height=500,padx=5,pady=5,bg='yellow',relief=RIDGE)
MF.grid()

titleFrame=Frame(MF,bd=10,width=610,height=100,padx=10,pady=10,bg='#00FFFF',relief=RIDGE)
titleFrame.pack(side=TOP)

EnergyFrame=LabelFrame(MF,text='Enter the object',font='Helvetica 18 bold',bd=10,width=610,height=200,padx=10,pady=10,relief=RIDGE)
EnergyFrame.pack(side=TOP)

ButtonFrame=Frame(MF,bd=10,width=610,height=150,padx=10,pady=10,relief=RIDGE)
ButtonFrame.pack(side=BOTTOM)

lblTitle=Label(titleFrame,text='How to calculate the Kinetic\n Energy of a Moving Object',font='Helvetica 31 bold',bg='#c0ded9')
lblTitle.pack(padx=2)

#=========================================================================
lblMass=Label(EnergyFrame,text='Mass in kilograms:',font='Helvetica 16 bold')
lblMass.grid(row=0,column=0,sticky='w')
txtMass=Entry(EnergyFrame,font='Helvetica 13 bold',width=27,bd=7,textvariable=mass)
txtMass.grid(row=0,column=1)

lblSpeed=Label(EnergyFrame,text='Speed in Meters Per Second:',font='Helvetica 16 bold')
lblSpeed.grid(row=1,column=0,sticky='w')
txtSpeed=Entry(EnergyFrame,font='Helvetica 13 bold',width=27,bd=7,textvariable=velosity)
txtSpeed.grid(row=1,column=1)

lblJoules=Label(EnergyFrame,text='Joules of Energy:',font='Helvetica 16 bold')
lblJoules.grid(row=2,column=0,sticky='w')
txtJoules=Entry(EnergyFrame,font='Helvetica 13 bold',width=27,bd=7,textvariable=Enery,state=DISABLED)
txtJoules.grid(row=2,column=1)

#===============================Buttons====================
btn1=Button(ButtonFrame,font='Helvetica 18 bold',bd=7,text='Calculate',bg='lime',fg='crimson',width=11,command=Calculate)
btn1.grid(row=0,column=0,padx=2,pady=2)
btn2=Button(ButtonFrame,font='Helvetica 18 bold',bd=7,text='Reset',bg='lime',fg='crimson',width=11,command=Reset)
btn2.grid(row=0,column=1,padx=2,pady=2)
btn3=Button(ButtonFrame,font='Helvetica 18 bold',bd=7,text='Exit',bg='lime',fg='crimson',width=11,command=Exit)
btn3.grid(row=0,column=2,padx=2,pady=2)

root.mainloop()