from tkinter import *
import tkinter.messagebox as tmsg
import threading
import random
import time
root = Tk()
root.geometry("400x500")
root.config(bg="#AC9E22")
root.title("Name Picker For Game")


listss = []


def addd(Event=None):
    if name_var.get() != "":
        list_box.pack(side=LEFT,fill=BOTH,pady=10,)
        scrollbar.pack(side=RIGHT,fill=Y,padx=10)
        data = name_var.get().strip()
        list_box.insert(END,data)
        listss.append(data)
        name_var.set("")
    else:
        tmsg.showerror("error","Enter Data To Add")
        return
def randomss():
    rands = random.choice(listss)
    res_status.config(text=f"Choose : {rands} ",bg="lime",fg="black",font=("lucida 20 bold"))
    rem.pack(side=BOTTOM,padx=10,pady=10)

def trysthread(Event=None):
    def statusbar():
        if listss:
            res_status.config(text="Spinning..",bg="red",fg="white")
            time.sleep(2)
            # root.after(1500)
            res_status.config(text="Spinning...",bg="red",fg="white")
            time.sleep(3)
            # root.after(1500)
            res_status.config(text="Spinning....",bg="red",fg="white")
            time.sleep(2)
            # root.after(1500)
            res_status.config(text="Spinning.....",bg="red",fg="white")
            time.sleep(3)
            # root.after(1500)
            res_status.config(text="Choosing Randomly...",bg="red",fg="white")
            time.sleep(2)
            # root.after(2000)
            res_status.config(text="Choosing Randomly....",bg="red",fg="white")
            time.sleep(3)
            # root.after(2000)
            res_status.config(text="Choosing Randomly.....",bg="red",fg="white")
            time.sleep(2)
            # root.after(2000)
            res_status.config(text="Almost Done",bg="red",fg="white")
            time.sleep(3)
            # root.after(3000)
            randomss()
        else:
            tmsg.showerror("ERROR","No Data Found")
            return
    threading.Thread(target=statusbar,daemon=True).start()

def removee(Event=None):
    selected = list_box.curselection()
    if selected:
        
        index = selected[0]
        value = list_box.get(index)

        list_box.delete(index)
        listss.remove(value)



btn_f = Frame(root,bg="#AC9E22")
btn_f.pack(side=BOTTOM)

add_names_btn = Button(btn_f,relief=GROOVE,bd=5,bg="#4651B5",fg="white",text="ADD NAMES",font=("lucida 13 bold"),command=addd)
add_names_btn.pack(side=RIGHT,padx=10,pady=10)
root.bind('<Return>',addd)



gen = Button(btn_f,bg="#4651B5",relief=GROOVE,bd=5,fg="white",text="RANDOM",font=("lucida 13 bold"),command=trysthread)
gen.pack(side=RIGHT,padx=10,pady=10)
root.bind('<Tab>',trysthread)


rem = Button(btn_f,bg="#4651B5",relief=GROOVE,bd=5,fg="white",text="REMOVE",font=("lucida 13 bold"),command=removee)
root.bind('<Delete>',removee)



main_lab = Label(root,bg="black",fg="white",text="RANDOM NAME PICKER",font=("Arial 15 bold"))
main_lab.pack(fill=X)

name_var = StringVar()
name_ent = Entry(root,justify=CENTER,relief=SUNKEN,bd=3,textvariable=name_var,font=("lucida 15 bold"))
name_ent.pack(pady=10)

list_and_scrol_f = Frame(root,bg="#AC9E22")
list_and_scrol_f.pack(side=BOTTOM)


list_box = Listbox(list_and_scrol_f,height=5,relief=RIDGE,bd=4,width=22,font=("lucida 20 bold"))

scrollbar = Scrollbar(list_and_scrol_f,command=list_box.yview)

list_box.config(yscrollcommand=scrollbar.set)

res_status = Label(root,bg="#AC9E22",font=("lucida 15 bold"))
res_status.pack(pady=40,fill=X)

root.mainloop()
