import random
from randnumgen import rng, jersey_number, jersey_size, jersey_color
from tkinter import *
from PIL import ImageTk, Image
import tkinter
import tkinter.messagebox
import pickle

root = Tk()
root.title('Jersey Generator')

# Create an image
my_img = ImageTk.PhotoImage(Image.open("test.jpg")) # Exact location of file or just name of file if it's in the same directory as the program
my_label = Label(image=my_img)
my_label.pack()

# Create list box
listbox_tasks = tkinter.Listbox(root, height=10, width=50) # Listbox will have these dimensions and go into the frame_tasks directory
listbox_tasks.pack(side=tkinter.LEFT) # Must eventually PACK EVERYTHING

#RNG program
def printer():
	num = jersey_number()
	color = jersey_color()
	size = jersey_size()

	jer_num = "Jersey number: " + str(num)
	jer_col = "Jersey color: " + color
	jer_size = "Jersey size: " + size
	listbox_tasks.insert(tkinter.END, jer_num)
	listbox_tasks.insert(tkinter.END, jer_col)
	listbox_tasks.insert(tkinter.END, jer_size)

# Create button to exeute function
button_submit = Button(root, text="GENERATE RNG!!!", command=printer)
button_submit.pack()

# Create exit button
button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack() 

root.mainloop()