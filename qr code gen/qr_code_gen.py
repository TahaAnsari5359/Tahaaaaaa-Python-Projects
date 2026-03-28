from tkinter import * 
import qrcode
from PIL import Image, ImageTk
import tkinter.messagebox as tmsg
from tkinter import filedialog
qr_image = None

root = Tk()
root.geometry("700x500")
root.configure(bg="Red")

root.title("QRCODE Generator")


def qrgen():
    global qr_image
    name = name_var.get()
    url = url_var.get()
    if name == "" and url == "":
        tmsg.showinfo("Error", "Please Enter Deatils")
    else:
        gen = qrcode.make(url)
        qr_path = f"{name} - QrCode.png"
        gen.save(qr_path)
        
        
    



        image_display = Image.open(qr_path)
        tk_img = ImageTk.PhotoImage(image_display)

        image_Label.config(image=tk_img)
        image_Label.image = tk_img
        tmsg.showinfo("Sucess", "Sucessfully Saved")
        
def clr():
    name_var.set("")
    url_var.set("")
    image_Label.destroy()


qrcode_label = Label(root, bg="Black",  fg="white", text="Qr Code Generator", font=("lucida 25 bold"))
qrcode_label.pack(fill=X)


name_lab = Label(root, bg="Red", text="Enter Name:-", font=("lucida 15 bold"))
name_lab.place(x=50, y=100)
name_var = StringVar()
name_entry = Entry(root, textvariable=name_var,width=20, font=("lucida 15"))
name_entry.place(x=50, y=150)



url_lab = Label(root, bg="Red", text="Enter Url:-", font=("lucida 15 bold"))
url_lab.place(x=50, y=200)
url_var = StringVar()
url_entry = Entry(root, textvariable=url_var,width=20, font=("lucida 15"))
url_entry.place(x=50, y=250)


quit_btn = Button(root, bg="black", fg="white", text="Generate", width=30, font=("lucida 10 bold"), command=qrgen)
quit_btn.place(x=50, y=350)



generate_btn = Button(root, bg="black", fg="white", text="Clear", width=30, font=("lucida 10 bold"), command=clr)
generate_btn.place(x=50, y=400)




clr_btn = Button(root, bg="black", fg="white", text="Quit", width=30, font=("lucida 10 bold"), command=root.destroy)
clr_btn.place(x=50, y=450)





image_Label = Label(root, bg="Red")
image_Label.place(x=330, y=130)


root.mainloop()
