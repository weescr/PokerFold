#!/bin/python

import server

myserver = server.Game(5)
players = [
	['nikita', 150],
	['ulyana', 300],
	['timur',  450],
	['maxim', 500]
]
errors = myserver.register(players)
if errors:
	print(errors)
	exit()

dealer_player = myserver.make_dealer()
myserver.make_zero_bets()
hand_cards = myserver.get_hands_cards()
#[			suit,value
#	['nikita', [3,5], [1,1]],
#	['ulyana', [1,1], [1,2]],
#	['timur', [2,10], [3,10]],
#	['maxim', [0,5], [1,5]],
#]

#function in-game
game_alert('Button:',dealer_player.name)
for round in myserver.rounds:
	new_cards_for_desk = myserver.get_desk_cards(round)
	game_alert('cards on desk now:',new_cards_for_desk)
	answer = myserver.need_blinds(): #returns 2nicks
	if answer:	
		game_alert('sb and bb:',answer)
	things = myserver.get_new_things() #show_making_process
	game_alert('things:',things)
	game_alert('desk:',myserver.desk_everywhere()) #show_desk
	game_alert('i need a bet!')
#errors true
	errors = True
	while errors != None:
		bet = in_game_get_bet_from_player(myserver.cursor)
		errors = myserver.bet_handler(bet) #players folded is error
		game_alert(errors) #maybe errors is None

	while myserver.bets_are_equal() != True:
		thinds = myserver.get_new_things()
		game_alert('things:',things)
		if myserver.all_ined:
			game_alert('The previous player was allined. And u?')
			if myserver.call_fold(in_game_vvod()):
				game_alert(players[myserver.cursor],', u r allined!')
				myserver.tableBet() #no args like player_cursor 'cause method must now it
				#myserver.change_cursor() todo: method tableBet must do it
			else:
				myserver.folded()
				game_alert(players[myserver.cursor],'u r folded! u can\'t allined(((')
		else:
			game_alert('ok. bet. (0 - fold)')
			new_bet = in_game_get_bet_from_player()
			if new_bet: #0 - false; 1+ - zero (Python)
				errors = myserver.bet_handler(new_bet)
				if errors:
					game_alert(errors)
					while error != None:
						new_bet = in_game_get_bet_from_player()
						errors = myserver.bet_handler(new_bet)
						game_alert(errors)
				myserver.tableBet(new_bet)
				#myserver.chane_cursor()
				game_alert('This bet is placed.')
			else:
				myserver.folded() #if cursor > len(players) must do method folded
				game_alert('U r folded')
	if len(myserver.players) == 1:
		game_alert('U r winner, ', myserver.players.name)
	game_alert('End of a round')
	myserver.end_bet_round()

	# todo: combo