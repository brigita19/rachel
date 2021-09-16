from _typeshed import Self

from PIL import ImageTk

class Login:
    def __init__(self,window):
        self.window = window
        self.window.title("Login system")
        self.window.geometry("1199x600+100+50")

    # Login frame
    Frame_login = Frame(Self.window, bg="white")
    Frame_login.place(x=338, y=150, width=500, height=400)

    #Title & Subtitle
    title=Label(Frame_login, text="Login Here", font=("Impact", 35, "bold"), fg="#6162FF", bg="Black").place(x=98, y=30)
window = Tk()
obj = Login(window)from tkinter import *
window.mainloop()
        
