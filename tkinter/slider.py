from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title('Codemy.com Image Viewer')
root.iconbitmap('icon.ico')
root.geometry("400x400")

def slide():
	my_label = Label(root, text=str(horizontal.get()) + " x " + str(vertical.get())).pack()
	# root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))

vertical = Scale(root, from_=0, to=200)
vertical.pack()

horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL)
horizontal.pack()


my_label = Label(root, text=horizontal.get()).pack()
my_btn = Button(root, text="Click Me!", command=slide).pack()

root.mainloop()

