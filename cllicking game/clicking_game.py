from tkinter import *
root = Tk()
root.geometry("400x500")
root.title("Clicking Game")
root.config(bg="Red")

click = 0
high_score = 0
time_left = 5
timer_running = False


def start():
    global click, time_left, timer_running
    try:
        time_left = int(time_set_var.get())  # Try converting to int
    except:
        info_lab.config(text="⛔ Please enter valid time!")
        return  # Invalid input, don't start timer
    time_set_var.set("")
     

    click = 0
    clicks_lab.config(text="Clicks : 0")
    info_lab.config(text="")
    timer_running = True
    update_timer()


def update_timer():
    global time_left,timer_running,high_score
    if time_left > 0:
        time_left -=1
        time_left_lab.config(text=f"Time Left: {time_left}s")
        root.after(1000,update_timer)
    else:
        timer_running = False
        start_btn.config(state="normal")
        if click > high_score:
            high_score = click
            hight_score_lab.config(text=f"High score : {high_score}")
            info_lab.config(text=f"You Clicked : {click} times!") 

def click_counter():
    global click
    if timer_running:
        click +=1
        clicks_lab.config(text=f"Clicks : {click}")   


def sett():
    time_get = int(time_set_var.get())
    time_left_lab.config(text=f"Time Left: {time_get}s")
    


main_lab = Label(root,bg="black",fg="white",text="Click Game",font=("lucida 25 bold"))
main_lab.pack(fill=X)

time_left_lab = Label(root,bg="red",fg="black",text="Time Left : 0s",font=("lucida 15 bold"))
time_left_lab.pack(pady=10)

clicks_lab = Label(root,bg="red",fg="black",text="Clicks : 0",font=("lucida 15 bold"))
clicks_lab.pack(pady=10)

hight_score_lab = Label(root,bg="red",fg="black",text="hight Score : 0",font=("lucida 15 bold"))
hight_score_lab.pack(pady=10)

info_lab = Label(root,bg="red",fg="black",text="",font=("lucida 15 bold"))
info_lab.pack(pady=10)

count_btn = Button(root,width=16,text="Count",font=("lucida 15 bold"),command=click_counter)
count_btn.pack(pady=10)

start_btn = Button(root,width=16,text="Start",font=("lucida 15 bold"),command=start)
start_btn.pack()


time_set_var = StringVar()
time_ent = Entry(root,width=9,textvariable=time_set_var)
time_ent.place(x=300,y=60)

time_set_btn = Button(root,text="set",command=sett)
time_set_btn.place(x=370,y=60)



root.mainloop()
