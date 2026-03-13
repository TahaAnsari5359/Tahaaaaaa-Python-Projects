from tkinter import *
import tkinter.messagebox as tmsg
import random
root = Tk()
root.geometry("400x500")
root.title("Number Guessing Game")
root.config(bg="blue")
l1 = Label(root,bg="lightblue",text="NUMBER GUESSING GAME",font="lucida 15 bold")
l1.pack(fill=X)

num = random.randint(1,100)
guess = 0


def gett():
    global num, guess
    try:
        guesss = int(guess_ent.get())
    except:
        tmsg.showerror("ERROR","Enter a number")
        return

    guess+=1

    
    if guesss>num:
        info_lab.config(text="Please Enter a Lower Number")
                
            
    elif guesss <num:
        info_lab.config(text="Please Enter a Higher Number")

    else:
        info_lab.config(text=f"You guessed the number {num} in {guess} guesses!")
        tmsg.showinfo("SUCCESS",f"You guessed the number {num} in {guess} guesses!")
        asking = tmsg.askyesno("GAME","Are You Want To Play Again ?")
        
        if asking == True:
            
            num = random.randint(1, 100)  
            guess = 0                     
            guess_var.set("")              
        else:
            root.destroy()

    guess_var.set("")
    

guess_var = StringVar()
guess_ent = Entry(root,textvariable=guess_var,font=("lucida 15 bold"))
guess_ent.pack(pady=20)


guess_btn = Button(root,text="GUESS",font=("lucida 13 bold"),width=20,command=gett)
guess_btn.pack()


info_lab = Label(root,bg="blue",font=("lucida 15 bold"))
info_lab.pack(pady=20)










root.mainloop()
