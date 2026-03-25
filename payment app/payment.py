from tkinter import *
from PIL import ImageTk, Image
import qrcode
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("410x580")
root.config(bg="#33A4B8")

def pay():
    name = name_var.get().strip()
    upi = upi_var.get().strip()
    amt_text = amm_var.get().strip()

    
    if name == "" or upi == "" or amt_text == "":
        tmsg.showwarning("Warning", "Fill All Details")
        return

    
    try:
        amount = int(amt_text)
    except ValueError:
        tmsg.showerror("Error", "Invalid Number")
        amm_var.set("")
        return

    
    upi_link = f"upi://pay?pa={upi}&pn={name}&am={amount}&cu=INR"

    qr = qrcode.make(upi_link)
    qr.save("upi_payment_qr.png")

    imge = Image.open("upi_payment_qr.png")
    resized = imge.resize((200, 200))
    imagee = ImageTk.PhotoImage(resized)

    qr_lab.config(image=imagee)
    qr_lab.image = imagee

    tmsg.showinfo("SUCCESSFULLY", "Successfully Generated")
    name_var.set("")
    upi_var.set("")
    amm_var.set("")


name_lab = Label(root,bg="#33A4B8",text="Name: ",font=("lucida 15 bold"))
name_lab.place(x=20,y=30)

name_var = StringVar()
name_ent = Entry(root,width=32,textvariable=name_var,font=("lucida 15 bold"))
name_ent.place(x=20,y=80)


upi_lab = Label(root,bg="#33A4B8",text='Upi Id: ',font=("lucida 15 bold"))
upi_lab.place(x=20,y=130)

upi_var = StringVar()
upi_ent = Entry(root,width=32,textvariable=upi_var,font=("lucida 15 bold"))
upi_ent.place(x=20,y=180)

amm_lab = Label(root,bg="#33A4B8",text='Amount No: ',font=("lucida 15 bold"))
amm_lab.place(x=20,y=230)
amm_00 = Label(root,bg="#33A4B8",text="RS",font=("lucida 15 bold"))
amm_00.place(x=80,y=280)

amm_var = StringVar()
amm_ent = Entry(root,width=5,textvariable=amm_var,font=("lucida 15 bold"))
amm_ent.place(x=20,y=280)

make_pay = Button(root,fg="white",bg="#176773",width=20,height=2,text="Make Payment",font=("lucida 10 bold "),command=pay)
make_pay.place(x=20,y=330)


qr_lab = Label(root,bg="#33A4B8",)
qr_lab.place(x=200, y=330)



root.mainloop()
