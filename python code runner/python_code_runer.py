import tkinter as tk
import customtkinter as ctk
import sys
import io
import tkinter.filedialog as fd

import tkinter.simpledialog as sd
import tkinter.messagebox as tmsg



root = ctk.CTk()
root.geometry("500x600+50+50")
root.configure(fg_color="#D6D025")
root.title("Python Compiler")
root.resizable(False,False)

main_lab = tk.Label(root,text="PYTHON COMPILER",bg="#EA6B39",font="lucida 15 bold")
main_lab.pack(fill="x")


termi = 0


def term():
    out_text.configure(state="normal")
    global termi
    termi+=1
    out_text.delete(1.0,"end")
    inserting = f"\t\t\tTerminal {termi}\n"
    out_text.insert("end",inserting)
    out_text.configure(state="disable")








def fetch():
    global termi
    out_text.configure(state="normal")
    code = inp_text.get(1.0,"end").strip()


    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()

    
    def custom_input(prompt=""):
        # root.attributes("-topmost",True)

        return sd.askstring("input required",prompt)


    try:
        exec(code,{"input":custom_input})
    except Exception as e:
        print("error",e)

    sys.stdout = old_stdout
    output = redirected_output.getvalue()
    out_text.delete(1.0,"end")
    inserting = f"\t\t\tTerminal {termi}\n"
    out_text.insert("end",inserting)
    

    out_text.insert("end",output)
    out_text.configure(state="disable")
    

    


def clr():
    global termi
    out_text.configure(state="normal")
    inp_text.delete(1.0,"end")
    out_text.delete(1.0,"end")
    inserting = f"\t\t\tTerminal {termi}"
    out_text.insert("end",inserting)
    out_text.configure(state="disable")


def savee():
    getsss = inp_text.get(1.0,"end").strip()
    if getsss == "":
        return
    
    file = fd.asksaveasfilename(filetypes=[("python file","*.py")],defaultextension="*.py")
    if file:
        with open(file , "w") as f:
            data = inp_text.get(1.0,"end")
            content = f.write(data)
            
            tmsg.showinfo("sucess",f"File Saved at {file}")

def kil():
    global termi
    if termi > 0:
        termi-=1
        out_text.configure(state="normal")
        out_text.delete(1.0,"end")
        inserting = f"\t\t\tTerminal {termi}"
        out_text.insert("end",inserting)
        out_text.configure(state="disable")

def opennn():
    file = fd.askopenfilename(filetypes=[("python file","*.py")],defaultextension="*.py")
    if file:
        with open(file, "r") as f:
            content = f.read()
            inp_text.delete(1.0,"end")
            inp_text.insert("end",content)



input_lab = tk.Label(root,bg="#D6D025",text="input",font=('lucida 13 bold'))
input_lab.place(x=30,y=50)





inp_text = ctk.CTkTextbox(root,fg_color="#034D54",text_color="white",undo=True,corner_radius=10,width=430,wrap="word",font=("lucida", 13, "bold"))
inp_text.place(x=30,y=100)

out_lab = tk.Label(root,bg="#D6D025",text="Output",font=('lucida 13 bold'))
out_lab.place(x=30,y=330)

out_text = ctk.CTkTextbox(root,fg_color="black",text_color="white",corner_radius=10,width=430,wrap="word",font=("lucida", 13, "bold"))
out_text.place(x=30,y=370)


inserting = f"\t\t\tTerminal {termi}"
out_text.insert("end",inserting)
out_text.configure(state="disable")

btn = ctk.CTkButton(root,fg_color="#131BB4",hover_color="#50304C",text="run",width=50,font=("lucida",13,"bold"),command=fetch)
btn.place(x=410,y=50)


clear_btn = ctk.CTkButton(root,fg_color="#B4136C",hover_color="#A342E2",text="clear",width=50,font=("lucida",13,"bold"),command=clr)
clear_btn.place(x=350,y=50)

save_btn = ctk.CTkButton(root,fg_color="#A5241A",hover_color="#3F9F0F",text="save",width=50,font=("lucida",13,"bold"),command=savee)
save_btn.place(x=290,y=50)


open_btn = ctk.CTkButton(root,fg_color="#13B45B",hover_color="#08C6EC",text="open",text_color="black",width=50,font=("lucida",13,"bold"),command=opennn)
open_btn.place(x=230,y=50)





kill_term = ctk.CTkButton(root,hover_color="#D6D025",text_color="black",fg_color="#D6D025",width=20,text="\U0001F5D1",font=("lucida",28),command=kil)
kill_term.place(x=460,y=380)

add_term = ctk.CTkButton(root,hover_color="#D6D025",text_color="black",fg_color="#D6D025",width=20,text="➕",font=("lucida",20),command=term)
add_term.place(x=460,y=450)




root.mainloop()


