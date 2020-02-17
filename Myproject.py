from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
class project:
    def helpfun(self):
        root = Tk()
        root.geometry("400x400")
        root.title("HELP DESK")
        root.configure(bg="#E1F5A9")
        var = "GOOGLE IT "
        label = Label( root,bg="#E1F5A9", text=var)
        label.pack()

    def click1(self):
        global a
        a=a+1
        messagebox.showinfo("notice","vote has been conformed")
        return
    def click2(self):
        global b
        b=b+1
        messagebox.showinfo("notice","vote has been conformed")
        return
    def click3(self):
        global c
        c=c+1
        messagebox.showinfo("notice","vote has been conformed")
        return
    def click4(self):
        global d
        d=d+1
        messagebox.showinfo("notice","vote has been conformed")
        return
    def reset(self): 
        messagebox.showinfo("NOTICE","DATA RESET DONE")
        #initialize global variables to 0
        global a
        a=0
        global b
        b=0
        global c
        c=0
        global d
        d=0
        #delete data from data.txt
        f = open('data.txt','r+')
        f.truncate(0)
        f = open('data2.txt','r+')
        f.truncate(0) 
        return
    def reg_window(self):
        top=Tk()
        top.geometry("1920x1080")
        top.title("REGISTRATION WINDOW")
        top.configure(bg="#E1F5A9")
        labelfont = ('times', 20, 'bold')
        self.Entry3 = Entry(top)
        self.Entry3.place(relx=0.383, rely=0.267,height=36, relwidth=0.34)
        self.Entry4 =Entry(top)
        self.Entry4.place(relx=0.383, rely=0.4,height=36, relwidth=0.34)
        self.Entry5 =Entry(top)
        self.Entry5.place(relx=0.383, rely=0.533,height=36, relwidth=0.34)
        self.Label1 =Label(top,text="New ID :",bg="#E1F5A9",font=labelfont)
        self.Label1.place(relx=0.25, rely=0.272, height=26, width=122)
        self.Label2 =Label(top,text="Password :",bg="#E1F5A9",font=labelfont)
        self.Label2.place(relx=0.25, rely=0.405, height=26, width=147)
        self.Label3 =Label(top,text="Re-Enter Password :",bg="#E1F5A9",font=labelfont)
        self.Label3.place(relx=0.20, rely=0.538, height=26, width=288)
        self.Button1 =Button(top,text="Register",bg="#E1F5A9",font=('systemfixed', 18),command=self.register)
        self.Button1.place(relx=0.433, rely=0.650, height=43, width=118)
        return

    def register(self):
        i3=self.Entry3.get()
        i4=self.Entry4.get()
        i5=self.Entry5.get()
        if i3=="":
            messagebox.showinfo("NOTICE","Please Enter Valid User Name")
            return
        file1 = open("data.txt", "r")
        if ((" "+i3+"-") not in file1.read()) and i3!="5g8":
            if(i4==i5):
                file1 = open("data.txt", "a")
                file1.write(" "+i3+"-"+i4+" \n")
                file1.close()
                messagebox.showinfo("NOTICE","REGISTRATION SUCCESS") 
            else :
                messagebox.showerror("WARNING","PASSWORD DIDN'T MATCH")
        else:
            messagebox.showwarning("NOTICE","User Name Already Exists")
        file1.close()
    def LOGIN_WINDOW(self):
        master=Tk()
        master.geometry("1920x1080")
        master.title("LOGIN WINDOW")
        master.configure(background="#E1F5A9")
        self.admin="5g8"
        labelfont = ('times', 20, 'bold')
        label1=Label(master,text="LOGIN ID :",bg="#E1F5A9",font=labelfont)
        label1.place(relx=0.25, rely=0.244, height=36, width=170)
        self.label2=Label(master,text="PASSWORD :",bg="#E1F5A9",font=labelfont)
        self.label2.place(relx=0.25, rely=0.378, height=36, width=198)
        self.entry1=Entry(master)
        self.entry1.place(relx=0.4, rely=0.244,height=36, relwidth=0.34)
        self.entry2=Entry(master,show="*")
        self.entry2.place(relx=0.4, rely=0.378,height=36, relwidth=0.34)
        self.button1=Button(master,text="Login",bg="#E1F5A9",font=('systemfixed', 18),command=self.storedata)
        self.button1.place(relx=0.300, rely=0.500, height=48, width=98)
        self.button3=Button(master,text="New User",bg="#E1F5A9",font=('systemfixed', 18),command=self.reg_window)
        self.button3.place(relx=0.550, rely=0.500, height=48, width=138)
        self.button2=Button(master,text="HELP",bg="#E1F5A9",command=self.helpfun)
        self.button2.place(relx=0.833, rely=0.044, height=33, width=56)
        #voting part
    def cheak(self,i1,i2):
        file1 = open("data.txt", "r")
        if (" "+i1+"-"+i2+" \n") in file1.read():
            return 1
        else :
            return 0 
        file1.close()
    def cheak2(self,i1,i2):
        file1 = open("data2.txt", "r")
        if (" "+i1+"-"+i2+" \n") in file1.read():
            return 1
        else :
            return 0
        file1.close()
    def storedata(self):
        i1=self.entry1.get()
        i2=self.entry2.get()
        if (i1!=self.admin):
            if self.cheak(i1,i2):
                if self.cheak2(i1,i2)==0:
                    file1 = open("data2.txt", "a")
                    file1.write(" "+i1+"-"+i2+" \n") 
                    file1.close()
                    top=Tk()
                    top.geometry("1920x1080")
                    top.title('Electronic Voting Machine')
                    top.configure(bg="#E1F5A9")
                    lab=Label(top,text="AP election commision",bg="#E1F5A9",font=("times",20,"bold"))
                    lab.place(relx=0.405, rely=0.086, height=26, width=320)
                    self.TSeparator0 = ttk.Separator(top)
                    self.TSeparator0.place(relx=0.0, rely=0.145, relwidth=0.983)
                    self.TSeparator1 = ttk.Separator(top)
                    self.TSeparator1.place(relx=0.0, rely=0.15, relwidth=0.983)
                    lab1=Label(top, text='PARTY1',bg="yellow",fg="green",font=10,width=50,height=3)
                    lab1.place(relx=0.255, rely=0.209, height=43, width=300)
                    button1=Button(top, text='vote',bg="#E1F5A9",font=10,width=7,height=2, command=self.click1)
                    button1.place(relx=0.573, rely=0.209, height=43, width=76)
                    lab2=Label(top,text="PARTY2",bg="blue",font=10,fg="white",width=50,height=3)
                    lab2.place(relx=0.255, rely=0.333, height=43, width=300)
                    button2=Button(top,text="vote",bg="#E1F5A9",font=10,width=7,height=2,command=self.click2)
                    button2.place(relx=0.573, rely=0.333, height=43, width=76)
                    lab3=Label(top,text="PARTY3",bg="red",font=10,fg="white",width=50,height=3)
                    lab3.place(relx=0.255, rely=0.467, height=43, width=300)
                    button3=Button(top,text="vote",bg="#E1F5A9",font=10,width=7,height=2,command=self.click3)
                    button3.place(relx=0.573, rely=0.467, height=43, width=76)
                    lab4=Label(top,text="Independent",bg="green",font=10,fg="white",width=50,height=3)
                    lab4.place(relx=0.255, rely=0.6, height=43, width=300)
                    button4=Button(top,text="vote",bg="#E1F5A9",font=10,width=7,height=2,command=self.click4)
                    button4.place(relx=0.573, rely=0.6, height=43, width=76)
                else:
                    messagebox.showwarning("WARNING","you can't vote again !!!! ")
                    return
            else:
                messagebox.showwarning("Warning","UNKNOWN USER")
        #admin login frame
        if (i2=="5g8") and (i1==self.admin):
            top=Tk()
            top.geometry("400x300+350+350")
            top.title("ADMIN CONTROL")
            top.configure(background="#E1F5A9")
            button5=Button(top,text="RESULT",bg="#E1F5A9",width=6,height=2,command=self.results)
            button5.place(relx=0.214, rely=0.267, height=63, width=96)
            ButtonReset = Button(top, text="Reset",bg="#E1F5A9",width=6,height=2, command=self.reset)
            ButtonReset.place(relx=0.567, rely=0.267, height=63, width=96)
    def results(self):
        global a,b,c,d
        global s
        s=a+b+c+d
        m=max(a,b,c,d)
        if s!=0:
            if m==a and not(a==b or a==c or a==d):
                percent=str(round((a/s)*100,2))
                s1=str(s)
                messagebox.showinfo("RESULT","PARTY1 wins with "+percent +"% in "+s1+" votes")
                f = open('data.txt','r+')
                f.truncate(0)
                return
            if m==b and not(b==c or b==d or b==a):
                percent=str(round((b/s)*100,2))
                s1=str(s)
                messagebox.showinfo("RESULT","PARTY2 wins with "+percent +"% in "+s1+" votes")
                f = open('data.txt','r+')
                f.truncate(0)
                return
            if m==c and not(a==c or b==c or c==d):
                percent=str(round((c/s)*100,2))
                s1=str(s)
                messagebox.showinfo("RESULT","PARTY3 wins with "+percent +"% in "+s1+" votes")
                f = open('data.txt','r+')
                f.truncate(0)
                return
            if m==d and not(a==d or b==d or c==d):
                percent=str(round((d/s)*100,2))
                s1=str(s)
                messagebox.showinfo("RESULT","Independent wins with "+percent +"% in "+s1+" votes")
                f = open('data.txt','r+')
                f.truncate(0)
                return
            if a==b or a==c or a==d or b==c or b==d or c==d:
                messagebox.showinfo("RESULT","Please Perfom Manual Power Comparision")
                f = open('data.txt','r+')
                f.truncate(0)
                return
        else:
            messagebox.showinfo("WARNING","please perform election")
a=0
b=0
c=0
s=0
d=0
top=project()
top.LOGIN_WINDOW()