from tkinter import *

root = Tk()
root.title('Button Clicker')

counter = IntVar()
counter.set(0)

counter_string = StringVar()
counter_string.set("You've clicked the button %d times" % counter.get())

def add_click():
	counter.set(counter.get() + 1)
	if counter.get() == 1:
		counter_string.set("You've clicked the button %d time" % counter.get())
	else:
		counter_string.set("You've clicked the button %d times" % counter.get())
	print(counter.get())
def reset_clicks():
	counter.set(0)
	counter_string.set("You've clicked the button %d times" % counter.get())


label = Label(root,
	textvariable = counter_string
)
label.pack(side = TOP)

button = Button(root,
	text = "Click Me!",
	font = ("Helvetica", 16, "bold"),
	padx = 5,
	command = add_click
)
button.pack(side = LEFT)

RESET = Button(root,
	text = "Reset",
	bg = "red",
	font = ("Helvetica", 16, "bold"),
	padx = 5,
	command = reset_clicks
)


RESET.pack(side = RIGHT)

root.mainloop()