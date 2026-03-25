from tkinter import *
import tkinter.filedialog as filesss
from PyPDF2 import PdfMerger
import tkinter.messagebox as tmsg

import os
root = Tk()
root.geometry("300x300")
root.title("PDF MERGER")
root.config(bg="#0F592D")
root.resizable(False,False)

lists= []
pdf_path = []

def select():
    file = filesss.askopenfilenames(defaultextension=".pdf",filetypes=[("PDF","*.pdf")])
    
    for f in file:
        exact_name = os.path.basename(f)
        n = lists.append(exact_name)
        pdf_path.append(f)
        list_box.insert(END,exact_name)

def pdf_merge():
    file = filesss.asksaveasfilename(defaultextension=".pdf",filetypes=[("PDF Files", "*.pdf")])
    if file:
        merger = PdfMerger()
        for pdf in pdf_path:
            merger.append(pdf)
        merger.write(file)
        merger.close()
        tmsg.showinfo("success","successfully saved")
        root.destroy()

def clr():
    list_box.delete(END)


select_pdf_btn = Button(root,text="select pdf",font=("lucida 10 bold"),command=select)
select_pdf_btn.pack(pady=20)

merge_pdf_btn = Button(root,text="merge pdf",font=("lucida 10 bold"),command=pdf_merge)
merge_pdf_btn.pack(pady=10)

clear_btn = Button(root,text="clear list",font=("lucida 10 bold"),command=clr)
clear_btn.pack(pady=10)


list_box = Listbox(root,height=6,width=5,font=("lucida 10 bold"))
list_box.pack(side=BOTTOM,fill=X,padx=20,pady=20)


root.mainloop()
