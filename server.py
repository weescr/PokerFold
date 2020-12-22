import random
import operator

cardsuit = ["черви","вини","буби","крести"]
cardvalue = ["2","3","4","5","6","7","8","9","10","Валет","Дама","Король","Туз"]
rounds = ["ПреФлоп","Флоп","Терн","Ривер"]
rounds_eng = ["Preflop","Flop","Turn","River"]

class Card:

	__slots__ = ('value', 'suit')

	def __init__(self, dsuit, dval):
		self.value = dval
		self.suit = dsuit

	def __str__(self):
		return cardvalue[self.value] + " " + cardsuit[self.suit]

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

	__slots__ = ('cardsondesk_combo', 'man_cards')

	def __values(self, list_cards_class):
		n = []
		for card in list_cards_class:
			n.append(card.value)
		return n

	def __thereflush(self, list_cards_class, fr, to):
		suits = list_cards_class[fr:to]
		setted_suit = set(map(operator.attrgetter('suit'), suits))
		if len(setted_suit) == 1:
			return True
		else:
			return False

	def __therestraight(self, list_cards, fr, to):
		if self.__values(list_cards)[fr:to] == list(range(list_cards[0].value,to)):
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

		minimal_card = self.cardsondesk_combo[0]
		
		setted_cards = set(map(operator.attrgetter('value'), self.cardsondesk_combo))
		
		uniques_length = len(setted_cards)

		temp = setted_cards

		if (uniques_length >= 5):
			temp2 = self.__values(temp)
			l = len(temp2)
			l1 = len(temp)

			if (self.__thereflush(temp, l1-5, l1) and temp2[l-1] == 12 and temp2[l-2] == 11 and temp2[l-3] == 10 and temp2[l-4] == 9 and temp2[l-5] == 8):
				return "Royal Flush"

			for i in range (3):
				if (self.__therestraight(temp, 0+i, 5+i) and self.__thereflush(temp, 0+i, 5+i)):
					return "Straight Flush"

		if (uniques_length == 4 or uniques_length == 3 or uniques_length == 2):
			temp = self.__values(self.cardsondesk_combo)
			if (temp.count(temp[0]) == 4 or temp.count(temp[1]) == 4 or temp.count(temp[2]) == 4):
				return "Four of a Kind"
			return "Full House"

		if (self.__thereflush(temp, 0, 2) or self.__thereflush(temp, 1, 6) or self.__thereflush(temp, 2, 7)):
			return "Flush"

		for i in range(3):
			if (self.__therestraight(temp, 0+i, 5+i)):
				return "Straight"

		if (uniques_length == 5):
			temp = self.__values(self.cardsondesk_combo)
			for i in range(5):
				if (temp.count(temp[i]) == 3):
					return "Three of a kind / SET"
			return "Two Pairs"
			
		if (uniques_length == 6):
			return "One Pair"

		return "nothing"

class Table:
	
	__slots__ = ('bets', 'players', 'deck', 'desk','lastBet', 'sb', 'bb', 'folded_score', 'all_game_money','player_bet', 'player_cursor','all_ined')
	
	def __init__(self, smallb):
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
		self.all_ined = False
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
			new_hand_cards.append(self.deck.pop())
			new_hand_cards.append(self.deck.pop())
			self.players[i].take_2_cards(new_hand_cards)
			self.players[i].with_cards = True

	def put_cards_on_desk(self, round):
		if (round == 1):
			for i in range(3):
				self.desk.append(self.deck.pop())
				
		elif (round != 0):
			self.desk.append(self.deck.pop())

	def make_dealer(self):
		self.dealer = self.players.index(random.choice(self.players))

	def make_zero_bets(self):
		for i in range(len(self.players)):
			self.bets.append(0) # todo: оптимизировать

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
		return sum(self.bets) + self.folded_score

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

	def p_cursor(self, find=None):
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
		if pred_bet > self.players[self.player_cursor].stack:
			return [0,"Вы делаете ставку больше вашего стека. Введите новую ставку:"]
		if pred_bet + self.bets[self.player_cursor] < self.lastBet:
			return [0,"Вы делаете ставку меньше последнего бета. Введите новую ставку:"]
		self.player_bet = pred_bet
		return [1,"Ставка принята"]

	def get_blinds(self):
		return self.sb, self.bb

	def try_combo(self,player_i):
		return Combo(self.desk, self.players[player_i]).answer()

class Game(Table, Combo, Card, Player):
	
	def __init__(self):
		pass

	def show_making_bets_process(self, table_obj):
		print( "Player: {} ".format(table_obj.players[table_obj.player_cursor].nickname))

		if (table_obj.players[table_obj.player_cursor].with_cards):
			player_cards = table_obj.players[table_obj.player_cursor].hand_cards
			print("Your cards: {} && {} ".format(player_cards[0].display(),player_cards[1].display()))

		print("Last Bet: {} ".format(table_obj.lastBet))
		print("Stack: {} ".format(table_obj.players[table_obj.player_cursor].stack))

		if (table_obj.bets[table_obj.p_cursor()] != 0):
			print("Personal bank: {} ".format(table_obj.bets[obj.player_cursor]))

	def show_desk(self, table_obj):
		print("|")
		if len(table_obj.desk) != 0:
			for i in table_obj.desk:
				print("{} | ".format(i.display()))

	def players_register(self, table_obj):
		nplayers = int(input("How many players are playing today? "))
		for i in range(nplayers):
			temp_nick = input("New player name: ")
			while(list(table_obj.get_blinds())[1] > temp_stack):
				temp_stack = int(input("New player stack: "))
				if (list(table_obj.get_blinds())[1] > temp_stack):
					print("Your stack is too small")
			print("Registered!")
			table_obj.join_the_game(temp_nick,temp_stack)
		return table_obj

	def main(self):
		print("PokerFold (v. 0.1)")
		if __name__ == "__main__": # todo: учитель называется блять, нет бы объяснил, что не нравится
			preTable = Table(5)
			print("==========Registration of new players=========")
			print("Blinds are: {} / {}".format(list(preTable.get_blinds())[0], list(preTable.get_blinds())[1]))

			myTable =  players_register(preTable)
			print("=======Registration of new players is over======")
			myTable.make_dealer()
			myTable.make_zero_bets()
			myTable.deal_hand_cards()

			print("Button: {}".format(myTable.dealer.nickname))

			for round in range(4):
				myTable.put_cards_on_desk(round)
				if (round == 0):
					players_blinds = list(myTable.bet_blinds())
					print("SB / BB: {} & {}".format(myTable.players[players_blinds[0]].nickname, myTable.players[players_blinds[1]].nickname))
					myTable.p_cursor(true)
				print("====== {} ======".format(rounds_eng[round]))
				show_making_bets_process(myTable)
				new_bet = int(input("Enter a new bet (0 - fold): "))
				show_desk(myTable)

				if (new_bet != 0):
					while (myTable.get_valid_bet(new_bet)[0] == 0 ):
						new_bet = int(input(myTable.get_valid_bet(new_bet)[1]))
					myTable.tableBet(myTable.p_cursor(), myTable.player_bet)
					myTable.p_cursor(true)
					print("======The bet is placed. Next player!!======")
				else:
					myTable.someone_fold(myTable.p_cursor())
					if (myTable.p_cursor() >= len(myTable.players)):
						myTable.player_cursor = 0
					print("=======Oops ... Someone left the game ...=======")

				while (myTable.bets_are_equal() != true):
					show_making_bets_process(myTable)
					if (myTable.all_ined):
						answ = input("The previous player was all in. All you have to do is call or fold. call / fold? ")
						if (myTable.call_fold(answ)):
							myTable.tableBet(myTable.player_cursor,myTable.bets[(myTable.player_cursor - 1) % len(myTable.players)])
							myTable.p_cursor(true)
							print("You're all-in! ========")
						else:
							myTable.someone_fold(myTable.player_cursor)
							if (myTable.player_cursor >= len(myTable.players)):
								myTable.player_cursor = 0
							print("Oops ... He didn't agree to put all-in ... ======")
					else:
						new_bet = int("Enter a new bet (0 - fold): ")

						if (new_bet != 0):
							while (myTable.get_valid_bet(new_bet)[1] == 0 ):
								new_bet = int(input(myTable.get_valid_bet(new_bet)[1]))
							myTable.tableBet(myTable.p_cursor(),myTable.player_bet)
							myTable.p_cursor(true)
							printf("======The bet is placed. Next player !!======")
						else:
							myTable.someone_fold(myTable.p_cursor())
							if (myTable.p_cursor() >= len(myTable.players)):
								myTable.player_cursor = 0
							print("=======Oops ... Someone left the game ...=======")

				if (len(myTable.players) == 1):
					print("Defeated {}, all others folded".format(myTable.players[0].nickname))
				print("End of the round. Common bank: {}".format myTable.calc_bank())
				myTable.end_bet_round()

			print("==========We open up!==========")
			show_desk(myTable)
			for i in range(len(myTable.players)):
				if __name__ == "__main__": # та же ошибка, что и выше, ведь мне никто не собирается объяснять, что же блять не так
					myCombo = Combo(myTable.desk,myTable.players[i])
					player_hands = myTable.players[i].hand_cards()
					print("Player: {}".format(myTable.players[i].nickname))
					print("Hand cards: {} && {} ".format(player_hands[0].display(),player_hands[1]display()))
					print("Combination: {}".format(myCombo.answer()))
					print("==================================")
			print("End of the game.")
			return 0