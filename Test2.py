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
		print(other.health, attack)

	def _healing(self, heal):
		self.health = min(200, self.health + heal)

	def moderate(self, other):
		attack = random.randrange(18, 26)
		self._attacking(attack, other)

	def heavy(self, other):
		attack = random.randrange(10, 36)
		self._attacking(attack, other)
		recoil = random.randrange(0, 6)
		self._attacking(recoil, self)

	def heal(self):
		heal = random.randrange(18, 26)
		self._healing(heal)

	def summon_gods(self, other):
		choice = random.randrange(2)
		if choice == 0:
			other.health = (other.health + 1) // 2
		else:
			self.health -= 25

class Interface:

	def __init__(self, master):
		self.Human = Player()
		self.Computer = Player()
		self.summon_counter = 0


		neutral_descrip = "Your Health: %s      Computer Health: %s" % (self.Human.health, self.Computer.health)
		mod_descrip = "Attack (18-25): Summon Gods after 3 turns"
		hev_descrip = "Attack (10-35) with a chance of (0-5) recoil"
		hel_descrip = "Heal (18-25) lifepoints: uses a healing elixir"
		pos_descrip = "Adds an extra 5 damage. Can be used once"
		sum_descrip = "Half Computer's health or minus 25 of own"




		self.display_variable = StringVar()
		self.display_variable.set(neutral_descrip)
		display = Message(master, textvariable = self.display_variable, font = ('Times New Roman', 16, 'bold'), width = 1000)
		display.grid(row = 0, column = 0, columnspan = 3)

		attacks = Message(master, text = 'Attacks', font = ('Times New Roman', 10, 'bold'), width = 50)
		attacks.grid(row = 1, column = 0)
		self.moderate_attack = Button(master, text = 'Moderate', font = ('Times New Roman', 16, 'bold'), command = self.click_moderate)
		self.moderate_attack.grid(row = 2, column = 0)
		self.moderate_attack.bind('<Enter>', lambda event: self.display_variable.set(mod_descrip))
		self.moderate_attack.bind('<Leave>', lambda event: self.update_health())
		self.heavy_attack = Button(master, text = 'Heavy', font = ('Times New Roman', 16, 'bold'), command = self.click_heavy)
		self.heavy_attack.grid(row = 3, column = 0)
		self.heavy_attack.bind('<Enter>', lambda event: self.display_variable.set(hev_descrip))
		self.heavy_attack.bind('<Leave>', lambda event: self.update_health())

		healing = Message(master, text = 'Healing', font = ('Times New Roman', 10, 'bold'), width = 50)
		healing.grid(row = 1, column = 1)
		self.heal_self = Button(master, text = 'Heal', font = ('Times New Roman', 16, 'bold'), state = DISABLED, command = self.click_heal)
		self.heal_self.grid(row = 2, column = 1)
		self.heal_self.bind('<Enter>', lambda event: self.display_variable.set(hel_descrip))
		self.heal_self.bind('<Leave>', lambda event: self.update_health())

		special_moves = Message(master, text = 'Special Moves', font = ('Times New Roman', 10, 'bold'), width = 100)
		special_moves.grid(row = 1, column = 2)
		self.poison_blade = Button(master, text = 'Poison Blade', font = ('Times New Roman', 16, 'bold'), fg = 'green', command = self.click_poison)
		self.poison_blade.grid(row = 2, column = 2)
		self.poison_blade.bind('<Enter>', lambda event: self.display_variable.set(pos_descrip))
		self.poison_blade.bind('<Leave>', lambda event: self.update_health())
		self.summon_gods = Button(master, text = 'Summon Gods', font = ('Times New Roman', 16, 'bold'), state = DISABLED, command = self.click_summon)
		self.summon_gods.grid(row = 3, column = 2)
		self.summon_gods.bind('<Enter>', lambda event: self.display_variable.set(sum_descrip))
		self.summon_gods.bind('<Leave>', lambda event: self.update_health())


	def click_moderate(self):
		self.Human.moderate(self.Computer)
		self.update_health()
		self.summon_counter += 1
		if self.summon_counter == 3:
			self.summon_gods.config(state = ACTIVE)

	def click_heavy(self):
		self.Human.heavy(self.Computer)
		self.update_health()
		self.update_heal()
		self.summon_counter = 0
		self.summon_gods.config(state = DISABLED)

	def click_heal(self):
		self.Human.heal()
		self.update_health()
		self.update_heal()
		self.summon_counter = 0
		self.summon_gods.config(state = DISABLED)

	def click_poison(self):
		self.Human.poisonous = True
		self.poison_blade.config(state = DISABLED)
		self.moderate_attack.config(fg = 'green')
		self.heavy_attack.config(fg = 'green')
		self.summon_counter = 0
		self.summon_gods.config(state = DISABLED)

	def click_summon(self):
		self.Human.summon_gods(self.Computer)
		self.update_health()
		self.update_heal()
		self.summon_counter = 0
		self.summon_gods.config(state = DISABLED)

	def update_health(self):
		neutral_descrip = "Your Health: %s      Computer Health: %s" % (self.Human.health, self.Computer.health)
		self.display_variable.set(neutral_descrip)

	def update_heal(self):
		if self.Human.health < 200:
			self.heal_self.config(state = ACTIVE)
		else:
			self.heal_self.config(state = DISABLED)

GUI = Interface(root)
root.mainloop()