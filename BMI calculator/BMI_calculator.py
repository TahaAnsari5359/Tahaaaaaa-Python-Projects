from tkinter import *
root= Tk()
root.title("BMI calculator")
root.geometry("500x400")
root.resizable(False,False)
root.config(bg="#1F597A")


def cal():
    weight = float(weight_var.get())
    height = float(height_var.get())

    meter = height / 100
    bmi_for = weight/(meter*meter)
    result_bmi.config(text=f"BMI = {bmi_for:.2f}",bg="#AD1EAD",fg="white")

    if bmi_for < 18.5:
        cato_lab.config(text=f"CATEGORY = Underweight",bg="#00BFFF")

    elif 18.5 <= bmi_for <=24.9:
        cato_lab.config(text=f"CATEGORY = Normal",bg="#32CD32")


    elif 25.0 <= bmi_for <=29.9:
        cato_lab.config(text=f"CATEGORY = Overweight",bg="#FFA500")

    elif 20.0 <= bmi_for <=34.9:
        cato_lab.config(text=f"CATEGORY = Obesity 1",bg="#FF4500")

    elif 35.0 <= bmi_for <=39.9:
        cato_lab.config(text=f"CATEGORY = Obesity 2",bg="#FF0000",fg="white")

    else:
        cato_lab.config(text=f"CATEGORY = Obesity 3",bg="#8B0000",fg="white")

    weight_var.set("")
    height_var.set("")








bmi_lab = Label(root, bg="purple",fg="white",text="BMI CALCULATOR",font=("lucida 25 bold"))
bmi_lab.pack(fill=X)

weight_lab = Label(root,bg="#1F597A",fg="white",text="Weight : ",font=("lucida 15 bold"))
weight_lab.place(x=100,y=100)

weight_var = StringVar()
weight_ent = Entry(root,highlightthickness=2,width=6,textvariable=weight_var,font=("lucida 15 bold"))
weight_ent.place(x=200,y=100)

kg_lab = Label(root,bg="#1F597A",fg="white",text="kg",font=("lucida 15 bold"))
kg_lab.place(x=280,y=100)



height_lab = Label(root,bg="#1F597A",fg="white",text="Height : ",font=("lucida 15 bold"))
height_lab.place(x=100,y=150)

height_var = StringVar()
height_ent = Entry(root,highlightthickness=2,width=6,textvariable=height_var,font=("lucida 15 bold"))
height_ent.place(x=200,y=150)

cm_lab = Label(root,bg="#1F597A",fg="white",text="cm",font=("lucida 15 bold"))
cm_lab.place(x=280,y=150)

cal_bmi = Button(root,bg="red",fg="white",width=30,text="CALCULATE BMI",font=('lucida 15 bold'),command=cal)
cal_bmi.place(x=60,y=200,)



cato_lab = Label(root,bg="#1F597A",font=("lucida 25 bold"))
cato_lab.pack(fill=X,side=BOTTOM)

result_bmi = Label(root,bg="#1F597A",font=("lucida 25 bold"))
result_bmi.pack(fill=X,side=BOTTOM)

root.mainloop()
