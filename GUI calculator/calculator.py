from tkinter import *
import math
root = Tk()
root.geometry("430x600")
root.title("calculator")
root.config(bg="#0C544E")
root.resizable(False,False)


def nums(event):
    value = event.widget["text"]
    e1_var.set((e1_var.get())+value)

def clear():
    current_text = e1_var.get()
    e1_var.set(current_text[:-1])

def all_clr():
    e1_var.set("")

def equals():
    try:
        getting = e1_var.get()
        new = getting.replace("x","*").replace("÷","/")
        result = eval(new)
        e1_var.set(result)
    except ZeroDivisionError:
    
        e1_var.set("cannot divide by 0")
    except:
        e1_var.set("ERROR")
    

def sin():
    try:
        rad_ent = float(e1_var.get())
        rad = math.radians(rad_ent)

        sin_math = math.sin(rad)
        e1_var.set(f"{sin_math:.4f}")

    except:
        e1_var.set("ERROR")


def cos():
    try:
        rad_ent = float(e1_var.get())
        rad = math.radians(rad_ent)

        sin_math = math.cos(rad)
        e1_var.set(f"{sin_math:.4f}")

    except:
        e1_var.set("ERROR")


def tan():
    try:
        rad_ent = float(e1_var.get())
        rad = math.radians(rad_ent)

        sin_math = math.tan(rad)
        e1_var.set(f"{sin_math:.4f}")

    except:
        e1_var.set("ERROR")

def square():
    try:
        getttt = float(e1_var.get())
        square = math.sqrt(getttt)
        e1_var.set(f"{square:.3f}")

    except:
        e1_var.set("ERROR")


def cube():
    try:
        cube_value = float(e1_var.get())
        cube_root = math.pow(cube_value,1/3)
        e1_var.set(f"{cube_root:.3f}")
    except:
        e1_var.set("ERROR")






show_more = False

def more_info():
    global show_more
    if not show_more:
        root.geometry("530x600")

        res = e1_var.get()

        sin_btn = Button(root,text="sin",fg="white",bg="blue",width=4,height=2,font=("lucida 20 bold"),command=sin)
        sin_btn.place(x=430,y=80)

        cos_btn = Button(root,text="cos",fg="white",bg="blue",width=4,height=2,font=("lucida 20 bold"),command=cos)
        cos_btn.place(x=430,y=180)

        tan_btn = Button(root,text="tan",fg="white",bg="blue",width=4,height=2,font=("lucida 20 bold"),command=tan)
        tan_btn.place(x=430,y=280)

        square_btn = Button(root,text="√",fg="white",bg="blue",width=4,height=2,font=("lucida 20 bold"),command=square)
        square_btn.place(x=430,y=380)

        cube_btn = Button(root,text="∛",fg="white",bg="blue",width=4,height=2,font=("lucida 20 bold"),command=cube)
        cube_btn.place(x=430,y=480)



        b1 = bmore.config(text="<")
        show_more=True

    else:
        root.geometry("430x600")
        
        bmore.config(text=">")
        show_more = False







e1_var = StringVar()
e1_ent = Entry(root,textvariable=e1_var,font=('lucida 25 bold'))
e1_ent.pack(fill=X,padx=20,pady=20)

b7 = Button(root,text="7",width=4,height=2,font=("lucida 20 bold"))
b7.place(x=30,y=180)
b7.bind("<Button-1>", nums)

b8 = Button(root,text="8",width=4,height=2,font=("lucida 20 bold"))
b8.place(x=130,y=180)
b8.bind("<Button-1>", nums)

b9 = Button(root,text="9",width=4,height=2,font=("lucida 20 bold"))
b9.place(x=230,y=180)
b9.bind("<Button-1>", nums)

b4 = Button(root,text="4",width=4,height=2,font=("lucida 20 bold"))
b4.place(x=30,y=280)
b4.bind("<Button-1>", nums)

b5 = Button(root,text="5",width=4,height=2,font=("lucida 20 bold"))
b5.place(x=130,y=280)
b5.bind("<Button-1>", nums)

b6 = Button(root,text="6",width=4,height=2,font=("lucida 20 bold"))
b6.place(x=230,y=280)
b6.bind("<Button-1>", nums)


b1 = Button(root,text="1",width=4,height=2,font=("lucida 20 bold"))
b1.place(x=30,y=380)
b1.bind("<Button-1>", nums)

b2 = Button(root,text="2",width=4,height=2,font=("lucida 20 bold"))
b2.place(x=130,y=380)
b2.bind("<Button-1>", nums)


b3 = Button(root,text="3",width=4,height=2,font=("lucida 20 bold"))
b3.place(x=230,y=380)
b3.bind("<Button-1>", nums)


b0 = Button(root,text="0",width=4,height=2,font=("lucida 20 bold"))
b0.place(x=30,y=480)
b0.bind("<Button-1>", nums)


b_clear = Button(root,text="⌫",width=4,height=2,bg="orange",font=("lucida 20 bold"),command=clear)
b_clear.place(x=230,y=80)

bAC = Button(root,text="AC",bg="orange",width=4,height=2,font=("lucida 20 bold"),command=all_clr)
bAC.place(x=130,y=80)



b_add = Button(root,text="+",width=4,bg="orange",height=2,font=("lucida 20 bold"))
b_add.place(x=330,y=80)
b_add.bind("<Button-1>", nums)

b_sub = Button(root,text="-",width=4,bg="orange",height=2,font=("lucida 20 bold"))
b_sub.place(x=330,y=180)
b_sub.bind("<Button-1>", nums)

b_mul = Button(root,text="x",width=4,bg="orange",height=2,font=("lucida 20 bold"))
b_mul.place(x=330,y=280)
b_mul.bind("<Button-1>", nums)

b_div = Button(root,text="÷",width=4,bg="orange",height=2,font=("lucida 20 bold"))
b_div.place(x=330,y=380)
b_div.bind("<Button-1>", nums)

bdot = Button(root,text=".",width=4,height=2,font=("lucida 20 bold"))
bdot.place(x=130,y=480)
bdot.bind("<Button-1>", nums)

bequal = Button(root,text="=",bg="orange",width=10,height=2,font=("lucida 20 bold"),command=equals)
bequal.place(x=230,y=480)


bmore = Button(root,text=">",bg="red",width=4,height=2,font=("lucida 20 bold"),command=more_info)
bmore.place(x=30,y=80)


root.mainloop()
