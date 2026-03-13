from tkinter import *
import tkinter.messagebox as tmsg
import random
root = Tk()
root.geometry("500x400")
root.config(bg="#2F3A68")
# root.resizable(False,False)
root.title("Passwoird Generator")

lowercase = "abcdefghijklmnopqrstuvwxyz"
nums = "1234567890"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?/"



main_lab = Label(root,bg="black",fg="white",text="PASSWORD GENERATOR",font=("lucida 15 bold"))
main_lab.pack(fill=X)


def genra():
    limits = slidebar.get()
    chars = ""

    if var1.get() == 1:
        chars+=nums
    

    if var2.get() == 1:
        chars+=uppercase

    

    

    if var3.get() == 1:
        chars+=lowercase

    
    

    if var4.get() == 1:
        chars+=symbols

    
    if chars == "":
        chars+=lowercase

    if limits >=1 and limits<=7:
        bar.config(text="strength = Weak",fg="red")


    elif limits >7 and limits<=14:
        bar.config(text="strength = Average",fg="yellow")

    elif limits >14 and limits<=20:
        bar.config(text="strength = Strong",fg="lime")




    password = "".join(random.choices(chars, k=limits))
    pass_lab.config(text=password,bg="#ED5435",relief=GROOVE,bd=4,)

    data = pass_lab.cget("text")
    root.clipboard_clear()
    root.clipboard_append(data)
    tmsg.showinfo("Success","Password Copied")


sel_lim = Label(root,bg="black",fg="white",text="Password Length: ",font=("lucida 10 bold"))
sel_lim.pack(pady=10,fill=X)


slidebar = Scale(root,bg="black",fg="white",from_=1, to=20,orient=HORIZONTAL)
slidebar.pack(pady=10,fill=X,padx=20)

framess = Frame(root,bg="#2F3A68",)
framess.pack()

var1 = IntVar()
only_num = Checkbutton(framess,bg="#21B4FE",relief=RIDGE,bd=4,variable=var1,text="Numbers",font=('lucida 12 bold'))
only_num.pack(pady=20,side=LEFT,fill=X)


var2 = IntVar()
only_num = Checkbutton(framess,bg="#21B4FE",relief=RIDGE,bd=4,variable=var2,text="uppercase",font=('lucida 12 bold'))
only_num.pack(pady=20,side=LEFT,fill=X)



var3 = IntVar()
only_num = Checkbutton(framess,bg="#21B4FE",relief=RIDGE,bd=4,variable=var3,text="lowercase",font=('lucida 12 bold'))
only_num.pack(pady=20,side=LEFT,fill=X)


var4 = IntVar()
only_num = Checkbutton(framess,bg="#21B4FE",relief=RIDGE,bd=4,variable=var4,text="symbol",font=('lucida 12 bold'))
only_num.pack(pady=20,side=LEFT,fill=X)






gen = Button(root,text="GENERATE",bg="#5435ED",fg="white",font=('lucida 13 bold'),command=genra)
gen.pack(side=BOTTOM,fill=X,padx=20,pady=20)


pass_lab = Label(root,font=("lucida 15 bold"),bg="#2F3A68")
pass_lab.pack(pady=20,fill=X)


bar = Label(root,font=("lucida 13 bold"),bg="#2F3A68")
bar.pack(pady=10,anchor=E,padx=20)



root.mainloop()
