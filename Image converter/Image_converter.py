from tkinter import *
import threading
import time
import tkinter.filedialog as fd
from PIL import Image, ImageTk
root = Tk()
root.geometry("600x500")
root.config(bg="#2C4B4A")
root.title("Image Converter")

main_lab = Label(root,text="IMAGE CONVERTER",bg="black",fg="white",font=("lucida 15 bold"))
main_lab.pack(fill=X)




def choose():
    opt_1 = exten_var.get()
    opt_2 = n_exten_var.get()
    datass = e1_var.get()

    if datass != "":
        
        if opt_1 == "PNG" and opt_2 == "JPG":
            
            file = fd.askopenfilename(filetypes=[
            ("PNG", "*.png")
            ])
            if not file:
                return 

            data = Image.open(file)

            if data.mode == "RGBA":
                data = data.convert("RGB")

            select_file_btn.config(state='disable')
            time.sleep(1)
            data_lab.update()
            data_lab.config(text="WAIT UNTIL PROCESS FINISH",relief=RIDGE,bd=5,bg="red",fg="white")
            time.sleep(3)
            data_lab.update()


            data_lab.config(text="IMPORTING IMAGE..",relief=RIDGE,bd=5,bg="red",fg="white")
            time.sleep(3)
            data_lab.update()

            data_lab.config(text="SAVING IMAGE......",relief=RIDGE,bd=5,bg="red",fg="white")
            time.sleep(3)
            data_lab.update()


            resized = data.resize((150,150))
            imge = ImageTk.PhotoImage(resized)

            imge_lab.config(image=imge,relief=GROOVE,bd=5)
            imge_lab.image = imge

            time.sleep(5)
            data_lab.update()



            data_lab.config(text="SELECT LOCATION",relief=RIDGE,bd=5,bg="red",fg="white")
            time.sleep(2)
            data_lab.update()

            save_loc = fd.asksaveasfilename(initialfile=datass)

            
            if save_loc:
                data.save(f"{save_loc}.jpg")
                data_lab.config(text=f"{datass} SAVED SUCCESSFULLY",relief=RIDGE,bd=5,bg="lime",fg="black")

                e1_var.set("")
                imge_lab.config(relief=FLAT,bd=0)
                select_file_btn.config(state='normal')
                


        elif opt_1 == "JPG" and opt_2 == "PNG":
            file = fd.askopenfilename(filetypes=[
            ("JPG", "*.jpg")
            ])
            if not file:
                return 

            data = Image.open(file)
            select_file_btn.config(state='disable')
            time.sleep(1)
            data_lab.update()
            data_lab.config(text="WAIT UNTIL PROCESS FINISH",relief=RIDGE,bd=5,bg="red",fg="white")
            time.sleep(3)
            data_lab.update()


            data_lab.config(text="IMPORTING IMAGE..",relief=RIDGE,bd=5,bg="red",fg="white")
            time.sleep(3)
            data_lab.update()

            data_lab.config(text="SAVING IMAGE......",relief=RIDGE,bd=5,bg="red",fg="white")
            time.sleep(3)
            data_lab.update()


            resized = data.resize((150,150))
            imge = ImageTk.PhotoImage(resized)

            imge_lab.config(image=imge,relief=GROOVE,bd=5)
            imge_lab.image = imge

            time.sleep(5)
            data_lab.update()


            data_lab.config(text="SELECT LOCATION",relief=RIDGE,bd=5,bg="red",fg="white")
            time.sleep(2)
            data_lab.update()

            save_loc = fd.asksaveasfilename(initialfile=datass)

            
            if save_loc:
                data.save(f"{save_loc}.png")
                data_lab.config(text=f"{datass} SAVED SUCCESSFULLY",relief=RIDGE,bd=5,bg="lime",fg="black")
                e1_var.set("")
                imge_lab.config(relief=FLAT,bd=0)
                select_file_btn.config(state='normal')
        else:
            data_lab.config(text="ERROR SOMETHING WENT WRONG",bg="red",fg="white")
    else:
        data_lab.config(text="INPUT FILE NAME",bg="red",fg="white")


    
    
def threadss(Event=None):
   threading.Thread(target=choose, daemon=True).start()
    
   






name_ent_f = Frame(root,bg="#2C4B4A")
name_ent_f.pack()

name_lab = Label(name_ent_f,bg="#2C4B4A",fg="white",text="Enter File Name: ",font=("lucida 15 bold"))
name_lab.pack(side=LEFT)


e1_var = StringVar()
e1_ent = Entry(name_ent_f,width=20,relief=SUNKEN,bd=3,justify=CENTER,textvariable=e1_var,font=("lucida 15 bold"))
e1_ent.pack(pady=20)

f_vars = Frame(root,bg="#2C4B4A")
f_vars.pack()


n_exten_var = StringVar()
n_exten_vales = "PNG","JPG"
n_exten_var.set("SELECT FILE FORMATS")
n_options = OptionMenu(f_vars,n_exten_var,*n_exten_vales)
n_options.pack(side=RIGHT,padx=40)

n_options.config(font=("lucida 10 bold"),bg="purple",fg="white")



exten_var = StringVar()
exten_vales = "PNG","JPG"
exten_var.set("SELECT FILE FORMATS")

options = OptionMenu(f_vars,exten_var,*exten_vales)
options.pack(padx=40)
options.config(font=("lucida 10 bold"),bg="purple",fg="white")







data_lab = Label(root,font=("lucida 15 bold"),bg="#2C4B4A")
data_lab.pack(pady=40,fill=X)


imge_lab = Label(root,bg="#2C4B4A")
imge_lab.pack()


select_file_btn = Button(root,width=25,relief=GROOVE,bd=5,bg="#177B64",fg="white",text="CHOOSE FILE",font=("lucida 13 bold"),command=threadss)
select_file_btn.pack(side=BOTTOM,pady=30)
root.bind('<Return>',threadss)


root.mainloop()



#-------------------------------------------------Different Conmcept-----------------




# def choose():
#     format_choice = exten_var.get().upper()


#     file = fd.askopenfilename(filetypes=[
#         ("PNG", "*.png"),
#         ("JPEG", "*.jpeg"),
#         ("JPG", "*.jpg")
#     ])
#     if not file:
#         return 

#     data = Image.open(file)


#     save_path = fd.asksaveasfilename(filetypes=[
#         ("PNG", "*.png"),
#         ("JPEG", "*.jpeg"),
#         ("JPG", "*.jpg")
#     ], defaultextension=f".{format_choice.lower()}")

#     if not save_path:
#         return  

   
#     if format_choice in ["JPG", "JPEG"] and data.mode == "RGBA":
#         data = data.convert("RGB")


#     data.save(save_path, format=format_choice)
#     data_lab.config(text=f"✅ Image saved as {save_path}")

