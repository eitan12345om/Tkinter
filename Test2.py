import random
from tkinter import *

root = Tk()
root.title('Turn Game')
root.resizable(0,0)


class Player:

	def __init__(self):
		self.health = 200
		self.poisonous = False

	def _attacking(self, attack, other):
		if self.poisonous:
			attack += 5
		other.health = max(0, other.health - attack)

	def _healing(self, heal, health):
		self.health = min(200, health + heal)

	def moderate(self, other):
		attack = random.randrange(23, 31)
		self._attacking(attack, other)

	def heavy(self, other):
		attack = random.randrange(10, 36)
		self._attacking(attack, other)

class Interface:

	def __init__(self, master):
		self.Human = Player()
		self.Computer = Player()



		neutral_descrip = "Your Health: %s      Computer Health: %s" % (self.Human.health, self.Computer.health)
		mod_descrip = "Attack (18-25): Summon Gods after 3 turns"
		hev_descrip = "Attack (10-35) with a chance of (0-5) recoil"
		hel_descrip = "Heal (18-25) lifepoints a with healing elixir"
		pos_descrip = "Adds an extra 5 damage. Can be used once"
		sum_descrip = "Half Computer's health or take 25 of own"





		display_variable = StringVar()
		display_variable.set(neutral_descrip)
		display = Message(master, textvariable = display_variable, font = ('Times New Roman', 16, 'bold'), width = 1000)
		display.grid(row = 0, column = 0, columnspan = 3)

		attacks = Message(master, text = 'Attacks', font = ('Times New Roman', 10, 'bold'), width = 50)
		attacks.grid(row = 1, column = 0)
		moderate_attack = Button(master, text = 'Moderate', font = ('Times New Roman', 16, 'bold'))
		moderate_attack.grid(row = 2, column = 0)
		moderate_attack.bind('<Enter>', lambda event: display.config(display_variable.set(mod_descrip)))
		moderate_attack.bind('<Leave>', lambda event: display.config(display_variable.set(neutral_descrip)))
		heavy_attack = Button(master, text = 'Heavy', font = ('Times New Roman', 16, 'bold'))
		heavy_attack.grid(row = 3, column = 0)
		heavy_attack.bind('<Enter>', lambda event: display.config(display_variable.set(hev_descrip)))
		heavy_attack.bind('<Leave>', lambda event: display.config(display_variable.set(neutral_descrip)))

		healing = Message(master, text = 'Healing', font = ('Times New Roman', 10, 'bold'), width = 50)
		healing.grid(row = 1, column = 1)
		heal_self = Button(master, text = 'Heal', font = ('Times New Roman', 16, 'bold'))
		heal_self.grid(row = 2, column = 1)
		heal_self.bind('<Enter>', lambda event: display.config(display_variable.set(hel_descrip)))
		heal_self.bind('<Leave>', lambda event: display.config(display_variable.set(neutral_descrip)))

		special_moves = Message(master, text = 'Special Moves', font = ('Times New Roman', 10, 'bold'), width = 100)
		special_moves.grid(row = 1, column = 2)
		poison_blade = Button(master, text = 'Poison Blade', font = ('Times New Roman', 16, 'bold'))
		poison_blade.grid(row = 2, column = 2)
		poison_blade.bind('<Enter>', lambda event: display.config(display_variable.set(pos_descrip)))
		poison_blade.bind('<Leave>', lambda event: display.config(display_variable.set(pos_descrip)))
		summon_gods = Button(master, text = 'Summon Gods', font = ('Times New Roman', 16, 'bold'), state = DISABLED)
		summon_gods.grid(row = 3, column = 2)
		summon_gods.bind('<Enter>', lambda event: display.config(display_variable.set(sum_descrip)))
		summon_gods.bind('<Leave>', lambda event: display.config(display_variable.set(sum_descrip)))


GUI = Interface(root)
root.mainloop()







print(Human.health)
print(Computer.health)
while Computer.health > 0:
	Human.heavy(Computer)
	print(Computer.health)