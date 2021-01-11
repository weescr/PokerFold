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
myserver.myTable.make_zero_bets()
hand_cards = myserver.myTable.deal_hand_cards()
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
	answer = myserver.myTable.bet_blinds(): #returns 2nicks
	if answer:	
		game_alert('sb and bb:',answer)
	things = myserver.get_new_things() #show_making_process
	game_alert('things:')
	for i in range(5):
		game_alert(things[i])
	game_alert('desk:',myserver.desk_everywhere()) #show_desk
	game_alert('i need a bet!')

	errors = in_game_get_bet_from_player()
	while errors != None:
		game_alert(errors) #players folded is error
		errors = in_game_get_bet_from_player() 

	while myserver.myTable.bets_are_equal() != True:
		things = myserver.get_new_things()
		game_alert('things:')
		for i in range(5):
			game_alert(things[i])
		if myserver.myTable.all_ined:
			if myserver.call_fold(in_game_input('The previous player was allined. And u?')):
				game_alert(players[myserver.myTable.player_cursor],', u r allined!')
				myserver.tableBet() #no args like player_cursor 'cause method must now it
				#myserver.change_cursor() todo: method tableBet must do it
			else:
				myserver.myTable.someone_fold(myTable.player_cursor)
				game_alert(players[myserver.myTable.player_cursor],"u r folded! u can't allined(((")
		else:
			new_bet = in_game_get_bet_from_player()
			if new_bet: #0 - false; 1+ - true (Python)
				errors = myserver.bet_handler(new_bet) #this one won't work. discuss and fix!
				if errors:
					while errors != None:
						game_alert(errors)
						new_bet = in_game_get_bet_from_player()
						errors = myserver.bet_handler(new_bet)
				myserver.tableBet(new_bet)
				myserver.myTable.change_cursor()
				game_alert('This bet is placed.')
			else:
				myserver.folded() #if cursor > len(players) must do method folded
				game_alert('U r folded')
	if len(myserver.players) == 1:
		game_alert('U r winner, ', myserver.players.name)
	game_alert('End of a round')
	myserver.end_bet_round()

	# todo: combo