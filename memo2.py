from tkinter import *
import random
import string
root=Tk()
root.title("memo2")


class cal:
    def __init__(self):
        self.fr=Frame(root,width=250,height=250)
        self.fr.grid(row=0,column=0)
    
        
        but=Button(self.fr,text="+",command=self.writ)
        but.grid()
        self.n=0
        
                
    def writ(self):
        self.n+=1
        self.name=random.choice("asdfghjjkkll")
        self.name= StringVar()
        print(self.name)
        ent=Entry(self.fr,textvariable=self.name)
        ent.grid(row=self.n,column=0)
        self.re()
    def re(self):
        f=open("store","a")
        f.write("\n")
        
        f.write(self.name.get())    
        
       
        
        
        
ca=cal()

mainloop()    
        