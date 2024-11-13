from tkinter import *
import customtkinter as ct

ct.set_appearance_mode("dark")
ct.set_default_color_theme("dark-blue")

root = ct.CTk()

root.title("template")
root.iconbitmap("./icon.ico")
root.geometry("600x350")

# -------- write code below ------------


my_label = ct.CTkLabel(root, text="Hello")
my_label.pack(pady=20)


# -------- write code above ------------

root.mainloop()
