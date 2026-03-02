from tkinter import *
import tkinter.messagebox as tmsg
import random
import winsound

root = Tk()
root.geometry("400x400")
root.config(bg="red")
root.title("VIRUS GAME")
score = 0


r1 = None  
r2 = None  
r3 = None  



def strt():
    global r1, r2, r3, timer, score

  
    score = 0
    timer = 30
    score_lab.config(text="SCORE: 0")
    timer_lab.config(text=str(timer))

    game()                    
    r2 = root.after(2000, desc_score)  
    r1 = root.after(1000, stopwatch)














def game():
    global r3
    b1.config(state="normal")
    x = random.randint(0, 300)
    y = random.randint(0, 300)
    b1.place(x=x, y=y)
    r3 = root.after(1000, game)

def click_me():
    
    global score
    score += 1

    b1.config(state="disable")
    score_lab.config(text=f"SCORE: {score}")

def desc_score():

    global score, r2
    if score > 0:
        score -= 1
        score_lab.config(text=f"SCORE: {score}")
    r2 = root.after(2000, desc_score)  

import os, sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for PyInstaller and dev """
    try:
        base_path = sys._MEIPASS  # For PyInstaller
    except Exception:
        base_path = os.path.dirname(os.path.abspath(__file__))  # For VS Code
    return os.path.join(base_path, relative_path)


img_path = resource_path("virus.png")
img = PhotoImage(file=img_path)

resizeimg = img.subsample(7, 7)
b1 = Button(root, text="CLICK", borderwidth=0,highlightthickness=0, image=resizeimg, bg="red", fg="white", command=click_me)

score_lab = Label(root, text="SCORE: 0", bg="red",fg="white", font=("lucida 15 bold"))
score_lab.place(x=30, y=350)






def stopwatch():
    global timer, r1, r2, r3
    timer -= 1
    timer_lab.config(text=timer)
    if timer == 0:
        b1.destroy()
        
        if r1 is not None:
            root.after_cancel(r1)
        if r2 is not None:
            root.after_cancel(r2)
        if r3 is not None:
            root.after_cancel(r3)
        for i in range(5):
            winsound.Beep(1000,300)
        tmsg.showinfo("RESULT", f"Times Up! Your Score {score}")
        
        root.destroy()
        
    r1 = root.after(1000, stopwatch)

timer_lab = Label(root,bg="red",fg="white", font=("lucida 20 bold"))
timer_lab.place(x=350, y=20)



strt_btn = Button(root,text="START",font=("lucida 15 bold"),command=strt)
strt_btn.place(x=280,y=340)


root.mainloop()
