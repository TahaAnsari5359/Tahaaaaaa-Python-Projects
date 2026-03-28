from spellchecker import SpellChecker
import tkinter as tk
import customtkinter as ctk
from tkinter import StringVar
import tkinter.messagebox as tmsg


root = ctk.CTk()
root.geometry("300x400")
root.configure(fg_color="#0E23E3")
ctk.set_default_color_theme("blue") 





mainn_lab = ctk.CTkLabel(root,fg_color="white",text="SPELL CHECK TOOL",font=("lucida",15,"bold"))
mainn_lab.pack(fill="x")


def chek(event=None):
    
    
    gets = e1_var.get()
    spell = SpellChecker()
    corrected = spell.correction(gets)

    
    
    if e1_var.get() == "":
        tmsg.showerror("some thing went wronnng","Input a Valid Word")

    else:

        if gets == corrected:
            res_lab.config(text="word is correct",bg="lime",fg="black")
            res2_lab.config(bg="#0E23E3",fg="#0E23E3")
        else:
            res_lab.config(text=f"wrong word",bg="red",fg="white")
            res2_lab.config(text=f"corrected word: {corrected}",bg="lime",fg="black")
    






enter_words_lab = tk.Label(root,bg="#0E23E3",fg="white",text="Enter Words: ",font=('lucida 13 bold'))
enter_words_lab.pack(pady=20,anchor="w",padx=50)



e1_var = StringVar()
words = ctk.CTkEntry(root,fg_color="#1ED2B0",corner_radius=10,placeholder_text="Enter Words",width=200,justify="center",textvariable=e1_var,font=("lucida",13,"bold"))
words.pack(pady=10)
 
res_lab = tk.Label(root,bg="#0E23E3",font=("lucida 14 bold"))
res_lab.pack(pady=20,fill="x")

res2_lab = tk.Label(root,bg="#0E23E3",font=("lucida 14 bold"))
res2_lab.pack(fill="x")


check_btn = tk.Button(root,bd=5,relief="ridge",bg="#932C06",fg="white",text="CHECK SPELLING",font=("lucida 10 bold"),command=chek)
check_btn.pack(side="bottom",pady=20)
root.bind('<Return>',chek)


root.mainloop()


