from tkinter import *

root = Tk()

myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="My Name Is John Elder")
myLabel3 = Label(root, text="My Name Is John Elder")

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)
myLabel3.grid(row=2, column=5) 

# here 5 and 1 means same | relative to previous line


root.mainloop()

