from tkinter import *
root=Tk()
root.title("Yuvi's CAl")


class cal:
    def __init__(self):
        self.frame=Frame(root,width=250,height=250)
        self.frame.grid()
        self.string=StringVar()
        self.count=1  
        self.ad()
        self.box()
   
    def ad(self):
        self.wrt()
        add=Button(self.frame,text="add",command=self.box)
        add.grid(row=self.count,column=7)
        
    def done(self):
        self.now=self.count-1
        
        add=Button(self.frame,text="done",command=self.box)
        add.grid(row=self.now,column=7)
    def box(self):    

        self.count+=1
        self.string=StringVar()
        enter=Entry(self.frame,textvariable=self.string)
        enter.grid(row=self.count,column=0,columnspan=6)
        self.done()
        self.ad()
        
    def wrt(self):
        cher="a"
        file=open("store2",cher)
        file.write("\n")
        file.write(self.string.get())  
        file.close()    
        
        
        
ca=cal()
ca.__init__()
      
mainloop()