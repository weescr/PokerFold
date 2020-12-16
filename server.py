import random


cardsuit = ["черви","вини","буби","крести"]
cardvalue = ["2","3","4","5","6","7","8","9","10","Валет","Дама","Король","Туз"]

class Card:

	__slots__ = ('value', 'suit')

	def __init__(self, dsuit, dval):
		self.value = dval
		self.suit = dsuits

	def display(self):
		return cardvalue[self.value] + " " + cardsuit[self.suit]

class Player:
	__slots__ = ('stack', 'nickname','hand_cards')

	def __init__(self, newstack, newnickname):
		self.stack = newstack
		self.nickname = newnickname
		self.with_cards = False
		self.hand_cards = []

	def bet(self,val):
		self.stack -= val

	def take_2_cards(self, argcards):
		self.hand_cards = argcards

class Combo:

	__slots__ = ('cardsondesk_combo')

	def __values(self, list_cards_class):
		n = []
		for card in list_cards_class:
			n.append(card.value)
		return n

	# todo: custom set comporator
	def __thereflush(self, list_cards_class, fr, to):
		suits = list_cards_class[fr:to]
		setted_suit = set(suits)
		if (len(setted_suit) == 1):
			return True
		else:
			return False

	def __therestraight(self, list_cards, fr, to):
		if self.__values(list_cards)[fr:to] == range(list_cards[0].value,to):
			return True
		else:
			return False

	def __init__(self, a, Man):
		self.cardsondesk_combo = a
		man_cards = Man.hand_cards
		self.cardsondesk_combo.append(man_cards[0])
		self.cardsondesk_combo.append(man_cards[1])

	def answer(self):
		self.cardsondesk_combo.sort(key = lambda card: card.value) # todo: Проверить!

		minimal_card = Card(self.cardsondesk_combo[0])
		# todo: cutom comporator
		uniques_length = len(self.cardsondesk_combo)

		temp = self.cardsondesk_combo

		if (uniques_length() >= 5):
			temp2 = values(temp)
			l = len(temp2)
			l1 = len(temp)

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

class Table:
	
	__slots__ = ('bets', 'players', 'deck', 'desk','lastBet', 'sb', 'bb', 'folded_score', 'all_game_money','player_bet', 'player_cursor','all_ined')
	
	def __init__(self, sb):
		self.bets = []
		self.players = []
		self.deck = []
		self.desk = []
		self.lastBet = 0
		self.sb = smallb
		self.bb = self.sb * 2
		self.folded_score = 0
		self.all_game_money = 0
		self.player_bet = 0
		self.player_cursor = 0
		self.all_ined = false
		generate_deck()
		shuffle_the_deck()

	def generate_deck(self):
		for i in range(13):
			for k in range(4):
				self.deck.append(Card(k, i))

	def shuffle_the_deck(self):
		random.shuffle(self.deck)

	def join_the_game(self, argnick, argstack):
		self.players.append(Player(argnick,argstack))

	def deal_hand_cards(self):
		for i in range(len(self.players)):
			new_hand_cards = []
			new_hand_cards.append(self.deck[-1])
			self.deck.pop()
			new_hand_cards.append(self.deck[-1])
			self.deck.pop()
			self.players[i].take_2_cards(new_hand_cards)
			self.players[i].with_cards = True

	def put_cards_on_desk(self, round):
		if (round == 1):
			for i in range(3):
				self.desk.append(self.deck[-1])
				self.deck.pop()
		elif (round != 0):
			self.desk.append(self.deck[-1])
			self.deck.pop()

	def make_dealer(self):
		self.dealer = self.players.index(random.choice(self.players))

	def make_zero_bets(self):
		for i in range(len(self.players)):
			self.bets.append(0)

	def bet_blinds(self):
		n = self.players.index(self.dealer)
		sbp = (n + 1) % len(self.players)
		bbp = (n + 2) % len(self.players)
		self.players[sbp].bet(self.sb)
		self.players[bbp].bet(self.bb)
		self.bets[sbp] = self.sb
		self.bets[bbp] = self.bb
		self.lastBet = self.bb
		self.player_cursor = bbp
		return sbp,bbp

	def calc_bank(self):
		summa = sum(self.bets) + self.folded_score
		return summa

	def bets_are_equal(self):
		if len(list(set(self.bets))) == 1:
			return True
		else:
			 return False

	def tableBet(self,player_i,player_bet):
		self.players[player_i].bet(player_bet)
		self.bets[player_i] += player_bet
		self.lastBet = self.bets[player_i]
		if self.players[self.player_cursor].stack == 0:
			self.all_in = True
		
	def someone_fold(self,player_i):
		self.folded_score += self.bets[player_i]
		self.bets.pop(player_i)
		self.players.pop(player_i)

	def p_cursor(self, find):
		if find:
			self.player_cursor = (self.player_cursor + 1) % len(self.players)
		else:
			return self.player_cursor
		

	def call_fold(self,p_answ):
		try:
			n = p_answ.index("fold")
			return True
		except:
			return False

	def end_bet_round(self):
		self.all_game_money += self.bets[0] * len(self.players)
		self.all_game_money += self.folded_score
		self.bets = []
		self.folded_score = 0
		self.lastBet = 0
		self.all_in = False
		self.make_zero_bets()

	def get_valid_bet(self,pred_bet):
		if pred_bet > self.players[self.p_cursor()].stack:
			return [0,"Вы делаете ставку больше вашего стека. Введите новую ставку:"]
		if pred_bet + self.bets[self.p_cursor()] < self.lastBet:
			return [0,"Вы делаете ставку меньше последнего бета. Введите новую ставку:"]
		obj.player_bet = pred_bet
		return [1,"Ставка принята"]

	def get_blinds(self):
		return self.sb,self.bb

	def try_combo(self,player_i):
		myCombo = Combo(self.desk, self.players[player_i])
		return myCombo.answer()