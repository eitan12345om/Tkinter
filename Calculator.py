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

	def exponentiate(self, a, b):
		return a ** b

	def a_root(self, a, b):
		b = self.exponentiate(b, -1)
		return round(a ** b, 5)


class CalcButton(Button):
	def __init__(self, master, number, callback):
		button_args = dict(width = 4, height = 2, bg = 'light blue', font = ("Helvetica", 10, "bold"), highlightcolor = 'gold')
		super().__init__(master, text = number, command = lambda: callback(number), **button_args)

class Interface:
	def __init__(self, master):
		master.bind('<Return>', self.press_equal)
		master.bind('=', self.press_equal)
		master.bind('<BackSpace>', self.backspace)
		master.bind('1', lambda event: self.show_number('1'))
		master.bind('2', lambda event: self.show_number('2'))
		master.bind('3', lambda event: self.show_number('3'))
		master.bind('4', lambda event: self.show_number('4'))
		master.bind('5', lambda event: self.show_number('5'))
		master.bind('6', lambda event: self.show_number('6'))
		master.bind('7', lambda event: self.show_number('7'))
		master.bind('8', lambda event: self.show_number('8'))
		master.bind('9', lambda event: self.show_number('9'))
		master.bind('0', lambda event: self.show_number('0'))
		master.bind('+', lambda event: self.small_interface_shift('+'))
		master.bind('-', lambda event: self.small_interface_shift('-'))
		master.bind('*', lambda event: self.small_interface_shift('*'))
		master.bind('/', lambda event: self.small_interface_shift('/'))
		master.bind('.', self.add_decimal)

		self.Calc = Calculator()

		self.display_maxLength = 15
		self.display_numbers = StringVar()
		self.small_display_numbers = StringVar()

		# Create display
		small_display = Message(master, textvariable = self.small_display_numbers, font = ("Times", 10), width = 200, bg = 'white', anchor = E)
		small_display.grid(column = 0, row = 0, columnspan = 5, sticky = NSEW)
		display = Message(master, textvariable = self.display_numbers, font = ("Helvetica", 16, "bold"), width = 200, bg = 'white', anchor = E)
		display.grid(column = 0, row = 1, columnspan = 5, sticky = NSEW)

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
		number1.bind("<Enter>", lambda event: number1.config(bg = "gold"))
		number2.bind("<Enter>", lambda event: number2.config(bg = "gold"))
		number3.bind("<Enter>", lambda event: number3.config(bg = "gold"))
		number4.bind("<Enter>", lambda event: number4.config(bg = "gold"))
		number5.bind("<Enter>", lambda event: number5.config(bg = "gold"))
		number6.bind("<Enter>", lambda event: number6.config(bg = "gold"))
		number7.bind("<Enter>", lambda event: number7.config(bg = "gold"))
		number8.bind("<Enter>", lambda event: number8.config(bg = "gold"))
		number9.bind("<Enter>", lambda event: number9.config(bg = "gold"))
		number0.bind("<Enter>", lambda event: number0.config(bg = "gold"))
		number1.bind("<Leave>", lambda event: number1.config(bg = "light blue"))
		number2.bind("<Leave>", lambda event: number2.config(bg = "light blue"))
		number3.bind("<Leave>", lambda event: number3.config(bg = "light blue"))
		number4.bind("<Leave>", lambda event: number4.config(bg = "light blue"))
		number5.bind("<Leave>", lambda event: number5.config(bg = "light blue"))
		number6.bind("<Leave>", lambda event: number6.config(bg = "light blue"))
		number7.bind("<Leave>", lambda event: number7.config(bg = "light blue"))
		number8.bind("<Leave>", lambda event: number8.config(bg = "light blue"))
		number9.bind("<Leave>", lambda event: number9.config(bg = "light blue"))
		number0.bind("<Leave>", lambda event: number0.config(bg = "light blue"))

		# backspace and clear
		backspace = Button(master, text = "←", width = 4, height = 2, bg = 'light blue', font = ("Helvetica", 10, "bold"), command = self.backspace)
		clear_display = Button(master, text = "CE", width = 4, height = 2, bg = 'light blue', font = ("Helvetica", 10, "bold"), command = self.clear_disp)
		clear_all = Button(master, text = "C", width = 4, height = 2, bg = 'light blue', font = ("Helvetica", 10, "bold"), command = self.clear_interface)
		backspace.grid(column = 0, row = 2, padx = 3, pady = 3)
		clear_display.grid(column = 1, row = 2, padx = 3, pady = 3)
		clear_all.grid(column = 2, row = 2, padx = 3, pady = 3)
		backspace.bind("<Enter>", lambda event: backspace.config(bg = "gold"))
		clear_display.bind("<Enter>", lambda event: clear_display.config(bg = "gold"))
		clear_all.bind("<Enter>", lambda event: clear_all.config(bg = "gold"))
		backspace.bind("<Leave>", lambda event: backspace.config(bg = "light blue"))
		clear_display.bind("<Leave>", lambda event: clear_display.config(bg = "light blue"))
		clear_all.bind("<Leave>", lambda event: clear_all.config(bg = "light blue"))

		# signs of operation and decimal
		plus = Button(master, text = "+", width = 4, height = 2, bg = 'light blue', font = ("Helvetica", 10, "bold"), command = lambda: self.small_interface_shift('+'))
		minus = Button(master, text = "-", width = 4, height = 2, bg = 'light blue', font = ("Helvetica", 10, "bold"), command = lambda: self.small_interface_shift('-'))
		multiply = Button(master, text = "*", width = 4, height = 2, bg = 'light blue', font = ("Helvetica", 10, "bold"), command = lambda: self.small_interface_shift('*'))
		divide = Button(master, text = "/", width = 4, height = 2, bg = 'light blue', font = ("Helvetica", 10, "bold"), command = lambda: self.small_interface_shift('/'))
		equal = Button(master, text = "=", width = 4, height = 2, bg = 'light blue', font = ("Helvetica", 10, "bold"), command = self.press_equal)
		decimal = Button(master, text = ".", width = 4, height = 2, bg = 'light blue', font = ("Helvetica", 10, "bold"), command = self.add_decimal)
		plus.grid(column = 3, row = 2, padx = 3, pady = 3)
		minus.grid(column = 3, row = 3, padx = 3, pady = 3)
		multiply.grid(column = 3, row = 4, padx = 3, pady = 3)
		divide.grid(column = 3, row = 5, padx = 3, pady = 3)
		equal.grid(column = 2, row = 6, padx = 3, pady = 3, columnspan = 2, sticky = EW)
		decimal.grid(column = 1, row = 6, padx = 3, pady = 3)
		plus.bind("<Enter>", lambda event: plus.config(bg = 'gold'))
		minus.bind("<Enter>", lambda event: minus.config(bg = 'gold'))
		multiply.bind("<Enter>", lambda event: multiply.config(bg = 'gold'))
		divide.bind("<Enter>", lambda event: divide.config(bg = 'gold'))
		equal.bind("<Enter>", lambda event: equal.config(bg = 'gold'))
		decimal.bind("<Enter>", lambda event: decimal.config(bg = 'gold'))
		plus.bind("<Leave>", lambda event: plus.config(bg = "light blue"))
		minus.bind("<Leave>", lambda event: minus.config(bg = "light blue"))
		multiply.bind("<Leave>", lambda event: multiply.config(bg = "light blue"))
		divide.bind("<Leave>", lambda event: divide.config(bg = "light blue"))
		equal.bind("<Leave>", lambda event: equal.config(bg = "light blue"))
		decimal.bind("<Leave>", lambda event: decimal.config(bg = "light blue"))

		# more advanced operators
		square = Button(master, text = "x²", width = 4, height = 2, bg = 'light blue', font = ("Helvetica", 10, "bold"))
		square.grid(column = 4, row = 2, padx = 3, pady = 3)
		exponent = Button(master, text = "xʸ", width = 4, height = 2, bg = 'light blue', font = ("Helvetica", 10, "bold"), command = lambda: self.small_interface_shift('^'))
		exponent.grid(column = 4, row = 3, padx = 3, pady = 3)
		squareroot = Button(master, text = "√x", width = 4, height = 2, bg = 'light blue', font = ("Helvetica", 10, "bold"))
		squareroot.grid(column = 4, row = 4, padx = 3, pady = 3)
		some_root = Button(master, text = "ʸ√x", width = 4, height = 2, bg = 'light blue', font = ("Helvetica", 10, "bold"), command = lambda: self.small_interface_shift('yroot'))
		some_root.grid(column = 4, row = 5, padx = 3, pady = 3)
		one_over = Button(master, text = "1/x", width = 4, height = 2, bg = 'light blue', font = ("Helvetica", 10, "bold"))
		one_over.grid(column = 4, row = 6, padx = 3, pady = 3)


	def show_number(self, number, *args):
		if len(self.display_numbers.get()) < self.display_maxLength:
			if number != '0': 
				self.display_numbers.set(self.display_numbers.get() + number)
			else:
				if len(self.display_numbers.get()) > 0 and number == '0':
					self.display_numbers.set(self.display_numbers.get() + number)

	def backspace(self, event = None):
		self.display_numbers.set(self.display_numbers.get()[:-1])

	def clear_disp(self):
		self.display_numbers.set('')

	def clear_interface(self):
		self.clear_disp()
		self.small_display_numbers.set('')

	def add_decimal(self, event = None):
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

	def press_equal(self, event = None):
		if len(self.small_display_numbers.get()) > 0 and len(self.display_numbers.get()):
			if self.small_display_numbers.get()[-1] == '+':
				answer = str(self.Calc.add(float(self.small_display_numbers.get()[:-2]), float(self.display_numbers.get())))
			elif self.small_display_numbers.get()[-1] == '-':
				answer = str(self.Calc.subtract(float(self.small_display_numbers.get()[:-2]), float(self.display_numbers.get())))
			elif self.small_display_numbers.get()[-1] == '*':
				answer = str(self.Calc.multiply(float(self.small_display_numbers.get()[:-2]), float(self.display_numbers.get())))
			elif self.small_display_numbers.get()[-1] == '/':
				answer = str(self.Calc.divide(float(self.small_display_numbers.get()[:-2]), float(self.display_numbers.get())))
			elif self.small_display_numbers.get()[-1] == '^':
				answer = str(self.Calc.exponentiate(float(self.small_display_numbers.get()[:-2]), float(self.display_numbers.get())))
			else:
				answer = str(self.Calc.a_root(float(self.small_display_numbers.get()[:-6]), float(self.display_numbers.get())))

			self.clean_up(answer)

	def clean_up(self, answer):
		self.clear_interface()
		if answer[-2:] == '.0':
			answer = answer[:-2]
		self.display_numbers.set(answer)

	def press_one_over(self):
	
		self.Calc

GUI = Interface(root)
root.mainloop()


"""Use Boolean to check if button is 'on'"""

"""
Make bind to allow key-presses
"""