from tkinter import *
import customtkinter as ct

ct.set_appearance_mode("dark")
ct.set_default_color_theme("dark-blue")

root = ct.CTk()

root.title("template")
root.iconbitmap("./icon.ico")
root.geometry("600x350")

def sliding(value):
    my_label.configure(text=int(value))

my_slider = ct.CTkSlider(root, from_=-100, to=100, command=sliding)
my_slider.pack(pady=40)

my_slider.set(0)

my_label = ct.CTkLabel(root, text=my_slider.get(), font=("Helvetica", 18))
my_label.pack(pady=20)



root.mainloop()
