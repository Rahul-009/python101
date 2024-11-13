from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title('Window')
root.iconbitmap('icon.ico')

def open():
	global my_img
	top = Toplevel()
	top.title('My Second Window')
	top.iconbitmap('icon.ico')
	my_img = ImageTk.PhotoImage(Image.open("./opencv/resources/chessboard/distortion.jfif"))
	my_label = Label(top, image=my_img).pack()
	btn2 = Button(top, text="close window", command=top.destroy).pack()



btn = Button(root, text="New Window", command=open).pack()


mainloop()