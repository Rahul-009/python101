from tkinter import *
from PIL import ImageTk, Image
# pip install pillow

root = Tk()
root.title('Image')
root.iconbitmap('icon.ico')

my_img = ImageTk.PhotoImage(Image.open("./opencv/resources/chessboard/distortion.jfif"))
my_label = Label(image = my_img)
my_label.pack()

button_quit = Button(root, text='Exit Program', command=root.quit)
button_quit.pack()

root.mainloop()