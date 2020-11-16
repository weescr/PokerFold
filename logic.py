import random 

class Dude:
	__slots__ = ('stack', 'nick')

	def __init__(self,nick,stack):
		self.stack = stack
		self.nick = nick

	def bet(self,sum):
		self.stack -= sum


class Table:
	
	__slots__ = ('sb', 'bb','bets','folded_bets','lastBet','players', 'dealer','bank','player_cursor',"all_game_money")
	
	def __init__(self, sb):
		self.bets = []
		self.players = []
		self.lastBet = []
		self.sb = sb
		self.bb = sb * 2
		self.player_cursor = 0
		self.folded_bets = []
		self.all_game_money = []

	def join_the_game(self,nick,stack):
		self.players.append(Dude(nick,stack))

	def make_dealer(self):
		self.dealer = random.choice(self.players)
		self.player_cursor = self.players.index(self.dealer)

	def make_zero_bets(self):
		for i in range(len(self.players)):
			self.bets.append(0)

	def whose_blind(self):
		n = self.players.index(self.dealer)
		sbp = (n + 1) % len(self.players)
		bbp = (n + 2) % len(self.players)
		return sbp,bbp

	def bet_blinds(self):
		n, m = self.whose_blind()
		self.players[n].bet(self.sb)
		self.players[m].bet(self.bb)
		self.bets[n] = self.sb
		self.bets[m] = self.bb
		self.lastBet = self.bb

	def calc_bank(self):
		banking = sum(self.bets)
		return banking

	def bets_are_equal(self):
		if len(list(set(self.bets))) == 1:
			return True
		else:
			#print("bets не экуал т.к len(list(set(self.bets)) == ",len(list(set(self.bets))))
			return False

	def tableBet(self,player_i,player_bet):
		self.players[player_i].bet(player_bet)
		self.bets[player_i] += player_bet
		self.lastBet = player_bet

	def someone_fold(self,player_i):
		self.folded_bets.append(self.bets[player_i])
		self.bets.pop(player_i)
		self.players.pop(player_i)

	def p_cursor(self,yes=None):
		if not yes:
			return self.player_cursor
		else:
			self.player_cursor = (self.player_cursor + 1) % len(self.players)

	def all_game_money_is():
		if self.all_game_money = 0:
			return sum(self.bets)

	def end_bet_round(self):
		self.all_game_money += self.bets[0] * len(self.players)

		pass

def get_valid_bet(obj,pred_bet,table):
	if pred_bet > obj.players[obj.p_cursor()].stack:
		print("Вы делаете ставку больше вашего стека. Введите новую")
		get_valid_bet(obj,int(input()), table.p_cursor())
	if pred_bet + table.bets[table.p_cursor()] < obj.lastBet:
		print("Вы делаете ставку меньше последнего бета. Введите новую")
		get_valid_bet(obj,int(input()),table.p_cursor())
	return pred_bet



def main():
	print('Poker')
	myTable = Table(5)
	print("Блайнды: {}/{}".format(myTable.sb,myTable.bb))
	print('Сколько игроков сегодня играет? ', end="")
	n = int(input())
	for i in range(n):
		print("Введите имя игрока: ", end="")
		nick = input()
		print("Введите стек: ", end="")
		stack = int(input())
		while myTable.bb > stack:
			print("Ваш стек слишком маленький")
			stack = int(input())
		myTable.join_the_game(nick,stack)

	#print("Игра начинается...")
	myTable.make_dealer()
	myTable.make_zero_bets()
	#print("Button: {}".format(myTable.dealer.nick))

	for round in range(4):
		if round == 0:
			#print("Ставим блайнды")
			myTable.bet_blinds()
			nn, mm = myTable.whose_blind()
			#print("Малый блайнд поставил: {}".format(myTable.players[nn].nick))
			#print("Большой блайнд поставил: {}".format(myTable.players[mm].nick))
			myTable.p_cursor(next)

		while myTable.bets_are_equal() != True:
			print("Ставку делает: {}".format(myTable.players[myTable.p_cursor()].nick))
			#print("Текущий банк: {}".format(myTable.calc_bank()))
			#print("Ваш стек: {}".format(myTable.players[myTable.p_cursor()].stack))
			print("Ставки: {}".format(myTable.bets))
			print("Банк: {}".format( myTable.all_game_money_is() ))
			print("Ваш банк: {}".format(myTable.bets[myTable.p_cursor()]))
			print("Введите новую ставку (0 - fold): ",end="")
			new_bet = int(input())
			if new_bet != 0:
				player_bet = get_valid_bet(myTable,new_bet,myTable)
				myTable.tableBet(myTable.p_cursor(), player_bet)
				myTable.p_cursor(next)
				print("Ставка в {} принята для игрока {}, ваш банк теперь: {}".format(new_bet,myTable.players[myTable.p_cursor()].nick,myTable.bets[myTable.p_cursor()]))
			else:
				myTable.someone_fold(myTable.p_cursor())
				if myTable.p_cursor() >= len(myTable.players):
					myTable.player_cursor = 0
			print("BETS ARE EQUAL? {}".format(myTable.bets))
		if len(myTable.players) == 1:
			print("Победил: {}, все остальные фолднули".format(myTable.players[0]))
			exit()
		print("Конец раунда")
		myTable.end_bet_round()


			




if __name__ == "__main__":
	main()