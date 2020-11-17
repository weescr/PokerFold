import random 
rounds = ["префлоп", "флоп", "терн", "ривер"]
class Dude:
	__slots__ = ('stack', 'nick')

	def __init__(self,nick,stack):
		self.stack = stack
		self.nick = nick

	def bet(self,sumalg):
		self.stack -= sumalg


class Table:
	
	__slots__ = ('sb', 'bb','bets','folded_score','lastBet','players', 'dealer','bank','player_cursor',"all_game_money","player_bet","all_in")
	
	def __init__(self, sb):
		self.bets = []
		self.players = []
		self.lastBet = []
		self.sb = sb
		self.bb = sb * 2
		self.player_cursor = 0
		self.folded_score = 0
		self.all_game_money = 0
		self.player_bet = 0
		self.all_in = False

	def join_the_game(self,nick,stack):
		self.players.append(Dude(nick,stack))

	def make_dealer(self):
		self.dealer = random.choice(self.players)
		self.player_cursor = self.players.index(self.dealer)

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
		return sbp,bbp

	def calc_bank(self):
		banking = sum(self.bets)
		banking += self.folded_score
		return banking

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

	def p_cursor(self,yes=None):
		if not yes:
			return self.player_cursor
		else:
			self.player_cursor = (self.player_cursor + 1) % len(self.players)

	def call_fold(self,p_answ):
		try:
			p_answ.index("fold")
			return False
		except:
			return True


	def end_bet_round(self):
		self.all_game_money += self.bets[0] * len(self.players)
		self.all_game_money += self.folded_score
		self.bets = []
		self.folded_score = 0
		self.lastBet = 0
		self.all_in = False
		self.make_zero_bets()



def get_valid_bet(obj,pred_bet):
	if pred_bet > obj.players[obj.p_cursor()].stack:
		print("Вы делаете ставку больше вашего стека. Введите новую")
		get_valid_bet(obj,int(input()))
	elif pred_bet + obj.bets[obj.p_cursor()] < obj.lastBet:
		print("Вы делаете ставку меньше последнего бета. Введите новую")
		get_valid_bet(obj,int(input()))
	else:
		obj.player_bet = pred_bet

def reflect_making_bets_process(obj):
	print("Ставку делает: {}".format(obj.players[obj.p_cursor()].nick ))
	print("Последняя ставка: {}".format( obj.lastBet ) )
	print("Ваш стек: {}".format(obj.players[obj.p_cursor()].stack))
	if obj.bets[obj.p_cursor()]:
		print("Вы уже до этого делали ставку. Ваш банк короче: {}".format(obj.bets[obj.p_cursor()]))



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
	print("=======Регистрация окончена=======")
	myTable.make_dealer()
	myTable.make_zero_bets()
	print("Button: {}".format(myTable.dealer.nick))

	for round in range(4):
		if round == 0:
			nn, mm = myTable.bet_blinds()
			print("Малый блайнд поставил: {}".format(myTable.players[nn].nick))
			print("Большой блайнд поставил: {}".format(myTable.players[mm].nick))
			myTable.p_cursor(next)
			myTable.p_cursor(next)
			myTable.p_cursor(next)
		print("============{}============".format(rounds[round]))
		reflect_making_bets_process(myTable)
		print("Введите новую ставку (0 - fold): ",end="")
		new_bet = int(input())
		if new_bet != 0:
			get_valid_bet(myTable,new_bet)
			myTable.tableBet(myTable.p_cursor(),myTable.player_bet)
			myTable.p_cursor(next)
			print("Ставка сделана. Следующий!! ======")
		else:
			myTable.someone_fold(myTable.p_cursor())
			if myTable.p_cursor() >= len(myTable.players):
				myTable.player_cursor = 0
			print("Упс... Кто то покину игру... =======")

		while myTable.bets_are_equal() != True:
			reflect_making_bets_process(myTable)
			#todo: all in
			print("all_in: {}".format(myTable.all_in))
			if myTable.all_in:
				print("Предыдущий игрок сделал олл ин. Вам остается только коллить или фолдить. call / fold?")
				answ = myTable.call_fold(input())
				if answ: # call
					myTable.tableBet(myTable.p_cursor(),myTable.bets[ (myTable.p_cursor() - 1) % len(myTable.players) ])
					myTable.p_cursor(next)
					print("Вы пошли олл-ин! ========")
				else: # fold
					myTable.someone_fold(myTable.p_cursor())
					if myTable.p_cursor() >= len(myTable.players):
						myTable.player_cursor = 0
					print("Упс... Он не соглаислся ставить олл-ин... ======")
			else:
				print("Введите новую ставку (0 - fold): ",end="")
				new_bet = int(input())
				if new_bet != 0:
					get_valid_bet(myTable,new_bet)
					myTable.tableBet(myTable.p_cursor(),myTable.player_bet)
					myTable.p_cursor(next)
					print("Ставка сделана. Следующий!! ======")
				else:
					myTable.someone_fold(myTable.p_cursor())
					if myTable.p_cursor() >= len(myTable.players):
						myTable.player_cursor = 0
					print("Упс... Кто то покинул игру... =======")
					#todo: баг возможно

		if len(myTable.players) == 1:
			print("Победил: {}, все остальные фолднули".format(myTable.players[0].nick))
			exit()
		print("Конец раунда. Общий банк: {}".format(myTable.calc_bank()))
		myTable.end_bet_round()


			




if __name__ == "__main__":
	main()