import tkinter as tk
import customtkinter as ctk
from tkinter import StringVar
import requests
import random
import urllib.parse
from PIL import Image,ImageTk
from io import BytesIO
import threading
import time
import tkinter.messagebox as tmsg
import tkinter.filedialog as fd
import random



root = ctk.CTk()
root.resizable(False,False)
root.title("AI image generator")
root.geometry("700x620")
root.configure(fg_color="#F2E858")
main_lab = tk.Label(root,bg="black",fg="white",text="AI IMAGE GENERATOR",font=('lucida 15 bold'))
main_lab.pack(fill="x")


img = None


def gen():
    

    global img
    
    


    prompt = prompt_var.get()



    safe_prompt = urllib.parse.quote(prompt)
    
    seed = random.randint(1, 999999)

    url = f"https://image.pollinations.ai/prompt/{safe_prompt}?seed={seed}"
    print(url)

    response = requests.get(url)

    img = Image.open(BytesIO(response.content))
        
    max_size = (320, 320)
    img.thumbnail(max_size)
    photo = ImageTk.PhotoImage(img)

    img_lab.config(image=photo)
    img_lab.image = photo

    bar.config(text="Image Generated succesfully",fg="lime")

    gen_img.configure(state="normal")
    save_img.configure(state="normal")
    rand_img.configure(state="normal")
    clear_img.configure(state="normal")



        

def status_bar():

    prompt = prompt_var.get()

    if prompt == "":
        tmsg.showerror("failed","Error Image Cannot be Generated")
        return

    gen_img.configure(state="disabled")
    save_img.configure(state="disabled")
    rand_img.configure(state="disabled")
    clear_img.configure(state="disabled")

    def step2():
        bar.config(text="generating image..", fg="red")
        root.after(2000, step3)

    def step3():
        bar.config(text="generating image...", fg="red")
        root.after(2000, step4)

    def step4():
        bar.config(text="generating image....", fg="red")
        root.after(2000, step5)

    def step5():
        bar.config(text="please wait..")
        root.after(2000, step6)

    def step6():
        bar.config(text="processing..")
        root.after(2000, step7)

    def step7():
        bar.config(text="rendering image..")
        root.after(2000, step8)

    def step8():
        bar.config(text="preparing final output")
        root.after(2000, step9)

    def step9():
        bar.config(text="almost done")
        root.after(2000, threadings)  

    bar.config(text="generating image.", fg="red")
    root.after(2000, step2)


def threadings():
    threading.Thread(target=gen,daemon=True).start()


def saves():
    global img
    if not img:
        tmsg.showerror("error","SomeThing Went Wrong")
        return
    

    file = fd.asksaveasfilename(filetypes=[("PNG file","*.png"),("JPG file","*.jpg"),("ALLL files","*.*")],title="SAVE IMAGE",defaultextension="*.png")
    
    

    if file:
        img.save(file)
        tmsg.showinfo("sucessfully",f"Image Saved Succesfully at {file}")
        asks = tmsg.askyesno("Askings","Want To Generate More Images")
        if asks == True:
            img_lab.config(image="")
            bar.config(text="Input Prompt",fg="red")
            prompt_var.set("")
        else:
            root.destroy()

def clr():
    prompt_var.set("")
    img_lab.config(image="",bd=1,relief="flat")
    bar.config(text="Input Prompt",fg="red")

def randomm():
    # prompt_var.set("")
    all_prompt = "Neon city at night with flying cars.", "Cute robot holding a glowing flower.","Fantasy castle floating in the clouds.","Samurai standing in the rain.","A fox wearing a tiny wizard hat.","Astronaut sitting on a moon rock.","Mystical forest with glowing plants.","Retro diner with neon signs.","Dragon flying over snowy mountains.","Minimalist modern living room interior."
    rand_prom = random.choice(all_prompt)
    prompt_var.set(rand_prom)



prompt_var = StringVar()
prompt_lab = ctk.CTkLabel(root,text="Enter Prompt: ",font=('lucida',15,"bold"))
prompt_lab.place(x=130,y=50)
prompt_enter = ctk.CTkEntry(root,border_width=3,fg_color="#73EA83",border_color="#444",height=30,width=450,textvariable=prompt_var,font=("lucida",13,"bold"))
prompt_enter.pack(pady=60)






img_lab = tk.Label(root,bg="#F2E858")
img_lab.pack(padx=20)






bar = tk.Label(root,bg="black",fg="#FF0000",text="Input Prompt",font=("lucida 12 bold"))
bar.pack(anchor="e",fill="x",side="bottom")

btn_f = tk.Frame(root,bg="#F2E858")
btn_f.pack(side="bottom")








clear_img = ctk.CTkButton(btn_f,width=150,fg_color="#134D2D",hover_color="#09757D",text="CLEAR",font=("lucida",15,"bold"),command=clr)
clear_img.pack(pady=20,side="left",padx=10)




gen_img = ctk.CTkButton(btn_f,width=150,fg_color="indigo",hover_color="#09757D",text="GENERATE",font=("lucida",15,"bold"),command=status_bar)
gen_img.pack(pady=20,side="left",padx=10)


save_img = ctk.CTkButton(btn_f,width=150,fg_color="#6B1219",hover_color="#09757D",text="SAVE",font=("lucida",15,"bold"),command=saves)
save_img.pack(pady=20,side="right",padx=10)

rand_img = ctk.CTkButton(btn_f,width=150,fg_color="#6A580E",hover_color="#09757D",text="RANDOM PROMPT",font=("lucida",15,"bold"),command=randomm)
rand_img.pack(pady=20,side="right",padx=10)


root.mainloop()



