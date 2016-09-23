from tkinter import *
root=Tk()
root.title("Memo 3")
class cal:
    def __init__(self):
        self.p=0
        self.n=0
        
        self.enter1=Text(root)
        self.enter1.bind('<Enter>',self.ent)
        self.enter1.pack(side=RIGHT)
        self.enter1.focus()
        add=Button(root,text="Done",command=self.box)
        add.pack(side=BOTTOM)
        self.re()
        
    def ent(self):
        self.p+=1
        self.enter1.set("\n")
        self.enter1.set(self.p)
        
    def box(self):
        input = self.enter1.get("0.0",END)
        self.f=open("store","a")
        self.f.write(input+"\n")
        self.done()
        self.f.close()
    def re(self):
        self.f=open("store","r")
        get=[]
        get=self.f.readlines()
        j=0
        for i in range(j,len(get)-1):
            j+=1
        
            Checkbutton(root, text=get[i]).pack(side=RIGHT)
        
        self.f.close()
    
    def done(self):
         
        self.f=open("store","r")
        ag=[]
        ag=self.f.readlines()
        
        for i in range(self.n,len(ag)-1):
            self.n+=1
        
            Checkbutton(root, text=ag[i]).pack(side=RIGHT)
        
        self.f.close()
        self.enter1.set("\n"+self.i)
        self.enter1.delete(0,END)
cal()
mainloop()

