from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("500x500")
root.config(bg="#D7C437")
root.title("Number System")
root.resizable(False,False)
main_lab = Label(root,bg="black",fg="white",text="NUMBER SYSTEM",font=("lucida 15 bold"))
main_lab.pack(fill=X)

e1_var = StringVar()
e1_ent = Entry(root,relief=GROOVE,bd=5,textvariable=e1_var,justify=CENTER,width=20,font=('lucida 15 bold'))
e1_ent.pack(pady=20)










def gens():
    nums = (e1_var.get())
    fromm = from_opt_var.get()
    too = to_opt_var.get()
    try:
        if fromm == "BINARY" and too == "DECIMAL":
            DATAS = int(nums,2)
            res_lab.config(text=f"binary: {nums} \n decimal: {DATAS}",bg='black',fg='white')

        elif fromm == "BINARY" and too == "OCTAL":
            DATAS = (oct(int(nums,2))[2:])
            res_lab.config(text=f"binary: {nums} \n octal: {DATAS}",bg='black',fg='white')

        elif fromm == "BINARY" and too == "HEXADECIMAL":
            DATAS = (hex(int(nums,2))[2:])
            res_lab.config(text=f"binary: {nums} \n hexadecimal: {DATAS}",bg='black',fg='white')


        elif fromm == "DECIMAL" and too == "BINARY":
            DATAS = bin(int(nums))[2:]
            res_lab.config(text=f"decimal: {nums} \n binary: {DATAS}",bg='black',fg='white')

        elif fromm == "DECIMAL" and too == "OCTAL":
            DATAS = oct(int(nums))[2:]
            res_lab.config(text=f"decimal: {nums} \n octal: {DATAS}",bg='black',fg='white')

        elif fromm == "DECIMAL" and too == "HEXADECIMAL":
            DATAS = hex(int(nums))[2:]
            res_lab.config(text=f"decimal: {nums} \n hexadecimal: {DATAS}",bg='black',fg='white')

        elif fromm == "OCTAL" and too == "DECIMAL":
            DATAS = (int(nums,8))
            res_lab.config(text=f"octal: {nums} \n decimal: {DATAS}",bg='black',fg='white')

        elif fromm == "OCTAL" and too == "BINARY":
            DATAS = (bin(int(nums,8))[2:])
            res_lab.config(text=f"octal: {nums} \n binary: {DATAS}",bg='black',fg='white')

        elif fromm == "OCTAL" and too == "HEXADECIMAL":
            DATAS = (hex(int(nums,8))[2:])
            res_lab.config(text=f"octal: {nums} \n hexadecimal: {DATAS}",bg='black',fg='white')

        elif fromm == "HEXADECIMAL" and too == "DECIMAL":
            DATAS = (int(nums,16))
            res_lab.config(text=f"hexadecimal: {nums} \n decimal: {DATAS}",bg='black',fg='white')


        elif fromm == "HEXADECIMAL" and too == "BINARY":
            DATAS = (bin(int(nums,16))[2:])
            res_lab.config(text=f"hexadecimal: {nums} \n binary: {DATAS}",bg='black',fg='white')

        elif fromm == "HEXADECIMAL" and too == "OCTAL":
            DATAS = (oct(int(nums,16))[2:])
            res_lab.config(text=f"hexadecimal: {nums} \n octal: {DATAS}",bg='black',fg='white')
        else:
            res_lab.config(text="ERROR SOMETHING WENT WRONG")

    except:
        tmsg.showwarning("warning","Input a Valid Number")
    e1_var.set("")

    

    









nums_f = Frame(root,bg="#D7C437")
nums_f.pack(pady=30,)


from_opt_var = StringVar()
from_opt_var.set("SELECT NUMBER SYSTEM")

from_opt_values = "DECIMAL","BINARY","OCTAL","HEXADECIMAL"

options_menu_1 = OptionMenu(nums_f,from_opt_var,*from_opt_values)
options_menu_1.pack(side=LEFT,padx=30)

options_menu_1.config(font=("lucida 9 bold"),bg="black",fg="white")


to_opt_var = StringVar()
to_opt_var.set("SELECT NUMBER SYSTEM")

to_opt_values = "DECIMAL","BINARY","OCTAL","HEXADECIMAL"

options_menu_2 = OptionMenu(nums_f,to_opt_var,*to_opt_values)
options_menu_2.pack(padx=30)
options_menu_2.config(font=("lucida 9 bold"),bg="black",fg="white")



gen_btn = Button(root,text="CALCULATE",bg="black",fg="white",width=20,font=("lucida 13 bold"),command=gens)
gen_btn.pack(side=BOTTOM,pady=20)

res_lab = Label(root,text="",font=("lucida 20 bold"),bg="#D7C437")
res_lab.pack(pady=50,fill=X)


root.mainloop()

















