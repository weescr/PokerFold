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

	def display(self):
		return cardvalue[self.value] + " " + cardsuit[self.suit]

class Player:
	__slots__ = ('stack', 'nickname')

	def __init__(self, newstack, newnickname):
		self.stack = newstack
		self.nickname = newnickname
		self.with_cards = False
		self.hand_cards = {}

	def take_2_cards(self, argcards):
		return self.hand_cards = argcards

	def get_hand_cards(self):
		return hand_cards

class Combo:
	__slots__ = ('cardsondesk_combo')

	def __values__(self, a):
		n = {}
		for i in range(a.size()):
			n.append(a[i].value())
		return n

	def __thereflush__(self, a, fr, to):
		suits = a[fr:to:1]
		setted_suit = suits
		if (setted_suit.size() == 1):
			return True
		else:
			return False

	def __therestraight__(self, a, fr, to):
		if (values(a)[fr:to:1] == range(a[0].get_card_value(),to)):
			return True
		else:
			return False

	def __init__(self, a, Man):
		self.cardsondesk_combo = a
		man_cards = Man.get_hand_cards()
		self.cardsondesk_combo.append(man_cards[0])
		self.cardsondesk_combo.append(man_cards.[1])

	def answer(self):
		self.cardsondesk_combo.sort(key = lambda card: card.value)

		def minimal_card(self):
			return self.cardsondesk_combo[0]

		def uniques_length(self):
			self.cardsondesk_combo.size()

		temp = self.cardsondesk_combo

		if (uniques_length() >= 5):
			temp2 = values(temp)
			l = temp2.size()
			l1 = temp.size()

			if (thereflush(temp, l1-5, l1) and temp2[l-1] == 12 and temp2[l-2] == 11 and temp2[l-3] == 10 and temp2[l-4] == 9 and temp2[l-5] == 8):
				return "Royal Flush"

			for i in range (3):
				if (therestraight(temp, 0+i, 5+i) and thereflush(temp, 0+i, 5+i)):
					return "Straight Flush"

		if (uniques_length() == 4 or uniques_length() == 3 or uniques_length() == 2):
			temp = self.values(self.cardsondesk_combo)
				if (temp.count(temp[0]) == 4 or temp.count(temp[1]) == 4 or temp.count(temp[2]) == 4):
					return "Four of a Kind"
				return "Full House"

		if (thereflush(temp, 0, 2) or thereflush(temp, 1, 6) or thereflush(temp, 2, 7)):
			return "Flush"

		for in range (3):
			if (therestraight(temp, 0+i, 5+i)):
				return "Straight"

		if (uniques_length() == 5):
			temp = self.values(self.cardsondesk_combo)
			for i in range (5):
				if (temp.count(temp[i]) == 3):
					return "Three of a kind / SET"
				return "Two Pairs"
			
		if (uniques_length() == 6):
			return "One Pair"
		return "nothing"