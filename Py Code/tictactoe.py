from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import customtkinter

#appearance
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

#frame
app = customtkinter.CTk()
app.geometry("1080x720")
app.title("tictactoe")

#UI
title = customtkinter.CTkLabel(app, text="TicTacToe")
title.pack(padx=10, pady=10)
image1 = Image.open("<C:/Users/aritz/Desktop/bs/1Pzpe.png>")
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test

app.mainloop()
