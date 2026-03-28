from tkinter import *
from tkinter import messagebox as tmsg

root = Tk()
root.geometry("700x500")
root.config(bg="#F57927")
root.title("Quiz Game")
root.resizable(False,False)

score = 0

def q2():
    about_btn.destroy()
    var.set("")
    WandR.config(bg="#F57927", text="")
    check_btn.config(state="normal", command=chk2)
    quiz_game_lab.config(text="Who wrote the play Romeo and Juliet?", font=("lucida 20 bold"))
    r1.config(text="A. William Wordsworth", bg="#F57927",value="William Wordsworth", variable=var, font=("lucida 15 bold"))
    r1.place(x=30, y=150)
    r2.config(text="B. Leo Tolstoy", value="Leo Tolstoy",bg="#F57927", variable=var, font=("lucida 15 bold"))
    r2.place(x=30, y=200)
    r3.config(text="C. William Shakespeare", bg="#F57927",value="William Shakespeare", variable=var, font=("lucida 15 bold"))
    r3.place(x=30, y=250)
    r4.config(text="D. Charles Dickens",bg="#F57927", value="Charles Dickens", variable=var, font=("lucida 15 bold"))
    r4.place(x=30, y=300)
    start_btn.config(command=q3, state="disabled")

def q3():
    about_btn.destroy()
    var.set("")
    WandR.config(bg="#F57927", text="")
    check_btn.config(state="normal", command=chk3)
    quiz_game_lab.config(text="What is the capital city of Japan?", font=("lucida 20 bold"))
    r1.config(text="A. Seoul", value="Seoul",bg="#F57927", variable=var, font=("lucida 15 bold"))
    r1.place(x=30, y=150)
    r2.config(text="B. Beijing", value="Beijing", bg="#F57927",variable=var, font=("lucida 15 bold"))
    r2.place(x=30, y=200)
    r3.config(text="C. Tokyo", value="Tokyo", bg="#F57927",variable=var, font=("lucida 15 bold"))
    r3.place(x=30, y=250)
    r4.config(text="D. Kyoto", value="Kyoto",bg="#F57927", variable=var, font=("lucida 15 bold"))
    r4.place(x=30, y=300)
    start_btn.config(command=q4, state="disabled")

def q4():
    about_btn.destroy()
    var.set("")
    WandR.config(bg="#F57927", text="")
    check_btn.config(state="normal", command=chk4)
    quiz_game_lab.config(text="What Does CPU Stand for?", font=("lucida 20 bold"))
    r1.config(text="A. Central processing unit",bg="#F57927",value="Central processing unit", variable=var, font=("lucida 15 bold"))
    r1.place(x=30, y=150)
    r2.config(text="B. central power unit",bg="#F57927", value="central power unit", variable=var, font=("lucida 15 bold"))
    r2.place(x=30, y=200)
    r3.config(text="C. Control process utility",bg="#F57927", value="control process utility", variable=var, font=("lucida 15 bold"))
    r3.place(x=30, y=250)
    r4.config(text="D. computer processing user",bg="#F57927",value="computer processing user", variable=var, font=("lucida 15 bold"))
    r4.place(x=30, y=300)
    start_btn.config(command=q5, state="disabled")

def q5():

    about_btn.destroy()
    var.set("")
    WandR.config(bg="#F57927", text="")
    check_btn.config(state="normal", command=chk5)
    quiz_game_lab.config(text="Which is the largest ocean on earth?", font=("lucida 20 bold"))
    r1.config(text="A. Atlantic Ocean",bg="#F57927", value="Atlantic Ocean", variable=var, font=("lucida 15 bold"))
    r1.place(x=30, y=150)
    r2.config(text="B. Indian ocean",bg="#F57927", value="Indian ocean", variable=var, font=("lucida 15 bold"))
    r2.place(x=30, y=200)
    r3.config(text="C. Arctic ocean",bg="#F57927", value="Arctic ocean", variable=var, font=("lucida 15 bold"))
    r3.place(x=30, y=250)
    r4.config(text="D. Pacific ocean",bg="#F57927", value="Pacific ocean", variable=var, font=("lucida 15 bold"))
    r4.place(x=30, y=300)
    start_btn.config(command=q6, state="disabled")

def q6():
    about_btn.destroy()
    var.set("")
    WandR.config(bg="#F57927", text="")
    check_btn.config(state="normal", command=chk6)
    quiz_game_lab.config(text="Water boils at what temperature at sea level?", font=("lucida 20 bold"))
    r1.config(text="A. 90° C",bg="#F57927", value="90° C", variable=var, font=("lucida 15 bold"))
    r1.place(x=30, y=150)
    r2.config(text="B. 100° C",bg="#F57927", value="100° C", variable=var, font=("lucida 15 bold"))
    r2.place(x=30, y=200)
    r3.config(text="C. 80° C", bg="#F57927",value="80° C", variable=var, font=("lucida 15 bold"))
    r3.place(x=30, y=250)
    r4.config(text="D. 110° C",bg="#F57927", value="110° C", variable=var, font=("lucida 15 bold"))
    r4.place(x=30, y=300)
    start_btn.config(command=q7, state="disabled")

def q7():
    about_btn.destroy()
    var.set("")
    WandR.config(bg="#F57927", text="")
    check_btn.config(state="normal", command=chk7)
    quiz_game_lab.config(text="Who Directed the movie Avatar?", font=("lucida 20 bold"))
    r1.config(text="A. Steven Spielberg",bg="#F57927", value="Steven Spielberg", variable=var, font=("lucida 15 bold"))
    r1.place(x=30, y=150)
    r2.config(text="B. James Cameron",bg="#F57927", value="James Cameron", variable=var, font=("lucida 15 bold"))
    r2.place(x=30, y=200)
    r3.config(text="C. Christopher Nolan",bg="#F57927", value="Christopher Nolan", variable=var, font=("lucida 15 bold"))
    r3.place(x=30, y=250)
    r4.config(text="D. Peter Jackson",bg="#F57927", value="Peter Jackson", variable=var, font=("lucida 15 bold"))
    r4.place(x=30, y=300)
    start_btn.config(command=q8, state="disabled")

def q8():
    about_btn.destroy()
    var.set("")
    WandR.config(bg="#F57927", text="")
    check_btn.config(state="normal", command=chk8)
    quiz_game_lab.config(text="What is the name of the main character in Minecraft?", font=("lucida 20 bold"))
    r1.config(text="A. Alex",bg="#F57927", value="Alex", variable=var, font=("lucida 15 bold"))
    r1.place(x=30, y=150)
    r2.config(text="B. Steve",bg="#F57927", value="Steve", variable=var, font=("lucida 15 bold"))
    r2.place(x=30, y=200)
    r3.config(text="C. Herobrine",bg="#F57927", value="Herobrine", variable=var, font=("lucida 15 bold"))
    r3.place(x=30, y=250)
    r4.config(text="D. Notch",bg="#F57927", value="Notch", variable=var, font=("lucida 15 bold"))
    r4.place(x=30, y=300)
    start_btn.config(command=q9, state="disabled")

def q9():
    about_btn.destroy()
    var.set("")
    WandR.config(bg="#F57927", text="")
    check_btn.config(state="normal", command=chk9)
    quiz_game_lab.config(text="What is the value of π (pi)?", font=("lucida 20 bold"))
    r1.config(text="A. 3.41",bg="#F57927", value="3.41", variable=var, font=("lucida 15 bold"))
    r1.place(x=30, y=150)
    r2.config(text="B. 2.14",bg="#F57927", value="2.14", variable=var, font=("lucida 15 bold"))
    r2.place(x=30, y=200)
    r3.config(text="C. 3.14",bg="#F57927", value="3.14", variable=var, font=("lucida 15 bold"))
    r3.place(x=30, y=250)
    r4.config(text="D. 4.13",bg="#F57927", value="4.13", variable=var, font=("lucida 15 bold"))
    r4.place(x=30, y=300)
    start_btn.config(command=q10, state="disabled")

def q10():
    about_btn.destroy()
    var.set("")
    WandR.config(bg="#F57927", text="")
    check_btn.config(state="normal", command=chk10)
    quiz_game_lab.config(text="Which planet is known as the red planet?", font=("lucida 20 bold"))
    r1.config(text="A. Mars", value="Mars",bg="#F57927", variable=var, font=("lucida 15 bold"))
    r1.place(x=30, y=150)
    r2.config(text="B. Venus", value="Venus",bg="#F57927", variable=var, font=("lucida 15 bold"))
    r2.place(x=30, y=200)
    r3.config(text="C. Earth", value="Earth",bg="#F57927", variable=var, font=("lucida 15 bold"))
    r3.place(x=30, y=250)
    r4.config(text="D. Saturn", value="Saturn",bg="#F57927", variable=var, font=("lucida 15 bold"))
    r4.place(x=30, y=300)
    start_btn.config(text="RESULT", command=result, state="disabled")

def result():
    about_btn.destroy()
    start_btn.destroy()
    WandR.config(bg="#F57927", text="")
    quiz_game_lab.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    check_btn.destroy()

    l1 = Label(root, bg="black", fg="white", text="RESULT", font=("lucida 35 bold"))
    l1.pack(fill=X)

    game_finish = Label(root, bg="black", fg="white", text="GAME FINISH! CONGRATULATIONS 🎉", font=("lucida 25 bold"))
    game_finish.pack(pady=30, fill=X)

    score_lab = Label(root, text="SCORE:", bg="#F57927",font=("lucida 15 bold"))
    score_lab.place(x=40, y=200)

    got_score = Label(root, text=f"YOU GOT SCORE: {score}/10 ",bg="#F57927", font=("lucida 15 bold"))
    got_score.place(x=40, y=250)



def check_answer(correct_answer):
    global score
    selected = var.get()
    if not selected:
        tmsg.showwarning("WARNING", "Please select an option!")
        return 
    if selected == correct_answer:
        WandR.config(bg="lime", text="CORRECT ✅")
        score += 1
    else:
        WandR.config(bg="red", text="WRONG ❌")
    WandR.place(x=1, y=350, width=700)
    check_btn.config(state="disabled")
    start_btn.config(state="normal")
    return True

def chk():
    
    r2.config(bg="lime")
    if check_answer("Mercury"):
        start_btn.config(command=q2)

def chk2():
    r3.config(bg="lime")
    if check_answer("William Shakespeare"):
        start_btn.config(command=q3)

def chk3():
    r3.config(bg="lime")
    if check_answer("Tokyo"):
        start_btn.config(command=q4)

def chk4():
    r1.config(bg="lime")
    if check_answer("Central processing unit"):
        start_btn.config(command=q5)

def chk5():
    r4.config(bg="lime")
    if check_answer("Pacific ocean"):
        start_btn.config(command=q6)

def chk6():
    r2.config(bg="lime")
    if check_answer("100° C"):
        start_btn.config(command=q7)

def chk7():
    r2.config(bg="lime")
    if check_answer("James Cameron"):
        start_btn.config(command=q8)

def chk8():
    r2.config(bg="lime")
    if check_answer("Steve"):
        start_btn.config(command=q9)

def chk9():
    r3.config(bg="lime")
    if check_answer("3.14"):
        start_btn.config(command=q10)

def chk10():
    r1.config(bg="lime")
    if check_answer("Mars"):
        start_btn.config(command=result)

def start():
    global score
    score = 0
    about_btn.destroy()
    var.set("")
    WandR.config(bg="#F57927", text="")
    quiz_game_lab.config(text="What is the smallest planet in our Solar System?", font=("lucida 20 bold"))
    r1.config(text="A. Earth", value="Earth", variable=var, font=("lucida 15 bold"))
    r1.place(x=30, y=150)
    r2.config(text="B. Mercury", value="Mercury", variable=var, font=("lucida 15 bold"))
    r2.place(x=30, y=200)
    r3.config(text="C. Mars", value="Mars", variable=var, font=("lucida 15 bold"))
    r3.place(x=30, y=250)
    r4.config(text="D. Venus", value="Venus", variable=var, font=("lucida 15 bold"))
    r4.place(x=30, y=300)
    check_btn.config(bg="blue", fg="white", text="CHECK", font=("lucida 15 bold"), command=chk)
    check_btn.place(x=560, y=415)
    start_btn.config(text="NEXT >>", command=q2, state="disabled")


def abt():
    tmsg.showinfo("about","Quiz Game - Created By Taha")

quiz_game_lab = Label(root, bg="#F57927", text="QUIZ GAME \n Press Start Button", font=("Algerian 35 underline bold"))
quiz_game_lab.pack(pady=50)

start_btn = Button(root, text="START GAME",bg="black",fg="white", font=("Algerian 25 bold"), command=start)
start_btn.pack(side=BOTTOM, pady=30, padx=30, fill=X)

var = StringVar()
var.set(None)
r1 = Radiobutton(root, bg="#F57927")
r2 = Radiobutton(root, bg="#F57927")
r3 = Radiobutton(root, bg="#F57927")
r4 = Radiobutton(root, bg="#F57927")

WandR = Label(root, font=("lucida 15 bold"))

check_btn = Button(root)

about_btn = Button(root,text="ABOUT",bg="black",fg="white",font=("lucida 15 bold"),command=abt)
about_btn.pack(side=BOTTOM,fill=X,padx=30)

root.mainloop()
