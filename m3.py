from tkinter import *
root=Tk()
root.title("Memo 3")
class cal:
    def __init__(self):
        
        self.frame=Frame(root,width=250,height=250)
        self.frame.grid()
        self.str1=StringVar()
        self.str2=StringVar()
        self.str3=StringVar()
        self.str4=StringVar()
        enter1=Entry(self.frame,textvariable=self.str1)
        enter1.grid(row=2,column=0,columnspan=6)
        enter2=Entry(self.frame,textvariable=self.str2)
        enter2.grid(row=3,column=0,columnspan=6)
        enter3=Entry(self.frame,textvariable=self.str3)
        enter3.grid(row=4,column=0,columnspan=6)
        enter4=Entry(self.frame,textvariable=self.str4)
        enter4.grid(row=5,column=0,columnspan=6)
        add=Button(self.frame,text="Done",command=self.box)
        add.grid(row=6,column=7)
        
        self.re()
    def box(self):
        self.f=open("store","w")
        self.f.write(self.str1.get()+"\n")
        
        
        self.f.write(self.str2.get()+"\n")
        
        self.f.write(self.str3.get()+"\n")

        self.f.write(self.str4.get()+"\n")
        self.done()
        self.f.close()
    def re(self):
        self.f=open("store","r")
        get=[]
        get=self.f.readlines()
        self.str1.set(get[0])
        self.str2.set(get[1])
        self.str3.set(get[2])
        self.str4.set(get[3])
        self.f.close()
    def done(self):
        self.f=open("store","r")
        ag=[]
        ag=self.f.readlines()
        Checkbutton(self.frame, text=ag[0]).grid(row=7)
        Checkbutton(self.frame, text=ag[1]).grid(row=8)
        Checkbutton(self.frame, text=ag[2]).grid(row=9)
        Checkbutton(self.frame, text=ag[3]).grid(row=10)
        self.f.close()
        
cal()
mainloop()

