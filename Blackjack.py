import random
from tkinter import *

root = Tk()
root.title("Blackjack")
root.resizable(0,0)





Hit = Button(root, text = "Hit Me!", font = ("Arial", 20), command = lambda: deal_card(Player))
Hit.grid(row = 0, column = 0, padx = 3, pady = 3)

Stay = Button(root, text = "Stay!", font = ("Arial", 20))
Stay.grid(row = 0, column = 1, padx = 3, pady = 3)

QUIT = Button(root, text = "Quit", font = ("Arial", 20), command = root.destroy)
QUIT.grid(row = 1, column = 0, padx = 3, pady = 3, columnspan = 2, sticky = EW)



deck_of_cards = [
	'2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC', 'AC',
	'2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS', 'AS',
	'2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH', 'AH',
	'2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD', 'AD'
]

class Gambler:
	def __init__(self, money):
		self.money = money
		self.cards = []

	def find_value(salf, cards):
		total = 0
		faces = ['J', 'Q', 'K']
		for card in cards:
			if card[:-1] in faces:
				total += 10
			elif card[:-1] == 'A':
				total += 1
			else:
				total += int(card[:-1])
		return total


Player = Gambler(1000)
Dealer = Gambler(0)

def find_suit(card):
	if card[-1] == 'H':
		return 'Hearts'
	elif card[-1] == 'D':
		return 'Diamonds'
	elif card[-1] == 'C':
		return 'Clubs'
	else:
		return 'Spades'


def deal_card(gambler):
	rand_card = random.choice(deck_of_cards)
	suit = find_suit(rand_card)
	value = rand_card[:-1]
	gambler.cards.append(rand_card)
	deck_of_cards.remove(rand_card)

def deal_starting_hand():
	for i in range(2):
		deal_card(Player)
		deal_card(Dealer)

deal_starting_hand()
print("Dealer's cards:", Dealer.cards)

# tkinter starts here
value = Player.find_value(Player.cards)
turn = True
while value <= 21 and turn == True:

	print("Your cards:", Player.cards)
	print("Value: ", value)
	while True:
		print('Hit or Stay')
		move = input("Your move: ")
		move = move.lower()
		if move == 'hit' or move == 'stay':
			break
	if move == 'stay':
		turn = False
	else:
		deal_card(Player)
		value = Player.find_value(Player.cards)
		if value > 21:
			print("You Busted!")
			turn = False
		elif value == 21:
			print('Blackjack')
			turn = False


root.mainloop()
