from tkinter import *

root = Tk()
root.title("Button")


label_text = StringVar()

a_label = Label(root, textvariable = label_text)
a_label.pack(side = TOP)

label_text.set("You've clicked the button 0 times")

def counter_generator(number):
	while True:
		yield number
		number += 1

def inc():
	label_text.set("You've clicked the button %d times" % next(counter_generator(0)))


a_button = Button(root,
	text = "Click Me!",
	fg = "Red",
	font = "Times 16 bold",
	padx = 5,
	command = inc
)
a_button.pack(side = LEFT)

a_nother_button = Button(root,
	text = "QUIT",
	fg = "Black",
	font = "Times 16 bold",
	padx = 5,
	command = root.quit
)
a_nother_button.pack(side = LEFT)

root.mainloop()