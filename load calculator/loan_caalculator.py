from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("500x500")
root.title("EMI Loan Calculator")
root.config(bg="#005580")


def calculate():
    try:
        p = int(amm_loan_var.get())
        r = float(intrest_var.get())
        n = int(term_year_var.get())

        r = r / 100 / 12  
        n = n * 12        

        if r == 0:
            monthly_payment = p / n
        else:
            monthly_payment = (p * r * (1 + r) ** n) / ((1 + r) ** n - 1)

        res_lab.config(text=f"EMI: {monthly_payment:.2f} ₹")

    except:
        tmsg.showinfo("Error","Enter All Required Fields To calculate")

    

main_lab = Label(root,bg="#005580",fg="White", text="EMI LOAN CALCULATOR", font=("lucida 20 bold"))
main_lab.pack(pady=20)

amm_loan_lab = Label(root,bg="#005580",fg="White", text="Amount Loan (₹): ", font=("lucida 15 bold"))
amm_loan_lab.place(x=50,y=100)

amm_loan_var = StringVar()
amm_loan_ent = Entry(root, textvariable=amm_loan_var, font=("lucida 15 bold"))
amm_loan_ent.place(x=250,y=100)




intrest_lab = Label(root,bg="#005580",fg="White", text="Intrest Rate (%): ", font=("lucida 15 bold"))
intrest_lab.place(x=50,y=150)

intrest_var = StringVar()
intrest_ent = Entry(root, textvariable=intrest_var, font=("lucida 15 bold"))
intrest_ent.place(x=250,y=150)





term_years_lab = Label(root,bg="#005580",fg="White", text="Loan Term (Years): ", font=("lucida 15 bold"))
term_years_lab.place(x=50,y=200)


term_year_var = StringVar()
term_year_ent = Entry(root, textvariable=term_year_var, font=("lucida 15 bold"))
term_year_ent.place(x=250,y=200)


res_lab = Label(root, text="EMI: ", bg="#005580",fg="White", font=("lucida 20 bold"))
res_lab.pack(side=BOTTOM,pady=50)





cal_btn = Button(root, text="CALCULATE", bg="#B48317",font=("lucida 10 bold"), command=calculate)
cal_btn.place(x=200,y=250)







root.mainloop()
