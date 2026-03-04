from tkinter import *
import tkinter.messagebox as tmsg
import tkinter.filedialog as fd
from datetime import datetime
import winsound
import win32print, win32ui
root = Tk()
root.geometry("550x500")
root.resizable(False,False)



print(win32print.GetDefaultPrinter())


def printss():
    itemss = data_list.get(0,END)
    text_to_print = "\n".join(itemss)


    raw_data = text_to_print.encode()

    printer_name = win32print.GetDefaultPrinter()
    hPrinter = win32print.OpenPrinter(printer_name)
    win32print.StartDocPrinter(hPrinter, 1, ("Listbox Print", None, "RAW"))
    win32print.WritePrinter(hPrinter,raw_data)
    win32print.EndPagePrinter(hPrinter)
    win32print.EndDocPrinter(hPrinter)
    win32print.ClosePrinter(hPrinter)




root.config(bg="#7FB1E3")

main_lab = Label(root,bg="black",fg="white",text="Smart Billing System",font=("lucida 15 bold"))
main_lab.pack(fill=X)

listss = []


date_lab = Label(root, bg="#7FB1E3", font=("lucida 12 bold underline"))
date_lab.place(x=30, y=50)


def datess():
    global date_lab 
    curr_date = datetime.now()
    date_lab.config(text=f"DATE: {curr_date.strftime('%d-%m-%Y   %I:%M:%S')}")
    root.after(100, datess)
    
datess()


def add_data(Event=None):
    try:

        prod_name = pro_var.get()
        amm = int(amou_var.get())
        quan = int(quan_var.get())

        addings = f"Product: {prod_name} | Amount: {amm} | Quantity: {quan}"
        list_box.insert(END,addings)
        listss.append((prod_name,amm,quan))
        pro_var.set("")
        amou_var.set("")
        quan_var.set("")
        gen_bill.place(x=180,y=250)
        winsound.Beep(1000,500)
    except:
        tmsg.showerror("error","Please input All details")
        return
def gen():
    print_data.place(x=360,y=250)
    root.geometry("850x500")
    data_scrolbar.pack(fill=Y,side=RIGHT)
    
    total = 0
    bill_text_lines = []  

    for prod, amt, qty in listss:
        subtotal = amt * qty
        total += subtotal
        
        bill_text_lines.append(f"\t Product: {prod}")
        bill_text_lines.append(f"\t Amount: {amt}")
        bill_text_lines.append(f"\t Quantity: {qty}")
        bill_text_lines.append(f"\t Subtotal: {subtotal}")
        bill_text_lines.append("")  

    bill_text_lines.append(f"\t Grand Total: {total}")

    
    data_list.delete(0, END)  
    for line in bill_text_lines:
        
        data_list.insert(END, line)
    list_box.delete(0,END)


def recs():
        
    
        file = fd.asksaveasfilename(defaultextension="*.txt",filetypes=[("Text Files","*.txt")],title="SAVING")
        if file:
            with open(file, "w") as f:
                values = data_list.get(0,END)
                f.write(f"{date_lab.cget('text')}\n")
                f.write("----------------------------------\n")
                for item in values:
                    f.write(f"{item}\n")
            tmsg.showinfo("successfully",f"Records Successfully Saved at {file} ")
            root.destroy()
            return
        
        if not file:
            tmsg.showerror("error","Something Went Wrong")
            return           





product_name = Label(root,bg="#7FB1E3",text="Product Name: ",font=("lucida 13 bold"))
product_name.place(x=30,y=100)

pro_var = StringVar()
pro_ent = Entry(root,relief=RIDGE,bd=4,textvariable=pro_var,font=("lucida 15 bold"))
pro_ent.place(x=190,y=100)




ammount = Label(root,bg="#7FB1E3",text="Amount: ",font=("lucida 13 bold"))
ammount.place(x=30,y=150)



rs = Label(root,text="Rs",bg="#7FB1E3",font=('lucida 13 bold'))
rs.place(x=315,y=153)




amou_var = StringVar()
amou_ent = Entry(root,relief=RIDGE,bd=4,width=10,textvariable=amou_var,font=("lucida 15 bold"))
amou_ent.place(x=190,y=150)




quant = Label(root,bg="#7FB1E3",text="Quantity: ",font=("lucida 13 bold"))
quant.place(x=30,y=200)

quan_var = StringVar()
quan_ent = Entry(root,relief=RIDGE,bd=4,width=10,textvariable=quan_var,font=("lucida 15 bold"))
quan_ent.place(x=190,y=200)

add_item = Button(root,bg="blue",fg="white",relief=GROOVE,bd=4,text="ADD ITEMS",font=("lucida 13 bold"),command=add_data)
add_item.place(x=30,y=250)
root.bind('<Return>',add_data)



frame = Frame(root)
frame.place(x=30, y=300)

list_box = Listbox(frame, relief=RIDGE,bd=4, bg="#025874",fg="white", height=8, width=52, font=("lucida", 13, "bold"))
list_box.pack(side=LEFT, fill=BOTH)

main_scrollbar = Scrollbar(frame, command=list_box.yview)
main_scrollbar.pack(side=RIGHT, fill=Y)

list_box.config(yscrollcommand=main_scrollbar.set)


# 0C0C6B



gen_bill = Button(root,relief=GROOVE,bd=4,bg="blue",fg="white",text="GENERATE BILL",font=("lucida 13 bold"),command=gen)





data_list = Listbox(root,relief=RIDGE,bd=4,bg="#04A4E3",height=16,width=25,font=("lucida 13 bold"))
data_list.place(x=550,y=100)

data_scrolbar = Scrollbar(root,command=data_list.yview)

data_list.config(yscrollcommand=data_scrolbar.set)



bills_lab = Label(root,text="BILLS",bg="red",fg='white',width=21,font=("Algerian 13 bold"))
bills_lab.place(x=550,y=75)


save_records = Button(root,width=23,relief=GROOVE,bd=4,bg="blue",fg="white",text="SAVE RECORDS",font=("lucida 13 bold"),command=recs)
save_records.place(x=550,y=445)


print_data = Button(root,width=15,relief=GROOVE,bd=4,bg="blue",fg="white",text="PRINT",font=("lucida 13 bold"),command=printss)





root.mainloop()
