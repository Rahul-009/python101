from tkinter import *
import customtkinter as ct

ct.set_appearance_mode("dark")
ct.set_default_color_theme("dark-blue")

root = ct.CTk()

root.title("template")
root.iconbitmap("./icon.ico")
root.geometry("600x350")

def hello():
    my_label.configure(text=my_button.cget("text"))


my_button = ct.CTkButton(root, 
    text="hello world!!",
    command = hello,
    height = 100,
    width = 200, 
    font = ("Helvetica", 24),
    text_color = "black",
    fg_color = "red",
    hover_color = "green",
    corner_radius = 50,
    bg_color = "white",
    border_width = 10,
    border_color = "yellow",
    state = "normal" # disabled 
)
my_button.pack(pady=80)

my_label = ct.CTkLabel(root, text="")
my_label.pack(pady=20)




root.mainloop()
