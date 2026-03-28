from tkinter import *
import tkinter.messagebox as tmsg
import random
import pyttsx3
root = Tk()
root.geometry("600x500")
root.config(bg="#12C870")
root.title("Quotes Generator")
root.resizable(False,False)

engine = pyttsx3.init()


main_lab = Label(root,text="QUOTES GENERATOR 💬",bg="black",fg="white",font=("lucida 20 bold"))
main_lab.pack(fill=X,)



happy_quotes = [
    "Happiness is not something ready-made. It comes from your own actions.",
    "The purpose of our lives is to be happy.",
    "Count your age by friends, not years. Count your life by smiles, not tears.",
    "Happiness is a warm puppy.",
    "For every minute you are angry, you lose sixty seconds of happiness.",
    "Do more of what makes you happy.",
    "Happiness is not having what you want. It’s wanting what you have.",
    "The most wasted of all days is one without laughter.",
    "Be happy for this moment. This moment is your life.",
    "Happiness is a direction, not a place."
]


sad_quotes = [
    "Tears are words the heart can’t express.",
    "Sometimes you have to accept that some chapters will close without closure.",
    "It hurts when you have someone in your heart, but not in your life.",
    "The worst feeling isn’t being lonely, it’s being forgotten by someone you can’t forget.",
    "You can’t be strong all the time. Sometimes you just need to be alone and let your tears out.",
    "We all have that one person we wish we could forget.",
    "It’s sad when the person who gave you memories becomes a memory.",
    "Silence is the most powerful scream.",
    "Behind every smile, there’s a story you’ll never understand.",
    "Sometimes, you have to smile to hide your pain."
]

romantic_quotes = [
    "Every love story is beautiful, but ours is my favorite.",
    "You are my today and all of my tomorrows.",
    "I saw that you were perfect, and so I loved you.",
    "Love is not about how many days, months, or years you’ve been together. Love is about how much you love each other every single day.",
    "You are the reason I look down at my phone and smile. Then walk into a pole."
]

funny_quotes = [
    "I’m on a whiskey diet. I’ve lost three days already.",
    "My bed is a magical place where I suddenly remember everything I forgot to do.",
    "I’m not lazy, I’m just on energy-saving mode.",
    "Common sense is like deodorant. The people who need it most never use it.",
    "I told my computer I needed a break, and now it won’t stop sending me KitKat ads."
]

motivational_quotes = [
    "Push yourself, because no one else is going to do it for you.",
    "Dream big. Work hard. Stay focused.",
    "Don’t watch the clock; do what it does. Keep going.",
    "It always seems impossible until it’s done.",
    "Success doesn’t come from what you do occasionally, it comes from what you do consistently."
]

energy_quotes = [
    "Start your day with energy and end it with gratitude.",
    "Your energy introduces you before you even speak.",
    "Surround yourself with those who radiate positive energy.",
    "You have the power to create the energy you want to feel.",
    "Be the energy you want to attract."
]

reality_quotes = [
    "Reality is often disappointing.",
    "The truth may hurt for a little while, but a lie hurts forever.",
    "Sometimes you have to accept that certain things will never go back to how they used to be.",
    "Not everyone will understand your journey, and that’s okay.",
    "Reality doesn’t always give you what you want, but it always gives you what you need."
]



def gen(Event=None):
        
        b1.config(state='disable')
        category = option_var.get()
        if category == "Happy":
            quote = random.choice(happy_quotes)
            res_lab.config(text=quote, bg="#FFF176",fg="black", relief=RIDGE)

        elif category == "Sad":
            quote = random.choice(sad_quotes)
            res_lab.config(text=quote, bg="#90A4AE",fg="black", relief=RIDGE)
        elif category == "Romantic":
            quote = random.choice(romantic_quotes)
            res_lab.config(text=quote, bg="#F48FB1",fg="black", relief=RIDGE)
        elif category == "Funny":
            quote = random.choice(funny_quotes)
            res_lab.config(text=quote, bg="#FFD54F",fg="black", relief=RIDGE)
        elif category == "Motivational":
            quote = random.choice(motivational_quotes)
            res_lab.config(text=quote, bg="#39D141",fg="black", relief=RIDGE)
        elif category == "Energy":
            quote = random.choice(energy_quotes)
            res_lab.config(text=quote, bg="#4DB6AC", fg="black",relief=RIDGE)
        elif category == "Reality":
            quote = random.choice(reality_quotes)
            res_lab.config(text=quote, bg="#126AC8",fg="white", relief=RIDGE)
        else :
            tmsg.showerror("Error", "Please select a valid category!")
        
        res_lab.update()


        get_data = res_lab.cget("text")
        engine.setProperty('rate', 130)
        engine.say(get_data)
        engine.runAndWait()
        b1.config(state='normal')
    
        







values = "Happy","Sad","Romantic","Funny","Motivational","Energy","Reality"

option_var = StringVar()
option_var.set("Choose Catogory")
option_menu = OptionMenu(root,option_var,*values)
option_menu.pack(pady=30)

option_menu.config(font=("lucida 15 bold"),bg="red",fg="white")


b1 = Button(root,text="GENERATE QUOTES",bg="black",fg="white",relief=FLAT,bd=3,font=("lucida 14 bold"),command=gen)
b1.pack(side=BOTTOM,fill=X,padx=20,pady=20)
root.bind('<Return>',gen)

res_lab = Label(root,bg="#12C870",bd=5,wraplength=500,font=("lucida 20 bold"))
res_lab.pack(pady=30,fill=X)



root.mainloop()
