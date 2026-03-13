from tkinter import *
import tkinter.messagebox as tmsg
from tkinter import filedialog

root = Tk()
root.title("Untitled - Notepad")
root.geometry("500x600")

file = None




def on_closing():
    if text_area.edit_modified():
        ans = tmsg.askyesnocancel("Save", "Do you want to save changes before exiting?")
        if ans:
            file = filedialog.asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[("Text file", ".txt"), ("All Files", ".*")])
            f = open(file, "w")
            f.write(text_area.get(1.0, END))
            f.close()
            root.destroy()
        elif ans is None:
            return
        else: 
            root.destroy()
    else:
        root.destroy()



def cutfile():
    text_area.event_generate(("<<Cut>>"))


def copyfile():
    text_area.event_generate(("<<Copy>>"))

def pastefile():
    text_area.event_generate(("<<Paste>>"))

def abt():
    tmsg.showinfo("About", "This GUI Notepad - Mabe By Taha")

def newfile():
    text_area.delete(1.0, END)

def openfile():
    file = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("All Files", ".*"), ("Text file", ".txt")])
    f = open(file,)
    text_area.insert(1.0, f.read())
    f.close()
    text_area.config(wrap=WORD)
    


def savefile():
    global file

    text_content = text_area.get(1.0,END)


    if not text_content:
        tmsg.showinfo("Error", "Enter Some Text To Save")
        return

    if file is None:
        file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text file", ".txt"), ("All Files", ".*")])
        
    if not file:
        return
        
    with open(file, "w") as f:
        f.write(text_content)
        f.close()
    tmsg.showinfo("Success", "File saved successfully")
    
    # f = open(file, "w")
    # f.write(text_area.get(1.0, END))
    # f.close()


Menubar = Menu(root)
file_menu = Menu(Menubar, tearoff=0)
file_menu.add_command(label="New", command=newfile)
file_menu.add_command(label="open", command= openfile)
file_menu.add_separator()
file_menu.add_command(label="save", command= savefile)
file_menu.add_command(label="Exit", command=quit)

Menubar.add_cascade(label="File", menu=file_menu)

edit_menu = Menu(Menubar, tearoff=0)
edit_menu.add_command(label="Cut", command=cutfile)
edit_menu.add_command(label="Copy", command=copyfile)
edit_menu.add_command(label="Paste", command=pastefile)
Menubar.add_cascade(label="Edit", menu=edit_menu)


about_menu = Menu(Menubar, tearoff=0)
about_menu.add_command(label="About", command=abt)
Menubar.add_cascade(label="Help", menu=about_menu)



root.config(menu=Menubar)

scroll = Scrollbar(root)
scroll.pack(side=RIGHT, fill=Y)
text_area = Text(root , font=("lucida", 13), yscrollcommand=scroll.set, wrap=WORD)
text_area.pack(expand=True, fill=BOTH)
scroll.config(command=text_area.yview)

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
