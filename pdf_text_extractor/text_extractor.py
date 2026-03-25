from tkinter import *
import os
import tkinter.filedialog as fd
import pdfplumber
import tkinter.messagebox as tmsg
import threading
root = Tk()
root.title("PDF Text Extractor")
root.geometry("400x500")
root.resizable(False,False)


root.config(bg="#14708E")
main_lab = Label(root,bg="black",fg="white",text="PDF TEXT EXTRACTOR",font=("lucida 15 bold"))
main_lab.pack(fill=X)

strinngss=""




def upl():
    
    global strinngss
    
    file = fd.askopenfilename(filetypes=[("PDF FILE","*.pdf")],title="Select a pdf file",defaultextension="*.pdf")
    if file:
        
        text_area.delete(1.0,END)
        conv = os.path.basename(file)
        e1_var.set(conv)
        strinngss=file
        
        

def trans():
    global strinngss
    
    
    
    if e1_var.get() != "":
        root.geometry("700x500")
        scroll_bar.pack(side=RIGHT,fill=Y)
        with pdfplumber.open(strinngss) as pdf:
            for pages in pdf.pages:
                page_text = pages.extract_text()
                if page_text:
                    text_area.insert(END,page_text)
    else:
        tmsg.showerror("Something Went Wrong","First Select PDF")
        return

def copy():
    geting_data_from_textarea = text_area.get(1.0,END)
    root.clipboard_clear()
    root.clipboard_append(geting_data_from_textarea)
    tmsg.showinfo("copied","Sucessfully copied to clipboard")

def threadss():
    threading.Thread(target=trans,daemon=True).start()

select_pdf = Label(root,bg="#14708E",fg="white",text="upload pdf: ",font=('lucida 13 bold'))
select_pdf.pack(pady=20,anchor=W,padx=30)


f_frame = Frame(root,bg="#14708E")
f_frame.pack(pady=20,anchor=W,padx=30)

e1_var = StringVar()
e1_ent = Entry(root,bg="#8DF228",relief=SUNKEN,bd=3,width=25,textvariable=e1_var,font=('lucida 15 bold'))
e1_ent.pack(padx=30,anchor=W,pady=20)











text_area = Text(root,height=20,width=25,wrap='word',font=('lucida 12 bold'))
text_area.place(x=450,y=50)



scroll_bar = Scrollbar(root,command=text_area.yview)



text_area.config(yscrollcommand=scroll_bar.set)

select_pdf = Button(root,relief=GROOVE,bd=6,bg="#95FD93",text="SELECT PDF",font=('lucida 12 bold'),command=upl)
select_pdf.pack(padx=30,anchor=W,pady=10)


get_text = Button(root,relief=GROOVE,bd=6,bg="#9395FD",width=25,text="GET TEXT",font=('lucida 12 bold'),command=threadss)
get_text.pack(side=BOTTOM,pady=30,anchor=W,padx=30)



cpy_btn = Button(root,relief=GROOVE,bd=6,bg="#FD9395",width=22,text="COPY",font=("lucida 12 bold"),command=copy)
cpy_btn.place(x=450,y=450)

root.mainloop()
