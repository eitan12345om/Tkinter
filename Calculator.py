from tkinter import *

root = Tk()
root.title("Calculator")

class Calculator:
	def __init__(self):
		pass

	def add(self, a, b):
		return a + b

	def subtract(self, a, b):
		return a - b

	def multiply(self, a, b):
		return a * b

	def divide(self, a, b):
		return round(a / b, 5)

class Interface:
	def __init__(self, master):
		self.display_maxLength = 10
		self.display_numbers = StringVar()
		self.small_display_numbers = StringVar()

		number_button_params = dict(width = 4, height = 2, bg = 'light blue', font = ("Helvetica", 10, "bold"))	

		# Create display
		small_display = Message(master, textvariable = self.small_display_numbers, font = ("Times", 10), width = 200, bg = 'white', anchor = E)
		small_display.grid(column = 0, row = 0, columnspan = 4, sticky = NSEW)
		display = Message(master, textvariable = self.display_numbers, font = ("Helvetica", 16, "bold"), width = 200, bg = 'white', anchor = E)
		display.grid(column = 0, row = 1, columnspan = 4, sticky = NSEW)

		# number buttons
		number1 = Button(master, text = "1", command = lambda: self.show_number('1'), **number_button_params)
		number2 = Button(master, text = "2", command = lambda: self.show_number('2'), **number_button_params)
		number3 = Button(master, text = "3", command = lambda: self.show_number('3'), **number_button_params)
		number4 = Button(master, text = "4", command = lambda: self.show_number('4'), **number_button_params)
		number5 = Button(master, text = "5", command = lambda: self.show_number('5'), **number_button_params)
		number6 = Button(master, text = "6", command = lambda: self.show_number('6'), **number_button_params)
		number7 = Button(master, text = "7", command = lambda: self.show_number('7'), **number_button_params)
		number8 = Button(master, text = "8", command = lambda: self.show_number('8'), **number_button_params)
		number9 = Button(master, text = "9", command = lambda: self.show_number('9'), **number_button_params)
		number0 = Button(master, text = "0", command = lambda: self.show_number('0'), **number_button_params)
		number1.grid(column = 0, row = 3, padx = 3, pady = 3)
		number2.grid(column = 1, row = 3, padx = 3, pady = 3)
		number3.grid(column = 2, row = 3, padx = 3, pady = 3)
		number4.grid(column = 0, row = 4, padx = 3, pady = 3)
		number5.grid(column = 1, row = 4, padx = 3, pady = 3)
		number6.grid(column = 2, row = 4, padx = 3, pady = 3)
		number7.grid(column = 0, row = 5, padx = 3, pady = 3)
		number8.grid(column = 1, row = 5, padx = 3, pady = 3)
		number9.grid(column = 2, row = 5, padx = 3, pady = 3)
		number0.grid(column = 0, row = 6, padx = 3, pady = 3)

		# backspace and clear
		backspace = Button(master, text = "←", width = 4, height = 2, bg = 'light blue', font = ("Helvetica", 10, "bold"), command = self.backspace)
		backspace.grid(column = 0, row = 2, padx = 3, pady = 3)
		clear_display = Button(master, text = "CE", width = 4, height = 2, bg = 'light blue', font = ("Helvetica", 10, "bold"), command = self.clear_disp)
		clear_display.grid(column = 1, row = 2, padx = 3, pady = 3)
		clear_all = Button(master, text = "C", width = 4, height = 2, bg = 'light blue', font = ("Helvetica", 10, "bold"), command = self.clear_interface)
		clear_all.grid(column = 2, row = 2, padx = 3, pady = 3)
		

		# signs of operation
		plus = Button(master, text = "+", width = 4, height = 2, bg = 'light blue', font = ("Helvetica", 10, "bold"), command = lambda: self.small_interface_shift('+'))
		plus.grid(column = 3, row = 3, padx = 3, pady = 3)
		minus = Button(master, text = "-", width = 4, height = 2, bg = 'light blue', font = ("Helvetica", 10, "bold"), command = lambda: self.small_interface_shift('-'))
		minus.grid(column = 3, row = 4, padx = 3, pady = 3)
		multiply = Button(master, text = "*", width = 4, height = 2, bg = 'light blue', font = ("Helvetica", 10, "bold"), command = lambda: self.small_interface_shift('*'))
		multiply.grid(column = 3, row = 5, padx = 3, pady = 3)
		divide = Button(master, text = "/", width = 4, height = 2, bg = 'light blue', font = ("Helvetica", 10, "bold"), command = lambda: self.small_interface_shift('/'))
		divide.grid(column = 3, row = 6, padx = 3, pady = 3)
		equal = Button(master, text = "=", width = 4, height = 2, bg = 'light blue', font = ("Helvetica", 10, "bold"), command = self.press_equal)
		equal.grid(column = 1, row = 6, padx = 3, pady = 3, columnspan = 2, sticky = EW)
		
		print_to_screen = Button(master, text = "prs", width = 4, height = 2, bg = 'light blue', font = ("Helvetica", 10, "bold"), command = self.prs)
		print_to_screen.grid(column = 3, row = 2, columnspan = 2, padx = 3, pady = 3, sticky = EW)

	def show_number(self, number):
		if len(self.display_numbers.get()) < self.display_maxLength:
			if number != '0': 
				self.display_numbers.set(self.display_numbers.get() + number)
			else:
				if len(self.display_numbers.get()) > 0 and number == '0':
					self.display_numbers.set(self.display_numbers.get() + number)

	def backspace(self):
		self.display_numbers.set(self.display_numbers.get()[:-1])

	def clear_disp(self):
		self.display_numbers.set('')

	def clear_interface(self):
		self.clear_disp()
		self.small_display_numbers.set('')

	def prs(self):
		if len(self.display_numbers.get()) > 0:
			print(int(self.display_numbers.get()))

	def small_interface_shift(self, operator):
		if len(self.small_display_numbers.get()) == 0:
			if len(self.display_numbers.get()) > 0:
				self.small_display_numbers.set(self.display_numbers.get() + ' ' + operator)
				self.clear_disp()
		else:
			self.small_display_numbers.set(self.small_display_numbers.get()[:-1] + operator)

	def press_equal(self):
		if len(self.small_display_numbers.get()) > 0 and len(self.display_numbers.get()):
			print('Hi')


GUI = Interface(root)
root.mainloop()


"""Use Boolean to check if button is 'on'"""

"""
if len(small_display) > 0:
	self.clear_disp()
"""
	
