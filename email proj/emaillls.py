from tkinter import *
import smtplib 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("400x500")
root.title("Gmail Msg Sender")
root.config(bg="blue")
root.resizable(False,False)




def mail():
    
    to_value = To_var.get()
    subject = sub_var.get()
    messagee = message.get(1.0, END)

    if To_var.get() == "":
        tmsg.showerror("ERROR","Input Sender and reciever Email")
    msg = MIMEMultipart()
    
    msg['To'] = to_value
    msg['Subject'] = subject

   
    msg.attach(MIMEText(messagee, 'plain'))

    
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

  
    server.login("tahairfanansari@gmail.com", "ldfw vqwk wusa qilb")

    
    server.sendmail("tahairfanansari@gmail.com", to_value, msg.as_string())
    server.quit()
    tmsg.showinfo("SUCESS","sucessfully mail send")

    To_var.set("")
    sub_var.set("")
    message.delete(1.0, END) 


email_lab = Label(root,bg="black",fg="white",text="EMAIL",font=("lucida 25 bold"))
email_lab.pack(fill=X)





TO_lab = Label(root,bg="blue",fg="white",text="To: ",font=("lucida 15 bold"))
TO_lab.place(x=20,y=130)


To_var = StringVar()
To_ent = Entry(root,textvariable=To_var,font=("lucida 15 bold"))
To_ent.place(x=150,y=130)


sub_lab = Label(root,bg="blue",fg="white",text="Subject: ",font=("lucida 15 bold"))
sub_lab.place(x=20,y=180)


sub_var = StringVar()
sub_ent = Entry(root,textvariable=sub_var,font=("lucida 15 bold"))
sub_ent.place(x=150,y=180)


message_lab = Label(root,bg="blue",fg="white",text="Message: ",font=("lucida 15 bold"))
message_lab.place(x=20,y=230)

message = Text(root,font=("lucida 15 bold"),wrap="word",width=20,height=5)
message.place(x=150,y=230)


send_mail = Button(root,text="SEND MAIL",font=("lucida 10 bold"),width=45,command=mail)
send_mail.place(x=20,y=450)




root.mainloop()
