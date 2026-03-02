from tkinter import *
from datetime import datetime
from tkcalendar import Calendar
from tkinter import messagebox as tmsg
from dateutil.relativedelta import relativedelta
root=Tk()
root.geometry("400x500")
root.title("AGE CALCULATOR WITH NEW FEATURES")


def date_pick():
    def chose():
        selected = cal.get_date()
        formatted = datetime.strptime(selected, "%m/%d/%y").strftime("%d-%m-%Y")
        e1_var.set(formatted)
        top.destroy()


    top = Toplevel(root)
    top.grab_set()
    top.title("CHOOSE DATE")

    cal = Calendar(top, selectmode='day')
    cal.pack()

    choose_btn = Button(top,text="Choose Date",command=chose)
    choose_btn.pack(side=BOTTOM)



def cal():
    dobvar = e1_var.get()
    
    try:
        dob = datetime.strptime(dobvar, "%d-%m-%Y")

        today = datetime.today()

        if dob > today:
            tmsg.showerror("Invalid Date, You Cant Calculate Future")
            return

        difference = relativedelta(today,dob)
    
        year_res.config(text=f"{difference.years} Yrs")
        month_res.config(text=f'{difference.months} Month')
        day_res.config(text=f"{difference.days} days")

    except ValueError:
        tmsg.showerror("Error", "Enter date in DD-MM-YYYY format")
        return








e1_var = StringVar()
e1_ent = Entry(root, width=13,textvariable=e1_var,font=("lucida 15 bold"))
e1_ent.place(x=50,y=50)

pick_dat_btn = Button(root,text="Pick Date",font=("lucida 10 bold"),bg="Blue",fg='white',command=date_pick)
pick_dat_btn.place(x=240,y=50)


cal_age = Button(root,text="CALCULATE AGE",font=("lucida 10 bold"),bg="Blue",fg='white',command=cal)
cal_age.pack(side=BOTTOM,fill=X,pady=10,padx=10)


result_label = Label(root,text="",font=("lucida 20 bold"))
result_label.pack(pady=150)

year_lab = Label(root,text="YEAR: ",font=("lucida 20 bold"))
year_lab.place(x=80,y=150)

year_res = Label(root,font=("lucida 20 bold"))
year_res.place(x=200,y=150)



month_lab = Label(root,text="MONTH: ",font=("lucida 20 bold"))
month_lab.place(x=80,y=200)

month_res = Label(root,font=("lucida 20 bold"))
month_res.place(x=200,y=200)




day_lab = Label(root,text="DAY: ",font=("lucida 20 bold"))
day_lab.place(x=80,y=250)

day_res = Label(root,font=("lucida 20 bold"))
day_res.place(x=200,y=250)



root.mainloop()
