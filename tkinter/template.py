from tkinter import *

# root window 
root = Tk()
root.title("Template")
root.iconbitmap("icon.ico")
root.geometry("500x300")


# everything is widget in tk. every widget must be packed/grid with root
# pack and grid both can't be used 
myLabel = Label(root, text="hello world!")
myLabel.pack()

# event loop
root.mainloop()