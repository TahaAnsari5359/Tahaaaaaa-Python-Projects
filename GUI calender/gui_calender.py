from tkinter import *
import tkinter.messagebox as tmsg
import calendar
root = Tk()
root.geometry("550x500")
root.config(bg="blue")
calander_lab = Label(root,bg="black",fg="white",text="CALENDAR",font=("algerian 25 bold"))
calander_lab.pack(fill=X)

def cal(event=None):
    try:
        year = int(e1_var.get())
        month = (e2_var.get()).strip()

        if month:
            monthh = int(e2_var.get())
            cal_month = calendar.month(year,monthh)
            l1.delete(1.0,END)
            l1.insert(1.0,cal_month)
            
        else:
            cal_year = calendar.calendar(year)
            l1.delete(1.0,END)
            l1.insert(1.0,cal_year)
    except:
        tmsg.showwarning("warning","input year or month")    
    
def clear():
    l1.delete(1.0,END)     

year = Label(root,bg="blue",fg="white",text="YEAR: ",font=("lucida 15 bold"))
year.place(x=100,y=64)
e1_var = StringVar()

e1_ent = Entry(root,width=10,textvariable=e1_var,font=("lucida 15 bold"))
e1_ent.pack(pady=20)



e2_var = StringVar()
e2_ent = Entry(root,width=10,textvariable=e2_var,font=("lucida 15 bold"))
e2_ent.pack(pady=10)
month = Label(root,fg="white",bg="blue",text="MONTH: ",font=("lucida 15 bold"))
month.place(x=100,y=120)


b1 = Button(root,text="GENERATE CALENDAR",font=("lucida 15 bold"),command=cal)
b1.pack(side=BOTTOM,pady=10)
root.bind('<Return>',cal)

l1 = Text(root,font=("lucida 10 bold"))
scroll_bar = Scrollbar(root,command=l1.yview)
scroll_bar.pack(side=RIGHT,fill=Y)
l1.pack(pady=10,padx=20,)

l1.config(yscrollcommand=scroll_bar.set)



b2 = Button(root,text="CLEAR",font=("lucida 15 bold"),command=clear)
b2.place(x=400,y=449)



root.mainloop()
