from tkinter import *
from deep_translator import GoogleTranslator
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("800x500")
root.config(bg="#ffbe98")


main_lab = Label(root, bg="#ffbe98", text="LANGUAGE TRANSLATOR", font=("lucida 15 bold"))
main_lab.pack(pady=15)




def translate():
    try:
    # fromm = from_var.get()
    # too = to_var.get()
        fromm = selected1.get()
        too = selected2.get() 

        text = enter_var.get()




        translated = GoogleTranslator(source=fromm, target=too).translate(text)
        mean_lab.config(text=translated)
        text = enter_var.set("")
    except:
        tmsg.showinfo("error", "Enter Language to translate")


def info():
    infoo = Label(root, text="en - English \n hi - Hindi \n fr - French \n es - Spanish \n de - German \n ar - Arabic \n ur - Urdu", font=("lucida 10 bold"))
    infoo.place(x=700, y=150)



info_button = Button(root, width=4, height=1, text="Info", font=("lucida 15 bold"), command=info)
info_button.place(x=700, y=50)



# from_lang_lab = Label(root, bg="#ffbe98", text="From Language", font=('lucida 10 bold'))
# from_lang_lab.place(x=50,y=50) 

# from_var = StringVar()
# from_ent = Entry(root, textvariable=from_var, font=("lucida 20 bold"))
# from_ent.place(x=50, y=80)

# to_lang_lab = Label(root, bg="#ffbe98", text="To Language", font=('lucida 10 bold'))
# to_lang_lab.place(x=50,y=140)

# to_var = StringVar()
# to_ent = Entry(root, textvariable=to_var, font=("lucida 20 bold"))
# to_ent.place(x=50, y=170)

from_dropdownn = ["Select One Of The Language From Below", "en", "hi", "fr", "es", "de", "ar", "ur"]

too_dropdown = ["Select One Of The Language From Below", "en", "hi", "fr", "es", "de", "ar", "ur"]

selected1 = StringVar()
selected1.set(from_dropdownn[0])
selected2 = StringVar()
selected2.set(too_dropdown[0])

FONT_OPTION = ("Arial", 12)

from_dropdown = OptionMenu(root,  selected1, *from_dropdownn)
from_dropdown.place(x=50, y=80)

to_dropdown = OptionMenu(root, selected2, *too_dropdown)
to_dropdown.place(x=50, y=170)




enter_lab = Label(root, bg="#ffbe98", text="Enter text", font=('lucida 10 bold'))
enter_lab.place(x=50,y=220)

enter_var = StringVar()
enter_text = Entry(root, textvariable=enter_var, font=("lucida 20 bold"))
enter_text.place(x=50, y=250)



translate_btn = Button(root, text="Translate", font=('lucida 10 bold'), command=translate)
translate_btn.place(x=400, y= 255)


mean_lab = Label(root, bg="#ffbe98", font=("lucida 25 bold"))
mean_lab.place(x=250, y=355)






root.mainloop()
