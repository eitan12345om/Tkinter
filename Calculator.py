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

class CalcButton(Button):
	def __init__(self, master, number, callback):
		button_args = dict(width = 4, height = 2, bg = 'light blue', font = ("Helvetica", 10, "bold"))
		super().__init__(master, text = number, command = lambda: callback(number), **button_args)

class Interface:
	def __init__(self, master):
		self.Calc = Calculator()

		self.display_maxLength = 10
		self.display_numbers = StringVar()
		self.small_display_numbers = StringVar()

		# Create display
		small_display = Message(master, textvariable = self.small_display_numbers, font = ("Times", 10), width = 200, bg = 'white', anchor = E)
		small_display.grid(column = 0, row = 0, columnspan = 4, sticky = NSEW)
		display = Message(master, textvariable = self.display_numbers, font = ("Helvetica", 16, "bold"), width = 200, bg = 'white', anchor = E)
		display.grid(column = 0, row = 1, columnspan = 4, sticky = NSEW)

		# number buttons
		number1 = CalcButton(master, "1", self.show_number)
		number2 = CalcButton(master, "2", self.show_number)
		number3 = CalcButton(master, "3", self.show_number)
		number4 = CalcButton(master, "4", self.show_number)
		number5 = CalcButton(master, "5", self.show_number)
		number6 = CalcButton(master, "6", self.show_number)
		number7 = CalcButton(master, "7", self.show_number)
		number8 = CalcButton(master, "8", self.show_number)
		number9 = CalcButton(master, "9", self.show_number)
		number0 = CalcButton(master, "0", self.show_number)
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

		# signs of operation and decimal
		plus = Button(master, text = "+", width = 4, height = 2, bg = 'light blue', font = ("Helvetica", 10, "bold"), command = lambda: self.small_interface_shift('+'))
		plus.grid(column = 3, row = 2, padx = 3, pady = 3)
		minus = Button(master, text = "-", width = 4, height = 2, bg = 'light blue', font = ("Helvetica", 10, "bold"), command = lambda: self.small_interface_shift('-'))
		minus.grid(column = 3, row = 3, padx = 3, pady = 3)
		multiply = Button(master, text = "*", width = 4, height = 2, bg = 'light blue', font = ("Helvetica", 10, "bold"), command = lambda: self.small_interface_shift('*'))
		multiply.grid(column = 3, row = 4, padx = 3, pady = 3)
		divide = Button(master, text = "/", width = 4, height = 2, bg = 'light blue', font = ("Helvetica", 10, "bold"), command = lambda: self.small_interface_shift('/'))
		divide.grid(column = 3, row = 5, padx = 3, pady = 3)
		equal = Button(master, text = "=", width = 4, height = 2, bg = 'light blue', font = ("Helvetica", 10, "bold"), command = self.press_equal)
		equal.bind("<Return>", self.press_equal())
		equal.grid(column = 2, row = 6, padx = 3, pady = 3, columnspan = 2, sticky = EW)
		decimal = Button(master, text = ".", width = 4, height = 2, bg = 'light blue', font = ("Helvetica", 10, "bold"), command = self.add_decimal)
		decimal.grid(column = 1, row = 6, padx = 3, pady = 3)

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

	def add_decimal(self):
		if '.' not in self.display_numbers.get():
			if len(self.display_numbers.get()) == 0:
				self.display_numbers.set('0.')
			else:
				self.display_numbers.set(self.display_numbers.get() + '.')

	def small_interface_shift(self, operator):
		if len(self.small_display_numbers.get()) == 0:
			if len(self.display_numbers.get()) > 0:
				self.small_display_numbers.set(self.display_numbers.get() + ' ' + operator)
				self.clear_disp()
		else:
			self.small_display_numbers.set(self.small_display_numbers.get()[:-1] + operator)

	def press_equal(self):
		if len(self.small_display_numbers.get()) > 0 and len(self.display_numbers.get()):
			if self.small_display_numbers.get()[-1] == '+':
				answer = str(self.Calc.add(float(self.small_display_numbers.get()[:-2]), float(self.display_numbers.get())))
			elif self.small_display_numbers.get()[-1] == '-':
				answer = str(self.Calc.subtract(float(self.small_display_numbers.get()[:-2]), float(self.display_numbers.get())))
			elif self.small_display_numbers.get()[-1] == '*':
				answer = str(self.Calc.multiply(float(self.small_display_numbers.get()[:-2]), float(self.display_numbers.get())))
			else:
				answer = str(self.Calc.divide(float(self.small_display_numbers.get()[:-2]), float(self.display_numbers.get())))

			self.clear_interface()
			if answer[-2:] == '.0':
				answer = answer[:-2]
			self.display_numbers.set(answer)

GUI = Interface(root)
root.mainloop()


"""Use Boolean to check if button is 'on'"""

"""
if len(small_display) > 0:
	self.clear_disp()
"""
	
