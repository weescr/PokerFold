import random

NVAL = 13
NSUIT = 4


cardsuit = ["черви","вини","буби","крести"]
cardvalue = ["2","3","4","5","6","7","8","9","10","Валет","Дама","Король","Туз"]

class Card:
	
	__slots__ = ('value', 'suit')
	
	def __init__(self, dsuit, dval):
		self.value = dval
		self.suit = dsuit
		
	def get_card_value(self):
		return self.value

	def get_card_suit(self):
		return self.suit

	def display(self):
		return cardvalue[self.value] + " " + cardsuit[self.suit]

class Player:
	
	__slots__ = ('stack', 'nickname')
	
	def __init__(self, newstack, newnickname):
		self.stack = newstack
		self.nickname = newnickname
		self.with_cards = False
		self.hand_cards = {}

	def name(self):
		return self.nickname

	def get_stack(self):
		return self.stack

	def take_2_cards(self, argcards):
		return self.hand_cards = argcards

	def get_hand_cards(self):
		return hand_cards
