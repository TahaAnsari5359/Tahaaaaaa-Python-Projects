from tkinter import *
import instaloader
import tkinter.messagebox as tmsg
root = Tk()
root.resizable(False,False)
root.config(bg="#58101C")
root.title("Instagram Details")
e1_var = StringVar()




username_enter = Label(root,bg="#58101C",fg="white",text="Enter Instagram Username: ",font=("lucida 10 bold"))
username_enter.pack(pady=10,anchor=W,padx=20)

def fetch():
    if e1_var.get() == "":
        tmsg.showwarning("warning","Enter Instagram Username")
        return
    else:
        try:
            namess = e1_var.get()
            cont = instaloader.Instaloader()
            profile = instaloader.Profile.from_username(cont.context,namess)

            username_lab.config(text=f"Username: {profile.username}" )
            full_name_lab.config(text=f"Full Name: {profile.full_name}")
            Bio_lab.config(text=f"Bio: {profile.biography}",wraplength=350)
            Followers_lab.config(text=f"Followers: {profile.followers}")
            Following_lab.config(text=f"Following: {profile.followees}")
            priv_test = profile.is_private
            if priv_test == True:
                Private_lab.config(text=f"Private: Account is Private")
            else:
                Private_lab.config(text=f"Public: Account is Public")

            verify_test = profile.is_verified
            if verify_test == "verified":
                Verified_lab.config(text=f"Verified: Account is Officially Verified")
            else:
                Verified_lab.config(text=f"Verified: Account is Not Verified")

            Posts_lab.config(text=f"Posts: {profile.mediacount}")

            webs_test = profile.external_url
            if webs_test == None:

                Website_lab.config(text=f"Website: No Website Found")
            else:
                Website_lab.config(text=f"Website: {profile.external_url}")

        except:
            tmsg.showerror("error","No Account Found For this Username")
            return
        



e1_ent = Entry(root,textvariable=e1_var,font=("lucida 15 bold"))
e1_ent.pack(fill=X,padx=20,pady=10)


fetch_btn = Button(root,bg="#10584C",fg="white",text="FETCH DETAILS",font=("lucida 10 bold"),command=fetch)
fetch_btn.pack(pady=10,padx=20,anchor=W)

details_bar = Label(root,bg="black",fg="white",text="DETAILS",font=("lucida 10 bold"))
details_bar.pack(pady=10,fill=X)

username_lab = Label(root,bg="#58101C",fg="white",text="Username: ",font=("lucida 10 bold"))
username_lab.pack(padx=20,anchor=W,pady=10)


full_name_lab = Label(root,bg="#58101C",fg="white",text="Full Name: ",font=("lucida 10 bold"))
full_name_lab.pack(padx=20,anchor=W,pady=10)



Bio_lab = Label(root,bg="#58101C",fg="white",text="Bio: ",font=("lucida 10 bold"))
Bio_lab.pack(padx=20,anchor=W,pady=10)


Followers_lab = Label(root,bg="#58101C",fg="white",text="Followers: ",font=("lucida 10 bold"))
Followers_lab.pack(padx=20,anchor=W,pady=10)


Following_lab = Label(root,bg="#58101C",fg="white",text="Following: ",font=("lucida 10 bold"))
Following_lab.pack(padx=20,anchor=W,pady=10)






Private_lab = Label(root,bg="#58101C",fg="white",text="Private: ",font=("lucida 10 bold"))
Private_lab.pack(padx=20,anchor=W,pady=10)



Verified_lab = Label(root,bg="#58101C",fg="white",text="Verified: ",font=("lucida 10 bold"))
Verified_lab.pack(padx=20,anchor=W,pady=10)



Posts_lab = Label(root,bg="#58101C",fg="white",text="Posts: ",font=("lucida 10 bold"))
Posts_lab.pack(padx=20,anchor=W,pady=10)



Website_lab = Label(root,bg="#58101C",fg="white",text="Website: ",font=("lucida 10 bold"))
Website_lab.pack(padx=20,anchor=W,pady=10)






root.mainloop()
